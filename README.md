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
        

## 9. Django model: Product, Category, Vendor, ProductImage, CartOrder, Wishlist


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


#### 13.4 Create product belong to a category - dispaly all products belong to a category

        modified:   README.md
        modified:   app/core/views.py
        modified:   templates/app/core/category_list.html
        modified:   templates/app/core/product_by_category_list.html


## 14. Django Context Processors (video 18)


#### 14.1 Load category in nav-bar using context_processors

        modified:   README.md
        new file:   app/core/context_processors.py
        modified:   config/settings.py
        modified:   templates/partials/nav-bar.html

        Activities:

        1. Create a new file: app/core/context_processors.py
        2. Within this file, do these:
                -imort Category model
                -create defualt() method 
                -retrieve categories from db
        3. Register this default() method in settings.py
        4. Create category menu in nav-bar
        5. Load (loop) categories in nav-bar
        6. Testing: refresh the browser
        7. Restult: ok


#### 14.2 Load all categories page and product by category page in nav-bar

        Activities:

        1. Add links to nav-bar for product by category page
        2. Add links to nav-bar for all categories page
        3. Testing: refresh the page and click the menu
        4. Result: ok

        modified:   README.md
        modified:   templates/partials/nav-bar.html


#### 14.3 Load all categories page and product by category page in nav-mobile

        modified:   README.md
        modified:   templates/partials/nav-mobile.html

        Activities:

        1. Add links to nav-mobile for product by category page
        2. Add links to nav-mobile for all categories page
        3. Testing: refresh the page and click the menu
        4. Result: ok

        modified:   README.md
        modified:   templates/partials/nav-bar.html


#### 14.4 Load all categories page and product by category page in nav-brows-all-categories

        modified:   README.md
        modified:   app/core/context_processors.py
        modified:   templates/partials/header.html
        new file:   templates/partials/nav-brows-all-categories.html

        Activities:

        1. In templates/partials reate nav-brows-all-categories.html file
        2. Move Brows All Categories menu to nav-brows-all-categories.html from header.html
        3. Include nav-brows-all-categories.html in header.html
        4. Slice category in default() method in context-processors.html
        5. Load/loop categories instance to nav-brows-all-categories.html
        6. Testing: refresh browser
        7. Result: all good


#### 14.5 Load all categories page and product by category page in nav-brows-all-categories (show more ...)

        modified:   app/core/context_processors.py
        modified:   templates/partials/nav-brows-all-categories.html

        Activities:

        1. Slicing category instances in default() method in context_processors.py
        2. Load/loop categories instance to nav-brows-all-categories.html
        3. Testing: refresh browser
        4. Result: all good

        NOTE:

        The display in menu Brows All Category is not so neat, due to the menu lengths
        are not the same.


#### 14.6 Add links to some category menu

        modified:   README.md
        modified:   templates/app/core/category_list.html
        modified:   templates/app/core/product_by_category_list.html
        modified:   templates/app/core/product_list.html
        modified:   templates/partials/header.html

        Activities:

        1. Add link to breadcrum of menu category 


#### 14.7 Add links to menu-related categories

        modified:   app/core/context_processors.py
        new file:   media/category/thumbnail-3.jpg
        new file:   media/category/thumbnail-4.jpg
        new file:   media/user_directory_path/product-13-2.jpg
        new file:   media/user_directory_path/thumbnail-3.jpg
        modified:   templates/app/core/index.html
        modified:   templates/partials/nav-bar.html
        modified:   templates/partials/nav-brows-all-categories.html


## 15. Vendors


#### 15.1 Vendor list: urls, views, templates

        modified:   README.md
        modified:   app/core/urls.py
        modified:   app/core/views.py
        new file:   templates/app/core/vendor_list.html

        Activities:

        1. Create vendors path
        2. Create vendor_list_view function
        3. Create vendors template and some dummy text
        4. Testing: start server and load vendors in the browser
        5. Result: ok

        NEXT: Add vendors template


#### 15.2 Add template to vendors page

        modified:   README.md
        modified:   templates/app/core/vendor_list.html

        Activities:

        1. Adding html template to vendors page

        NEXT: Define logic to vendor_list_view function       


#### 15.3 Add logic to vendor_list_view and render vendors to vendor's page

        modified:   README.md
        new file:   app/core/migrations/0023_auto_20230111_0009.py
        modified:   app/core/models.py
        modified:   app/core/views.py
        modified:   templates/app/core/vendor_list.html

        Activities:

        1. Modified the vendor field in Product model by adding 
           relatad_name='vendor_product', that is like product-by vendor
        2. Run migration to make change in the Product's table field.
        3. In vendor_list_view function add logic to get all vendors
        4. Load the instances to the the vendor pade.

        NEXT: ...?


#### 15.4 Vendor detail - Part 1: Static

        modified:   README.md
        modified:   app/core/urls.py
        modified:   app/core/views.py
        new file:   templates/app/core/vendor_detail.html
        modified:   templates/app/core/vendor_list.html

        Aktivities:

        1. Define url path
        2. Defeine vendor_detail_view
        3. Create a new file: vendor_detail.html
        4. Adding html template to vendor_detail page
        5. Add dynamic links in vendor_list page to link vendor_detail page

        NEXT: Vendor detail - Part 2: Dynamic


#### 15.5 Vendor detail - Part 2: Dynamic

        modified:   README.md
        new file:   app/core/migrations/0024_vendor_cover_image.py
        modified:   app/core/models.py
        modified:   app/core/views.py
        new file:   media/user_directory_path/vendor-1.png
        ...
        new file:   media/user_directory_path/vendor-header-bg.png
        modified:   templates/app/core/vendor_detail.html

        Aktivities:

        1. Change Vendor model by adding a new field:
                cover_image = models.ImageField(upload_to='user_directory_path', default='vendor.jpg')
        2. Run and apply migrations
        3. Working on vendor's banner
        4. Showing we found xx item/s
           <p>We found <strong class="text-brand">{{products.count}}</strong> 
           item{{products.count|pluralize}} for you!</p>
        5. Showing product by vendor:
           {% for product in products %}
                -{{product.get_percentage|floatformat:0}}%
                {{product.category.title}}
                {{product.title|truncatechars:15}}
                {{product.description|truncatechars:75}}
                ${{product.price}}
                ${{product.old_price}}
           {% endfor %}
        6. Showing product by category:
           {% for cat in categories %}
                <li>
                <a href="shop-grid-right.html"> 
                    <img src="{{cat.image.url}}" alt="" />
                    {{cat.title}}
                </a>
                <span class="count">{{cat.category.all.count}}</span>
                </li>
            {% endfor %}


#### 15.6 Vendor lists - Add links in navbar

        modified:   README.md
        modified:   templates/partials/nav-bar.html

        Aktivities:

        1. Add links to navbar


## 16. Product detail


#### 16.1 Product detail - Urls, Views, Template

        Aktivities:

        1. Modified
        modified:   README.md

        2. Configure product-detail path
        modified:   app/core/urls.py

        path('product-detail/<any>/', views.product_detail_view, name='product_detail_view'),

        3. Configure the logic
        modified:   app/core/views.py

        # Product Detail
        def product_detail_view(request, any):
                product = Product.objects.get(pid=any)
                # product = get_object_or_404(Product, vid=vid) # this similar to the above
                # print(products)
        context = {'product':product}
        return render(request, 'app/core/product_detail.html', context)

        4. Modified
        modified:   app/core/admin.py

        5. Create a new page with block tags
        new file:   templates/app/core/product_detail.html


#### 16.2 Product detail - Add static template and load static files

        Aktivities:

        1. Modified
        modified:   README.md

        2. Add html template and load static files
        modified:   templates/app/core/product_detail.

        {% extends 'base.html' %}
        {% load static %}

        {% block content %}
        
        <main class="main">
        ...
        </main>
        {% endblock content %}


#### 16.3 Product detail - Loding prod_image in slider section

        Aktivities:

        1. Modified
        modified:   README.md

        2. Not sure what has changed
        modified:   app/core/views.py

        3. Rendering prod_image
        modified:   templates/app/core/product_detail.html

        <figure class="border-radius-10">
            <img src="{{product.prod_image.url}}" alt="product image" />
        </figure>


#### 16.4 Product detail - Loading product image and thumbnails

        Aktivities:

        1. Modified
        modified:   README.md

        2. Modified fields of ProductImage model
           before: image
           now   : thumbnail

           before: no related_name
           now   : related_name='related_products',
        modified:   app/core/models.py

        class ProductImage(models.Model):
                thumbnail = models.ImageField(upload_to='product-images/thumbnails/', default='product.jpg')
                product = models.ForeignKey(Product, related_name='related_products', on_delete=models.SET_NULL, null=True)
                created = models.DateTimeField(auto_now_add=True)
                updated = models.DateTimeField(null=True, blank=True)

        3. Run and apply migrations
        new file:   app/core/migrations/0025_alter_productimage_product.py
        new file:   app/core/migrations/0026_remove_productimage_image_productimage_thumbnail_and_more.py

        4. Modified views
        modified:   app/core/views.py

        5. Add some images from admin panel
        new file:   media/product-images/thumbnail-1.jpg
        ...
        new file:   media/product-images/thumbnails/thumbnail-9.jpg

        6. Load product, prod_image, thumbnails to detail page
        modified:   templates/app/core/product_detail.html

        <div class="detail-gallery">
            <span class="zoom-icon"><i class="fi-rs-search"></i></span>
            <!-- MAIN SLIDES -->
            <div class="product-image-slider">

                <!-- Get product image -->
                <figure class="border-radius-10">
                    <img src="{{product.prod_image.url}}" alt="product image" />
                </figure>
                <!-- Get product image -->

                <!-- Get thumbnail for product image -->
                {% for product in products %}
                <figure class="border-radius-10">
                    <img src="{{product.thumbnail.url}}" alt="product image" />
                </figure>
                {% endfor %}
                <!-- Get thumbnail for product image -->

            </div>

            <!-- THUMBNAILS -->
            <div class="slider-nav-thumbnails">

                <!-- Get product image as thumbnail -->
                <div><img src="{{product.prod_image.url}}" alt="product image" /></div>
                <!-- Get product image as thumbnail -->

                <!-- Get thumbnail -->
                {% for product in products %}
                <div><img src="{{product.thumbnail.url}}" alt="product image" /></div>
                {% endfor %}
                <!-- Get thumbnail -->

            </div>
        </div>

        NOTE:

        1. this: <!-- Get product image -->
           the same with this:<!-- Get product image as thumbnail -->

        2. this: <!-- Get thumbnail for product image -->
           the same with this: <!-- Get thumbnail -->


#### 16.5 Product detail - Load product information

        Aktivities:

        1. Modified
        modified:   README.md

        2. Modified get_percentage function in Product model
        modified:   app/core/models.py

        from: # prod_current_price = (self.price / self.old_price) * 100
        to  :   prod_current_price = (self.old_price - self.price) / (self.old_price) * 100
        
        3. Load product infomrmation
        modified:   templates/app/core/product_detail.html


#### 16.6 Product detail - Load product spesifications 

        Aktivities:

        1. Modified
        modified:   README.md

        2. Modified Product model
        modified:   app/core/models.py

        ...
        type = models.CharField(max_length=100, default='Organic', null=True, blank=True)
        stock = models.CharField(max_length=100, default='10', null=True, blank=True)
        life = models.CharField(max_length=100, default='100', null=True, blank=True)
        mfd = models.DateTimeField(auto_now_add=False , null=True, blank=True)

        3. Run and apply migration
        new file:   app/core/migrations/0027_product_life_product_mfd_product_stock_product_type_and_more.py
        
        4. Update products from admin
        new file:   media/user_directory_path/cat-1.png
        new file:   media/user_directory_path/product-13-2_BCyjwCF.jpg

        5. Load product specs
        modified:   templates/app/core/product_detail.html


#### 16.7 Product detail - Redering product description

        Aktivities:

        1. Modified
        modified:   README.md

        2. Modified Product model
        modified:   app/core/models.py

        3. Run and apply migrations
        new file:   app/core/migrations/0028_rename_stock_product_stock_status_alter_product_life.py
        new file:   app/core/migrations/0029_rename_stock_status_product_stock_count.py
        
        4. Add some images
        new file:   media/product-images/thumbnails/thumbnail-10_BXhTSwa.jpg
        ...
        new file:   media/product-images/thumbnails/thumbnail-9_zUsMKT4.jpg
        
        5. Add links
        modified:   templates/app/core/index.html
        
        6. Load full product description and truncate it as well 
        modified:   templates/app/core/product_detail.html


#### 16.8 Product detail - Redering user address

        Aktivities:

        1. Modified
        modified:   README.md

        2. Define address object
        modified:   app/core/context_processors.py

        3. Render it to product_detail with conditionals to show
           verified or unverified address
        modified:   templates/app/core/product_detail.html

        NOTE:

        1. It worked.
        2. But when logged out, it showed error


#### 16.9 Product detail - Return & Warranty

        Aktivities:

        1. Modified
        modified:   README.md

        2. Rendring return and warranty
        modified:   templates/app/core/product_detail.html

        2.1 Codes
        Return & Warranty

        <span>{{product.vendor.authentic_rating}} % Authentic </span>
        <span>{{product.vendor.days_return}} Days Return </span>
        {{product.vendor.warranty_period}} Months Warranty </span>

        
        2.2 Result
        Return & Warranty

         _100 % Authentic
         _100 Days Return
         _100 Months Warranty


#### 16.10 Product detail - Display Vendor information

        Aktivities:

        1. Modified
        modified:   README.md

        2. Displaying vendor information
        modified:   templates/app/core/product_detail.htm


#### 16.11 Product detail - Display and link product-by-category

        Aktivities:

        1. Modified
        modified:   README.md

        2. Load product-by-category and link them to catagory detail page
        modified:   templates/app/core/product_detail.html

        <div class="sidebar-widget widget-category-2 mb-30">

                <h5 class="section-title style-1 mb-30">Category</h5>

                <ul>
                    {% for category in categories %}
                    <li>
                        <a href="{% url 'core:product_by_category_list_view' category.cid %}"> 
                        <img src="{{category.image.url}}" alt="" />{{category.title}}
                        </a>
                        <span class="count">{{ category.category.count }}</span>
                    </li>
                    {% endfor %}
                </ul>
        </div>


#### 16.12 Product detail - Turned off the address

        Aktivities:

        1. Modified
        modified:   README.md

        2. Turned off the address in context_processors
        modified:   app/core/context_processors.py

        3. Referring to git repo no. 16.12
        modified:   templates/app/core/product_detail.html

        <span>
           {{address.address}} 
           <br>
           {% if address.status == True %}
           <span class="text-success">Verified address</span>
           {% else %}
           <span class="text-danger">Unverified address, refer to git repo no: 16.12</span>
           {% endif %}
        </span>

        NOTE:

        I turned it off because when I logged out from the admin panel
        (I was logged in as admin), it gives me error.
        To fix it, I must turn off the address in the context_processors.


## 17. Related Products


#### 17.1 Related Products - Geting instance of the related product by category in product_detail_view

        Aktivities:

        1. Modified
        modified:   README.md

        2. Get the product instance
        modified:   app/core/views.py

        rel_products = Product.objects.filter(category=product.category)
        print(rel_products)

        3. Result:
        <QuerySet [<Product: _Gorton’s Beer Battered Fish Fillets>]>


#### 17.2 Related Products - Rendering rel_products instance to product_detail page

        Aktivities:

        1. Modified
        modified:   README.md

        2. Create prod_image_hover field in Product model
        modified:   app/core/models.py

        3. Run and apply migrations
        new file:   app/core/migrations/0030_product_prod_image_hover_alter_product_status_choice.py

        4. Add images from admin panel
        new file:   media/user_directory_path/product-2-1_rRrH2k9.jpg
        new file:   media/user_directory_path/product-2-2.jpg

        5. Load rel_product to product_detail page
        modified:   templates/app/core/product_detail.html

        NOTE:

        1. It works
        2. But it shows the same product, NOT the related product

        NEXT: Showing the related product by using exclude


#### 17.3 Related Products - Showing product related category

        Aktivities:

        1. Modified
        modified:   README.md

        2. Re-write the logic in product_detail_view
        rel_products = Product.objects.filter(category=product.category).exclude(pid=any)[:4]

        3. Add product based-category (coffes) in admin

        NOTE:

        1. It works.
        2. There is no information in the product-detail page if there is no product-related category found

        NEXT: Add conditionals to show message if there is no product-related category found


#### 17.4 Related Products - Showing information if there no product-related category found

        Aktivities:

        1. Modified
        modified:   README.md

        2. Showing product that has no ralted category
        modified:   templates/app/core/product_detail.html

        <!-- related products -->
        <div class="row mt-60">
            <div class="col-12">
                <h2 class="section-title style-1 mb-30">Related products</h2>
            </div>
            {% if rel_products %}
            {% for rel_product in rel_products %}
            <div class="col-12">
            ...
            </div>
            {% endfor %}
            {% else %}
            <div class="col-12">
            <p>There is no related product found ...</p>
            </div>
            {% endif %}
         <!-- related products -->

        NOTE:

        1. It works.

        :)


#### 17.5 Related Products - Add link to show detail of the product-related category

        Aktivities:

        1. Modified
        modified:   README.md

        2. Add link
         modified:   templates/app/core/product_detail.html

         <a href="{% url 'core:product_detail_view' rel_product.pid %}" tabindex="0"></a>

        NOTE:

        1. It works.

        :)


#### 17.6 Related Products - Add link with the shop menu in nav-bar to show product-list page and add link to show product-detail page

        Aktivities:

        1. Modified
        modified:   README.md

        2. Add link to shop menu in nav-bar
        modified:   templates/partials/nav-bar.html

        <li>
                <a href="{% url 'core:product_list_view' %}">Shop <i class="fi-rs-angle-down"></i></a>
                <ul class="sub-menu">
                    <li><a href="{% url 'core:product_list_view' %}">Shop Grid – Right Sidebar</a></li>
                    <li><a href="{% url 'core:product_list_view' %}">Shop Grid – Left Sidebar</a></li>
                    <li><a href="{% url 'core:product_list_view' %}">Shop List – Right Sidebar</a></li>
                    <li><a href="{% url 'core:product_list_view' %}">Shop List – Left Sidebar</a></li>
                    <li><a href="{% url 'core:product_list_view' %}">Shop - Wide</a></li>
                    ...
                </ul>    
        <li>

        3. Add link to show product-detail page
        modified:   templates/app/core/product_list.html

        <div class="product-img product-img-zoom">
                <a href="{% url 'core:product_detail_view' product.pid %}">
                    <img class="default-img" src="{{product.prod_image.url}}" alt="" />
                    <img class="hover-img" src="{{product.prod_image.url}}" alt="" />
                </a>
        </div>

        NOTE:

        1. It works.

        :)


## 18. Working with Tags


#### 18.1 Working with Tags - Install django-taggit

        Aktivities:

        1. Modified
        modified:   README.md

        2. Installing django-taggit

        venv3932) λ pip install django-taggit


#### 18.2 Working with Tags - Register taggit to the IINSTALLED_APPS

        Aktivities:

        1. Modified
        modified:   README.md

        2. Register taggit to settings.py
        modified:   config/settings.py

        INSTALLED_APPS = [

            # New
            'jazzmin',

            'django.contrib.admin',
            ...

            # Third parties
            'taggit',


#### 18.3 Working with Tags - Adding tags field in the Product model

        Aktivities:

        1. Modified
        modified:   README.md

        2. Add tags field in Product model
        modified:   app/core/models.py

        from taggit.managers import TaggableManager

        tags = TaggableManager(blank=True)

        3. Run and apply migrations
        new file:   app/core/migrations/0031_product_tags.py


#### 18.4 Working with Tags - Load tags to product-detail page

        Aktivities:

        1. Modified
        modified:   README.md

        2. Load tags
        modified:   templates/app/core/product_detail.html

        <li class="mb-5">Tags: 
                {% for tag in product.tags.all %}
                <a href="#" rel="tag">{{tag.name}}</a>,
                {% endfor %}
        </li>


#### 18.5 Working with Tags - Create tag page: urls, views, template

        Aktivities:

        1. Modified
        modified:   README.md

        2. Create path
        modified:   app/core/urls.py

        path('products/tag/<slug:tag_slug>/', views.tag_list_view, name='tag_list_view')
        http://127.0.0.1:8000/products/tag/milk/

        3. Create tag_list_view in views
        modified:   app/core/views.py

        def tag_list_view(request, tag_slug=None):
        products = Product.objects.filter(status_choice='published').order_by('-id')

        tag = None 
        if tag_slug:
                 # If there is slug in the Tags model
                 # then, slug is equal to what ever we passed in the tag_slug
                 # Example: http://127.0.0.1:8000/products/tag/lotion
                tag = get_object_or_404(Tag, slug=tag_slug)
                # Get all products from Product table which have tags in it and put it in products variable
                products = products.filter(tags__in=[tag])

        context = {'products':products}

        return render(request, 'app/core/tag.html', context)

        4. Create tag page
        new file:   templates/app/core/tag.html

        5. Testing:
        http://127.0.0.1:8000/products/tag/milk/


        <!DOCTYPE html>
        <html>
        <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Tag page</title>
        </head>
        <body>
                <h1>Tags</h1>
        </body>
        </html>


#### 18.6 Working with Tags - Add template to tag page and render tags in it

        Aktivities:

        1. Modified
        modified:   README.md

        2. Modified tag_list_view
        modified:   app/core/views.py

        context = {
                'tag':tag,

        3. Copy product_by_category page for tag page and render tags here
        modified:   templates/app/core/tag.html

        <h1 class="mb-15">{{tag.name|capfirst}}</h1>
        <div class="breadcrumb">
                <a href="{% url 'core:index' %}" rel="nofollow"><i class="fi-rs-home mr-5"></i>Home</a>
                <span></span><a href="{% url 'core:tag_list_view' tag.slug %}">Tag</a> <span></span> {{tag.name|capfirst}}
        </div>


#### 18.7 Working with Tags - linked each tag in product-detail page to show product-by-tag

        Aktivities:

        1. Modified
        modified:   README.md

        2. Render tags here
        modified:   templates/app/core/tag.html

        3. Add link to tags to show product-detail by tag
        modified:   templates/app/core/product_detail.html


## 19. CKEDITOR


#### 19.1 Install CKEditor

        Aktivities:

        1. Modified
        modified:   README.md

        2. Install CKEditor
        https://django-ckeditor.readthedocs.io/en/latest/
        (venv3932) λ pip install django-ckeditor


#### 19.2 Setting up CDEditor basic features         

        Aktivities:

        1. Modified
        modified:   README.md

        2. Configure CKEditor
        modified:   config/settings.py

        INSTALLED_APPS = [

                    ...
                    'taggit',
                    'ckeditor',]

        # CKEditor path for media uploads
        CKEDITOR_UPLOAD_PATH = 'media/'

        3. Add path for CKEditor 
        modified:   config/urls.py

        # CKEditor
        path('ckeditor/', include('ckeditor_uploader.urls')),

        4. Use CKEditor in the model
        modified:   app/core/models.py

        from ckeditor_uploader.fields import RichTextUploadingField

        # Vendor model
        description = RichTextUploadingField(null=True, blank=True, default='I am a great vendor')

        # Product model
        description = RichTextUploadingField(null=True, blank=True, default='This is the product')
        specifications = RichTextUploadingField(null=True, blank=True)

        5. Run and apply migrations
        new file:   app/core/migrations/0032_alter_product_description_and_more.py

        6. Tesing: 
        > runserver 
        > go to admin 
        > open Products

        DONE :)

        NOTE:

        Basic features of the CKEditor shows up
