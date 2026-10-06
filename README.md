# Diffusion Model from Scratch

A lightweight, notebook-first implementation of a **Denoising Diffusion Probabilistic Model (DDPM)** for generating small handwritten digit images.

The project is designed for CPU-only machines and limited disk space. It uses MNIST, a compact open dataset, and a small convolutional denoiser rather than a large image-generation model.

## What this project demonstrates

- Forward diffusion: gradually add Gaussian noise to an image.
- Reverse diffusion: learn to predict the noise and reconstruct an image.
- A small DDPM implemented directly with PyTorch.
- Sampling from pure noise to generate new images.
- A Django web application for an interview-ready interactive demo.
- Reproducible, configurable training with CPU-safe defaults.

## Repository structure

```text
Diffusion-Model-from-Scratch/
├── diffusion_demo/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── notebooks/
│   └── 01_ddpm_from_scratch.ipynb
├── diffusion_site/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTE.md
├── LICENSE
├── README.md
├── manage.py
└── requirements.txt
```

There is intentionally **no `src/` directory**, no preprocessing module, and no separate ML script. The notebook is the main implementation; the Django app contains only the small amount of inference code needed by the demo.

## Quick start

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Training

Open `notebooks/01_ddpm_from_scratch.ipynb` in Jupyter. The notebook downloads MNIST automatically through `torchvision` and defaults to a small subset suitable for CPU experimentation.

After training, save the model as:

```text
artifacts/ddpm_mnist.pt
```

The Django demo automatically looks for that checkpoint. The `artifacts/` directory is ignored by Git because model checkpoints are generated files.

## CPU / disk friendly settings

The notebook uses 28×28 MNIST images, a compact model, a small diffusion schedule, and configurable `TRAIN_SAMPLES`, `EPOCHS`, and `BATCH_SIZE`. Increase them gradually when more compute is available.

For an interview demonstration, explain that this is an educational DDPM implementation rather than a production-scale Stable Diffusion system. The same forward/reverse diffusion principle scales to much larger architectures and datasets.

## Profiles

- GitHub: https://github.com/InfinitePraveen
- LinkedIn: https://www.linkedin.com/in/infinitepraveen/

## License

MIT License.
