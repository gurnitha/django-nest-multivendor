## BUILDING MULTIVENDOR ECOMMERCE USING DJANGO
Based on Desphixs tutorials on Youtube
Github repository: https://github.com/gurnitha/django-nest-multivendor


## 1. Setup project

#### 1.1 Create a new Github repository 

#### 1.2 Create virtual environment

#### 1.3 Activate venv3932, install django==3.2, and upgrade pip 

#### 1.4 Create new project named config

        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py

#### 1.5 Create a new app: app/core

        (venv3932) λ mkdir app\core
        (venv3932) λ django-admin startapp core app\core

        new file:   app/core/__init__.py
        new file:   app/core/admin.py
        new file:   app/core/apps.py
        new file:   app/core/migrations/__init__.py
        new file:   app/core/models.py
        new file:   app/core/tests.py
        new file:   app/core/views.py

#### 1.6 Register core app to config/settings.py, run the server

        modified:   app/core/apps.py
        modified:   config/settings.py

#### 1.7 Hello Wordl using url, view and templates

        new file:   app/core/urls.py
        modified:   app/core/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/app/core/index.html

