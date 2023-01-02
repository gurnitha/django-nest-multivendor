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

#### 1.8 Add html template to index

        modified:   .gitignore
        modified:   templates/app/core/index.html

#### 1.9 Setting up static and media files

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py

#### 1.10 Add and loading static files

        modified:   README.md
        modified:   templates/app/core/index.html

#### 1.11 Template inheritance

        modified:   README.md
        modified:   templates/app/core/index.html
        new file:   templates/base.html
        new file:   templates/partials/footer.html
        new file:   templates/partials/header.html
        new file:   templates/partials/modals.html
        new file:   templates/partials/nav-bar.html
        new file:   templates/partials/nav-mobile.html
        new file:   templates/partials/preloader.html
        new file:   templates/partials/quickview.html

## 2. Setting up PostgreSQL database

#### 2.1 Install psycopg2 driver: pip install psycopg2

        modified:   README.md

#### 2.2 Create and connect database with the project

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'django-nest-multivendor',
                'USER': 'postgres',
                'PASSWORD': 'x',
                'HOST': 'localhost'
            }
        }

        modified:   README.md
        modified:   config/settings.py

#### 2.3 Protecting project configuration files

        pip install django-decoupl
        Install python-decouple: pip install django-decouple
        Create .env file inside the project
        Adding parameter to .env file
        Use the parameter in .env file in config/settings.py
        Add .env in .gitignore file before git commit
        Configur BASE_DIR in settings.py if found error:
        # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))

        modified:   README.md
        modified:   config/settings.py

