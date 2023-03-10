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


#### 19.2 Setting up CKEditor basic features         

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


#### 19.3 Fixing issue address in context_processors

        Aktivities:

        1. Modified readme file
        modified:   README.md

        2. Fixing issue by using try block
        modified:   app/core/context_processors.py

        # Locals
        
        BEFORE:

        address = Address.objects.get(user=request.user)

        AFTER:

        try:
                address = Address.objects.get(user=request.user)
                # print(address)
        except:
                address = None


        DONE :)

        NOTE: It was an issue before using try block


#### 19.4 Adding more features to CKEditor basic features and some js and css in the product-detail page

        Aktivities:

        1. Modified readme file
        modified:   README.md

        2. Add more configurations
        modified:   config/settings.py

        3. Create new product from admin panel
        new file:   media/media/2023/01/31/blog-3.png
        new file:   media/media/2023/01/31/cat-13.png
        new file:   media/product-images/thumbnails/product-10-1.jpg
        new file:   media/product-images/thumbnails/product-2-1.jpg
        new file:   media/product-images/thumbnails/product-2-2.jpg
        new file:   media/uploads/2023/01/31/product-13-2.jpg
        new file:   media/user_directory_path/product-10-1_wL4SZLf.jpg
        new file:   media/user_directory_path/product-10-2.jpg

        4. Add some js and css, like this:
        modified:   templates/app/core/product_detail.html

        <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/10.0.3/styles/default.min.css">
        <script>hljs.initHighlighthingOnLoad();</script>
        <script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/10.0.3/highlight.min.js"></script>
        <script src="{% static 'assets/js/prism.js' %}"></script>
        <link rel="stylesheet" type="text/css" href="{% static 'assets/css/prism.css' %}">

        NOTE:

        1. The result is so amazing: it colored the html code, it just looks like in the text-editor
        2. But it has no html, copy button on the top-right corner

        EXAMPLE:

        1. Run the server
        2. Go to the broser with this link: 
        Open this link: http://127.0.0.1:8000/product-detail/prod24ghdcdea3/


## 20. PRODUCT REVIEWS


#### 20.1 Adding logic to product_detail_view

        Aktivities:

        1. Modified readme file
        modified:   README.md

        2. Modified ProductReview model
        modified:   app/core/models.py

        BEFORE:
        rating = models.ImageField(choices=PRODUCT_RATING_CHOICES, default=None) # ImageField

        AFTER:
        rating = models.IntegerField(choices=PRODUCT_RATING_CHOICES, default=None) # IntegerField

        3. Run and apply migrations
        new file:   app/core/migrations/0033_alter_productreview_rating.py
        new file:   app/core/migrations/0034_alter_productreview_rating.py

        4. Add logic to views
        modified:   app/core/views.py

        # Getting all review of each product
        reviews = ProductReview.objects.filter(product=product).order_by('-date')


#### 20.2 Rendering reviews in the Customer questions & answers

        Aktivities:

        1. Modified readme file
        modified:   README.md

        2. Getting all review of each product
        modified:   app/core/views.py

        reviews = ProductReview.objects.filter(product=product).order_by('-created')

        3. Redering reviews object
        modified:   templates/app/core/product_detail.html

        DONE :)

        NEXT: Product Rating


#### 20.3 Rendering product rating and sum reviews of a product

        Aktivities:

        1. Modified readme file
        modified:   README.md

        2. Getting average review
        modified:   app/core/views.py

        average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

        3. Renderig average_rating and sum of reviews
        modified:   templates/app/core/product_detail.html

        Reviews ({{reviews.count}})

        <h4 class="mb-30">Customer reviews</h4>
        <div class="d-flex mb-30">
        <!-- <div class="product-rate d-inline-block mr-15">
            <div class="product-rating" style="width: 90%"></div>
        </div> -->
        <h6>{{average_rating.rating|floatformat:1}} out of 5.0</h6> <<------------
        </div

        DONE :)

        NOTE:

        1. Showing number of average rating, not the star  


#### 20.4 Adding product reviews with ajax jquery

        Aktivities:

        1. Modified readme file
        modified:   README.md

        2. Create ProductReviewForm
        new file:   app/core/forms.py

        # app/core/forms.py

        # Import django modules
        from django import forms
        from stripe import Review

        # Import from locals
        from app.core.models import ProductReview


        class ProductReviewForm(forms.ModelForm):
                review = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Write review"}))

                class Meta:
                        model = ProductReview
                        fields = ['review', 'rating']

        3. Create url                
        modified:   app/core/urls.py

        # Add review
        path('ajax-add-review/<int:pid>/', views.ajax_add_review, name='ajax_add_review'),

        4. Create
        modified:   app/core/views.py

        # app/core/views.py

        # Django modules
        ...
        from django.http import HttpResponse, JsonResponse 
        ...
        from app.core.forms import ProductReviewForm

        # Product Detail
        def product_detail_view(request, any):
                ...

                # Product Review Form
                review_form = ProductReviewForm()

                context = {
                        ...
                        'review_form':review_form
                }


        # Ajax User Review
        '''Reviewing a product using a parameter of its own id (pid)'''
        def ajax_add_review(request, pid):
            
            '''get aproduct by its id (pid)'''
            product = Product.objects.get(pk=pid)
            
            '''get the user who wants to review that product'''
            user = request.user

            '''
            Create review: get things that passes by the user from the review form
            '''
            review = ProductReview.objects.create(
                # get the user, product, review and rating
                # you cat also get the date, but we will use js to do that
                user=user,
                product=product,
                review=request.POST['review'],
                rating=request.POST['rating'],
            )

            # Put in the context as variable
            context = {
                'user':user.username,
                'review':request.POST['review'],
                'rating':request.POST['rating'],
            }

            # Create avarage rating review
            average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

            # Js for the reating
            return JsonResponse(
                # It should be true, bc use write something in the form
                {
                    'bool':True,
                    'context':context,
                    'average_rating':average_rating,
                }
            )

        5. Render form instance    
        modified:   templates/app/core/product_detail.html

         <!--comment form-->
        <div class="comment-form">
            <h4 class="mb-15">Add a review</h4>
            <!-- <div class="product-rate d-inline-block mb-30"></div> -->
            <strong class="text-success" id="review-res"></strong>
            <div class="row">
                <div class="col-lg-8 col-md-12">
                    <form 
                        class="form-contact comment_form" 
                        action="{% url 'core:ajax_add_review' product.id %}" 
                        id="commentForm"
                        method="post">
                        {% csrf_token %}
                        <div class="row">
                            <div class="col-12">
                                <div class="form-group">
                                    {{review_form.review}}
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-group">
                                    {{review_form.rating}}
                                </div>
                            </div>
                        </div>
                        <div class="form-group">
                            <button type="submit" class="button button-contactForm">Submit Review</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>

        6. Create ajax jquery script
        new     :   static/assets/js/custom.js

        console.log("working fine");

        $("#commentForm").submit(function(e){

                // prevent the browser from refreshing
                e.preventDefault();

                // Using ajax
                $.ajax({

                        // serialize data comming from the form
                        data: $(this).serialize(),

                        // get the form attribute (method)
                        method: $(this).attr("method"),

                        // get the url (action) attribute from
                        url: $(this).attr("action"),

                        // define data type
                        dataType: "json",

                        // Console log
                        success: function(res){
                                console.log("Comment succssefully saved to database ...");

                                if(res.bool == true){
                                        $("#review-res").html("Review added succssefully ...");
                                }
                        }

                        })
        })

        7. Load custom.js
        modified:   templates/base.html

        <script src="{% static 'assets/js/custom.js' %}"></script> 

        8. Modified ProductReviewAdmin   
        modified:   app/core/admin.py

        class ProductReviewAdmin(admin.ModelAdmin):
        list_display = ['user', 'product',
                        'review', 'rating']


        8. Testing

        NOTE:

        1. Review added to db
        2. But to see the review in the product-detail page, the page MUST be refresh


#### 20.5 Adding product reviews with ajax jquery - hiding the form after adding review

        now when that's done the next thing I
        will do is go ahead and and hide this
        review button right because we don't
        want to show this review button again
        because they added a review.

        and in order
        to do that we could just look for the
        reviewers in or rather instead of hiding
        the button we can even hide the form all
        at once right.

        so instead of hiding
        hiding the only the button and the
        button alone we just go ahead and hide
        the form because that's going to be way
        better.


        1. Modified readme file
        modified:   README.md

        2. Adding class
        modified:   templates/app/core/product_detail.html

        h4 class="mb-15 hide-add-review">Add a review</h4>

        <form 
                class="form-contact comment_form hide-comment-form" 

        3. Modified custom.js

        $(".hide-comment-form").hide()
        $(".hide-add-review").hide()

        DONE :)


#### 20.6 Adding product reviews with ajax jquery - append the user review using ajax-jquery

        Aktivities:

        1. Modified readme file
        modified:   README.md

        2. Append the use review 
        modified:   static/assets/js/custom.js

        console.log("working fine");

        $("#commentForm").submit(function(e){

                // prevent the browser from refreshing
                e.preventDefault();

                // Using ajax
                $.ajax({

                        // serialize data comming from the form
                        data: $(this).serialize(),

                        // get the form attribute (method)
                        method: $(this).attr("method"),

                        // get the url (action) attribute from
                        url: $(this).attr("action"),

                        // define data type
                        dataType: "json",

                        // Console log
                        success: function(res){
                                console.log("Comment succssefully saved to database ...");

                                if(res.bool == true){
                                        $("#review-res").html("Review added succssefully ...");
                                        $(".hide-comment-form").hide()
                                        $(".hide-add-review").hide()

                                        let _html = '<div class="single-comment justify-content-between d-flex mb-30">'
                                                _html += '<div class="user justify-content-between d-flex">'
                                                _html += '<div class="thumb text-center">'
                                                _html += '<img src="https://static.vecteezy.com/system/resources/thumbnails/009/734/564/small/default-avatar-profile-icon-of-social-media-user-vector.jpg" alt="" />'
                                                _html += '<a href="#" class="font-heading text-brand">'+ res.context.user +'</a>'
                                                _html += '</div>'

                                                _html += '<div class="desc">'
                                                _html += '<div class="d-flex justify-content-between mb-10">'
                                                _html += '<div class="d-flex align-items-center">'
                                                _html += '<span class="font-xs text-muted">{{review.created|date:"d F Y"}}</span>'
                                                _html += '</div>'

                                                for(let i = 1; i < res.context.rating; i++ ){
                                                        _html += '<i class="fas fa-star text-warning">'
                                                }

                                                _html += '</div>'
                                                _html += '<p class="mb-10">'+ res.context.review +'</p>'

                                                _html += '</div>'
                                                _html += '</div>'
                                                _html += '</div>'


                                                $(".comment-list").prepend(_html)

                                        
                                }
                        }
                })
        })


        DONE :)

        NOTE: 

        1. The append does not show the date in user review

        NEXT: Working with the date


#### 20.7 Adding product reviews with ajax jquery - Adding stars

        Aktivities:

        1. Modified readme file
        modified:   README.md

        2. Adding a cdn font-awesome css
        modified:   templates/base.html

        3. Modified custom.js


        NOTE: 

        1. It worked.
        2. Stars display after refreshing the browser.
        3. All review comes with 4 stars after refreshment.

        NEXT: Solving the stars, then the date


#### 20.8 Adding product reviews with ajax jquery - Solving star

        Aktivities:

        1. Modified readme file
        modified:   README.md

        2. Looping star in Customer questions & answers
        modified:   templates/app/core/product_detail.html

        ...
        <h4 class="mb-30">Customer questions & answers</h4>

        <!-- <div class="product-rate d-inline-block">
            <div class="product-rating" style="width: 100%"></div>
        </div> -->

        {% for star in review.rating|ljust:review.rating %}
        <div class=" d-inline-block">
            <i class="fa fa-star" style="color: #f3da35;"></i>
        </div>
        {% endfor %}

        3. Adding font-awesome
        modified:   templates/base.html

        <!-- FontAwesome -->
        <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/css/all.min.css">

        4. Modified custom.js
        console.log("working fine");

        $("#commentForm").submit(function(e){

                // prevent the browser from refreshing
                e.preventDefault();

                // Using ajax
                $.ajax({

                        // serialize data comming from the form
                        data: $(this).serialize(),

                        // get the form attribute (method)
                        method: $(this).attr("method"),

                        // get the url (action) attribute from
                        url: $(this).attr("action"),

                        // define data type
                        dataType: "json",

                        // Console log
                        success: function(res){
                                console.log("Comment succssefully saved to database ...");

                                if(res.bool == true){
                                        $("#review-res").html("Review added succssefully ...");
                                        $(".hide-comment-form").hide()
                                        $(".hide-add-review").hide()

                                        let _html = '<div class="single-comment justify-content-between d-flex mb-30">'
                                                _html += '<div class="user justify-content-between d-flex">'
                                                _html += '<div class="thumb text-center">'
                                                _html += '<img src="https://static.vecteezy.com/system/resources/thumbnails/009/734/564/small/default-avatar-profile-icon-of-social-media-user-vector.jpg" alt="" />'
                                                _html += '<a href="#" class="font-heading text-brand">'+ res.context.user +'</a>'
                                                _html += '</div>'

                                                _html += '<div class="desc">'
                                                _html += '<div class="d-flex justify-content-between mb-10">'
                                                _html += '<div class="d-flex align-items-center">'
                                                _html += '<span class="font-xs text-muted">{{review.created|date:"d F Y"}}</span>'
                                                _html += '</div>'

                                                for(let i = 1; i <= res.context.rating; i++ ){
                                _html += '<i class="fa fa-star" style="color: #f3da35;"></i>'
                                                }


                                                _html += '</div>'
                                                _html += '<p class="mb-10">'+ res.context.review +'</p>'

                                                _html += '</div>'
                                                _html += '</div>'
                                                _html += '</div>'


                                                $(".comment-list").prepend(_html)
                                }
                        }
                })
        })

        NOTE:

        1. It worked
        2. Date has not been fixed yet

        NEXT: Fixing date


#### 20.9 Adding product reviews with ajax jquery - Adding currentdate

        Aktivities:

        1. Modified readme file
        modified:   README.md

        2. Modified custom.js by adding currentitem

        console.log("working fine");

        // Defining name of the months
        const monthNames = [
                "January", "February", "March", "April", "May", "June", 
                "July", "August", "September", "October", "Novpember", "December" 
        ]

        $("#commentForm").submit(function(e){

                // prevent the browser from refreshing
                e.preventDefault();

                // Creating date-time
                let currentdate = new Date();
                let currenttime = currentdate.getDate() + " " + monthNames[currentdate.getUTCMonth()] + ", " + currentdate.getFullYear()

        ...

                                        _html += '<div class="desc">'
                                        _html += '<div class="d-flex justify-content-between mb-10">'
                                        _html += '<div class="d-flex align-items-center">'
                                        // _html += '<span class="font-xs text-muted">{{review.created|date:"d F Y"}}</span>'
                                        _html += '<span class="font-xs text-muted">' + currenttime + '</span>'
                                        _html += '</div>'


        NOTE:

        1. It worked.
        2. The same user still can comment again and again to a product

        NEXT: Let a user to make ONE comment only to a spesific product


#### 20.10 Adding product reviews with ajax jquery - Preventing a user to make more than one comment for a spesific product

        Aktivities:

        1. Modified readme file
        modified:   README.md

        2. Add logic to prevent user to make more than one time review
        modified:   app/core/views.py

        # Preventing a user to make review for a spesific product MORE THEN ONE TIME
        make_review = True 

        #1 Check if user is logged in
        if request.user.is_authenticated:
                #2 If user logged ini, count his review
                user_review_count = ProductReview.objects.filter(user=request.user, product=product).count()

                #3 If user have made a review ( > 0 or one), 
                #  then dont let him make another review
                if user_review_count > 0:
                        make_review = False

        3. Add the logic to the form: Add a review
        modified:   templates/app/core/product_detail.html

        {% if request.user.is_authenticated %}
        {% if make_review == True %}
            <div class="comment-form">
                <h4 class="mb-15 hide-add-review">Add a review</h4>
                <strong class="text-success" id="review-res"></strong>
                <div class="row">
                    <div class="col-lg-8 col-md-12">
                        <form 
                            class="form-contact comment_form hide-comment-form" 
                            action="{% url 'core:ajax_add_review' product.id %}" 
                            id="commentForm"
                            method="post">
                            {% csrf_token %}
                            <div class="row">
                                <div class="col-12">
                                    <div class="form-group">
                                        {{review_form.review}}
                                    </div>
                                </div>
                                <div class="col-12">
                                    <div class="form-group">
                                        {{review_form.rating}}
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <button type="submit" class="button button-contactForm">Submit Review</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        {% endif %}
        {% endif %}

        DONE :)
        