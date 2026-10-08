from pathlib import Path
import base64,io
import numpy as np
import torch
import torch.nn as nn
from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image
BASE_DIR=Path(__file__).resolve().parent.parent
CHECKPOINT=BASE_DIR/'artifacts'/'ddpm_mnist.pt'
T=100
BETAS=torch.linspace(1e-4,0.02,T); ALPHAS=1-BETAS; ALPHA_BARS=torch.cumprod(ALPHAS,0)
class TinyDenoiser(nn.Module):
    def __init__(self):
        super().__init__()
        self.time=nn.Sequential(nn.Linear(1,32),nn.SiLU(),nn.Linear(32,32),nn.SiLU())
        self.down=nn.Sequential(nn.Conv2d(1,32,3,padding=1),nn.SiLU(),nn.Conv2d(32,64,3,stride=2,padding=1),nn.SiLU())
        self.mid=nn.Sequential(nn.Conv2d(64,64,3,padding=1),nn.SiLU())
        self.up=nn.Sequential(nn.ConvTranspose2d(64,32,4,stride=2,padding=1),nn.SiLU(),nn.Conv2d(32,1,3,padding=1))
    def forward(self,x,t):
        emb=self.time((t.float()/T).view(-1,1)).view(-1,32,1,1)
        h=self.down(x); h=h+emb.repeat(1,2,1,1); return self.up(self.mid(h))
def load_model():
    if not CHECKPOINT.exists(): return None
    model=TinyDenoiser().cpu(); model.load_state_dict(torch.load(CHECKPOINT,map_location='cpu')); model.eval(); return model
@torch.no_grad()
def sample(model,count=16):
    x=torch.randn(count,1,28,28)
    for step in range(T-1,-1,-1):
        t=torch.full((count,),step,dtype=torch.long); pred=model(x,t)
        alpha=ALPHAS[step]; abar=ALPHA_BARS[step]; beta=BETAS[step]
        mean=(x-(beta/torch.sqrt(1-abar))*pred)/torch.sqrt(alpha)
        x=mean+torch.sqrt(beta)*torch.randn_like(x) if step>0 else mean
    return x.clamp(-1,1)
def grid_png(images):
    images=((images+1)*127.5).byte().numpy()[:,0]; canvas=np.zeros((112,112),dtype=np.uint8)
    for i,image in enumerate(images[:16]):
        r,c=divmod(i,4); canvas[r*28:(r+1)*28,c*28:(c+1)*28]=image
    b=io.BytesIO(); Image.fromarray(canvas).resize((336,336),Image.Resampling.NEAREST).save(b,format='PNG'); return base64.b64encode(b.getvalue()).decode()
def home(request): return render(request,'index.html',{'checkpoint_ready':CHECKPOINT.exists()})
def generate(request):
    model=load_model()
    if model is None: return HttpResponse('Train the notebook first and save artifacts/ddpm_mnist.pt.',status=503)
    return render(request,'index.html',{'checkpoint_ready':True,'image':grid_png(sample(model))})
