# app/core/views.py

# Django modules
# from math import prod 
# from stripe import Review 
from django.http import HttpResponse, JsonResponse 
from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Avg 

# Locals
from app.core.models import Product, Category, Vendor, ProductReview
from app.core.forms import ProductReviewForm
from taggit.models import Tag  

# Create your views here.

# Homepage
def index(request):
	# products = Product.objects.all().order_by('-id')
	products = Product.objects.filter(status_choice='published', featured=True)
	# print(products)
	context = {
		'products':products,
	}
	return render(request, 'app/core/index.html', context)


# Product List
def product_list_view(request):
	products = Product.objects.all()
	# print(products)
	context = {'products':products}
	return render(request, 'app/core/product_list.html', context)


# Product Detail
def product_detail_view(request, any):
	# Get product by pid
	product = Product.objects.get(pid=any)
	# product = get_object_or_404(Product, vid=vid) # this similar to the above
	# print(product)

	# # Related products - part 1
	# rel_products = Product.objects.filter(category=product.category)
	# print(rel_products)

	# Related products - part 2 
	rel_products = Product.objects.filter(category=product.category).exclude(pid=any)[:4]
	print(rel_products)

	# Get related products
	products = product.related_products.all()
	# print(products)

	# Getting all review of each product
	reviews = ProductReview.objects.filter(product=product).order_by('-created')

	# Getting average review
	average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

	# Product Review Form
	review_form = ProductReviewForm()

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

	context = {
		'product':product, 
		'products':products,
		'rel_products':rel_products,
		'reviews':reviews,
		'average_rating':average_rating,
		'review_form':review_form,
		'make_review':make_review
	}
	return render(request, 'app/core/product_detail.html', context)


# Category List
def category_list_view(request):
	categories = Category.objects.all()
	# print(categories)
	context = {'categories':categories}
	return render(request, 'app/core/category_list.html', context)


# Product By Category
def product_by_category_list_view(request, cat_id):
	category_based_id = Category.objects.get(cid=cat_id)
	products = Product.objects.filter(status_choice='published', category=category_based_id)
	context = {
		'category': category_based_id,
		'products': products,
	}
	return render(request, 'app/core/product_by_category_list.html', context)


# Vendor List
def vendor_list_view(request):
	vendors = Vendor.objects.all()
	# print(vendors)
	context = {
		'vendors':vendors
	}
	return render(request, 'app/core/vendor_list.html', context)


# Vendor Detail
def vendor_detail_view(request, vid):
	vendor = Vendor.objects.get(vid=vid)
	# print(vendor)
	products = Product.objects.filter(vendor=vendor, status_choice='published')
	# print(products)
	context = {
		'vendor':vendor,
		'products':products,
	}
	return render(request, 'app/core/vendor_detail.html', context)


def tag_list_view(request, tag_slug=None):
	products = Product.objects.filter(status_choice='published').order_by('-id')

	tag = None 
	if tag_slug:
		 # If there is slug in the Tags model
		 # then, slug is equal to what ever we passed in the tag_slug
		 # Example: http://127.0.0.1:8000/products/tag/lotion
		tag = get_object_or_404(Tag, slug=tag_slug)
		# print(tag)
		# Get all products from Product table which have tags in it and put it in products variable
		products = products.filter(tags__in=[tag])
		# print(products)

	context = {
		'tag':tag,
		'products':products,
	}

	return render(request, 'app/core/tag.html', context)



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