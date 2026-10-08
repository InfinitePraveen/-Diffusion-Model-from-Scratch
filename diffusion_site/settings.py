from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY='dev-only-diffusion-demo-key'
DEBUG=True
ALLOWED_HOSTS=[]
INSTALLED_APPS=['django.contrib.contenttypes','django.contrib.staticfiles','diffusion_demo']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware','django.middleware.common.CommonMiddleware']
ROOT_URLCONF='diffusion_site.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'diffusion_demo'/'templates'],'APP_DIRS':True,'OPTIONS':{'context_processors':[]}}]
WSGI_APPLICATION='diffusion_site.wsgi.application'
DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
LANGUAGE_CODE='en-us'; TIME_ZONE='Asia/Kolkata'; USE_I18N=True; USE_TZ=True
STATIC_URL='static/'
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
