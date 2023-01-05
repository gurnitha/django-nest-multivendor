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

        1. pip install django-decoupl
        2. Install python-decouple: pip install django-decouple
        3. Create .env file inside the project
        4. Adding parameter to .env file
        5. Use the parameter in .env file in config/settings.py
        6. Add .env in .gitignore file before git commit
        7. Configur BASE_DIR in settings.py if found error:
        
        # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))

        modified:   README.md
        modified:   config/settings.py

## 3. Custome user model

#### 3.1 Create a new app: app/userauth

        (venv3932) λ mkdir app\userauth
        (venv3932) λ django-admin startapp userauth app\userauth

        modified:   README.md
        new file:   app/userauth/__init__.py
        new file:   app/userauth/admin.py
        new file:   app/userauth/apps.py
        new file:   app/userauth/migrations/__init__.py
        new file:   app/userauth/models.py
        new file:   app/userauth/tests.py
        new file:   app/userauth/views.py

#### 3.2 Register userauth app to config/settings.py

        modified:   README.md
        modified:   app/userauth/apps.py
        modified:   config/settings.py

#### 3.3 Create custom class User(AbstractUser): in userauth/models.py

        It will create errors as seen bellow!

        ERRORS:                                                                                                                 
        auth.User.groups: (fields.E304) Reverse accessor for 'auth.User.groups' clashes with reverse accessor for 'userauth.User
        .groups'.                                                                                                               
                HINT: Add or change a related_name argument to the definition for 'auth.User.groups' or 'userauth.User.groups'. 

        modified:   README.md
        modified:   app/userauth/models.py
        modified:   config/settings.py

#### 3.4 Add AUTH_USER_MODEL = 'userauth.User' in config/settings.py

        It will raise warning like this:

        raise ValueError("Dependency on app with no migrations: %s" % key[0])
        ValueError: Dependency on app with no migrations: userauth
        
        modified:   README.md
        modified:   config/settings.py

#### 3.5 Run makemigrations and migrate and runserver

        modified:   README.md
        new file:   app/userauth/migrations/0001_initial.py

#### 3.6 Create superuser, run server and login to admin

        (venv3932) λ python manage.py createsuperuser
        Email: x
        Username: x
        Password:
        Password (again):
        ...
        Superuser created successfully.

        modified:   README.md

#### 3.7 Register User model to admin.py

        modified:   README.md
        modified:   app/userauth/admin.py

#### 3.8 Customising user display in admin panel

    modified:   README.md
    modified:   app/userauth/admin.py

## 4. Setting up admin panel

#### 4.1 Install django-jazzmin: pip install -U django-jazzmin

        modified:   README.md

#### 4.2 Add jazzmin in config/INSTALLED_APPS and re-run the server

        INSTALLED_APPS = [

            # New
            'jazzmin',
        ...

        modified:   README.md
        modified:   config/settings.py

#### 4.3 Configuring jazzmin for its look in admin panel

        modified:   README.md
        modified:   config/settings.py

## 5. User register system

#### 5.1 Create register_view method to render sign-up page

        modified:   README.md
        new file:   app/userauth/urls.py
        modified:   app/userauth/views.py
        modified:   config/urls.py
        new file:   templates/app/userauth/sign-up.html

#### 5.2 Create form class UserRegisterForm (UserCreationForm) in: app/userauth/forms.py and reder its instances to sign-up page

        modified:   README.md
        new file:   app/userauth/forms.py
        modified:   app/userauth/views.py
        modified:   templates/app/userauth/sign-up.html

#### 5.3 Use UserRegisterForm in register_view method to register a new user

        modified:   README.md
        modified:   app/userauth/views.py
        modified:   templates/app/userauth/sign-up.html

#### 5.4 Redirect signed up user to login page

        modified:   README.md
        modified:   app/userauth/urls.py
        modified:   app/userauth/views.py
        new file:   templates/app/userauth/sign-in.html

#### 5.5 Add template to register page and renamed sign-up and sign-in files

        modified:   README.md
        modified:   app/userauth/urls.py
        modified:   app/userauth/views.py
        renamed:    templates/app/userauth/sign-in.html -> templates/app/userauth/login.html
        new file:   templates/app/userauth/register.html
        deleted:    templates/app/userauth/sign-up.html

#### 5.6 Configure the register page - delete form input

        modified:   README.md
        modified:   templates/app/userauth/register.html

#### 5.7 Configure the register page - add widget in forms.py and use it in the regiter page

        modified:   README.md
        modified:   app/userauth/forms.py
        modified:   templates/app/userauth/register.html

#### 5.8 Configure the register page - showing error messages to register page

        modified:   README.md
        modified:   templates/app/userauth/register.html

## 6. User login system

#### 6.1 Add logic to login_view

        modified:   README.md
        modified:   app/userauth/views.py

#### 6.2 Add template to login page and login


        modified:   README.md
        modified:   app/userauth/views.py
        modified:   templates/app/userauth/login.html
        modified:   templates/app/userauth/register.html

        NOTE:

        The code bellow, does not work as code in the tutorials.
        It works, but could not access the login page.
        For now, I disabled it.
        And I could logged in successfully.

## 7. User logout system

#### 7.1 Logout a user

        modified:   app/userauth/urls.py
        modified:   app/userauth/views.py
        modified:   templates/app/userauth/login.html
        modified:   templates/partials/header.html

        NOTE:

        1. Logout user
        2. Add some links
        3. User logged out, but the menu still showing log-out menu

        Next: hiding log-out menu if user logged in.

#### 7.2 Hiding logout and login menu in header

        modified:   README.md
        modified:   templates/partials/header.html

## 8. Alerts in Django

#### 8.1 Looping alert messages in the header

        modified:   README.md
        modified:   app/userauth/views.py
        modified:   templates/partials/header.html

        NOTE:

        Problem:

        Alert message remains stay or does not disappear.
        To make it disappear, we have to refresh the browser.
        But this is not what we want.

        Solution:

        Use jQuery to solve it.

#### 8.2 Use jQuery to make alert disappear automatically in some seconds

        modified:   README.md
        modified:   templates/base.html
        modified:   templates/partials/header.html

        NOTE:

        Add jQery CDN and Ajax in the header.
        It works.

#### 9.1 Create django model, migrations, and admin

        modified:   app/core/admin.py
        new file:   app/core/migrations/0001_initial.py
        new file:   app/core/migrations/0002_vendor.py
        new file:   app/core/migrations/0003_product_tag.py
        new file:   app/core/migrations/0004_productimage.py
        new file:   app/core/migrations/0005_cartorder.py
        new file:   app/core/migrations/0006_cartorderitem.py
        new file:   app/core/migrations/0007_productreview.py
        new file:   app/core/migrations/0008_wishlist.py
        new file:   app/core/migrations/0009_address.py
        modified:   app/core/models.py

        NOTE:

        max_digits = 99999999999999 does not work in postgresql

#### 9.2 Modify Product model

        modified:   app/core/admin.py
        new file:   app/core/migrations/0010_auto_20230104_0821.py
        modified:   app/core/models.py

#### 9.3 Modify Category model

        modified:   app/core/admin.py
        new file:   app/core/migrations/0011_auto_20230104_0827.py
        modified:   app/core/models.py

#### 9.4 Modify Vendor model

        modified:   app/core/admin.py
        new file:   app/core/migrations/0012_auto_20230104_0829.py
        modified:   app/core/models.py

#### 9.5 Modify ProductImage model

        new file:   app/core/migrations/0013_auto_20230104_0831.py
        modified:   app/core/models.py

#### 9.6 Modify CartOrder model

        modified:   app/core/admin.py
        new file:   app/core/migrations/0014_auto_20230104_0834.py
        modified:   app/core/models.py

#### 9.7 Modify CartOrderItem model

        modified:   app/core/admin.py
        new file:   app/core/migrations/0015_auto_20230104_0836.py
        modified:   app/core/models.py

#### 9.8 Modify ProductReview model

        modified:   app/core/admin.py
        new file:   app/core/migrations/0016_auto_20230104_0851.py
        modified:   app/core/models.py

        NOTE:

        Modified image field in the Product model: form image to prod_image

#### 9.9 Modify Wishlist model

        modified:   app/core/admin.py
        new file:   app/core/migrations/0017_auto_20230104_0859.py
        modified:   app/core/models.py

#### 9.10 Modify Product model

        modified:   app/core/admin.py
        new file:   app/core/migrations/0018_auto_20230104_0901.py
        modified:   app/core/models.py

#### 9.11 Modify Product model by adding vendor field

        modified:   README.md
        new file:   app/core/migrations/0019_product_vendor.py
        modified:   app/core/models.py

## 10. Product list view

#### 10.1 Display all products to homepage without filter

        modified:   README.md                                            
        modified:   app/core/admin.py                                    
        new file:   app/core/migrations/0020_auto_20230104_2253.py       
        new file:   app/core/migrations/0021_rename_pro_status_choice_pro
        modified:   app/core/models.py                                   
        modified:   app/core/views.py                                    
        new file:   media/category/product-1-1.jpg                       
        ...    
        modified:   templates/app/core/index.html                        
        modified:   templates/base.html 

        NOTE:

        Some modifies were made in the Product model and admin, as well in the template    

#### 10.2 Display all products to homepage with filter

        products = Product.objects.filter(status_choice='published', featured=True)

        modified:   README.md
        modified:   app/core/views.py

## 11. Products list

#### 11.1 Create products list page - urls, views, templates

        modified:   README.md
        modified:   app/core/urls.py
        modified:   app/core/views.py
        new file:   templates/app/core/product_list_view.html

#### 11.2 Create products list page - add template

        modified:   README.md
        modified:   app/core/urls.py
        modified:   app/core/views.py
        new file:   templates/app/core/product_list.html

#### 11.3 Create products list page - loading static files

        modified:   README.md
        modified:   templates/app/core/product_list.html

#### 11.4 Create products list page - add logic to view and loop products to products-list

        modified:   app/core/views.py
        modified:   templates/app/core/product_list.html

## 12. Category

#### 12.1 Create category-list page - urls, views, templates

        modified:   README.md
        modified:   app/core/urls.py
        modified:   app/core/views.py
        new file:   templates/app/core/category_list.html

#### 12.2 Create category-list page - add template to category-list page

        modified:   README.md
        modified:   app/core/views.py
        modified:   templates/app/core/category_list.html

#### 12.3 Create category-list page - Load static files

        modified:   README.md
        modified:   templates/app/core/category_list.html

#### 12.4 Create category-list page - Modify the template

        modified:   README.md
        modified:   templates/app/core/category_list.html

#### 12.5 Create category-list page - Add logic to view and loop categories to category-list

        modified:   README.md
        modified:   app/core/views.py
        modified:   templates/app/core/category_list.html

#### 12.6 Create category-list page - Showing all products belong to a category

        modified:   README.md
        modified:   app/core/admin.py
        new file:   app/core/migrations/0022_alter_product_category.py
        modified:   app/core/models.py
        modified:   templates/app/core/category_list.html

#### 12.7 Create category-list page - Showing all products belong to a category in the sidebar

        modified:   README.md
        modified:   templates/app/core/category_list.html

## 13. Product-based Category List View

#### 13.1 Create product belong to a category - urls, view, templates

        modified:   app/core/urls.py
        modified:   app/core/views.py
        new file:   templates/app/core/product_belong_to_a_category_list.html

#### 13.2 Create product belong to a category - add template

        modified:   README.md
        modified:   app/core/urls.py
        modified:   app/core/views.py
        deleted:    templates/app/core/product_belong_to_a_category_list.html
        new file:   templates/app/core/product_by_category_list.html

#### 13.3 Create product belong to a category - load static files

        modified:   README.md
        modified:   templates/app/core/product_by_category_list.html

