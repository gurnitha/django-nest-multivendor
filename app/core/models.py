# app/core/models.py

# Django modules
from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe

# Locals
from app.userauth.models import User

# Define user directory path (each user will have its own directory)
def user_directory_path(instance, filename):
	return 'user_{0}/{1}.format(instance.user_id, filename)'


# Create your models here.

# =========================Catgegory, Product, ProductImage=====================
# =========================Catgegory, Product, ProductImage=====================
# =========================Catgegory, Product, ProductImage=====================


# Model: Category
class Category(models.Model):
	cid = ShortUUIDField(
					unique=True, length=10, max_length=20,
					prefix='cat', alphabet='abcdefgh12345')
	title = models.CharField(max_length=100, default='Food')
	image = models.ImageField(upload_to='category', default='category.jpg')

	class Meta:
		verbose_name_plural = 'Categories'

	def category_image(self):
		# Concatinate src="%s" and (self.image.url)
		# s in "%s" = src, src = self.image.url
		return mark_safe('<img src="%s" width="50" height="50" />' %(self.image.url))

	def __str__(self):
		return self.title 


# Model: Tag
class Tag(models.Model):
	pass 



# Model: Vendor
class Vendor(models.Model):
	ven_id = ShortUUIDField(
					unique=True, length=10, max_length=20,
					prefix='ven', alphabet='abcdefgh12345')
	ven_title = models.CharField(max_length=100, default='Nestify')
	ven_image = models.ImageField(upload_to='user_directory_path', default='vendor.jpg')
	ven_description = models.TextField(null=True, blank=True, default='I am a great vendor')
	ven_address = models.CharField(max_length=100, default='123 Main Street')
	ven_contact = models.CharField(max_length=100, default='+123 (456) 789')
	ven_chat_response_time = models.CharField(max_length=100, default='100')
	ven_shipping_on_time = models.CharField(max_length=100, default='100')
	ven_authentic_rating = models.CharField(max_length=100, default='100')
	ven_days_return = models.CharField(max_length=100, default='100')
	ven_warranty_period = models.CharField(max_length=100, default='100')
	ven_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

	class Meta:
		verbose_name_plural = 'Vendors'

	def vendor_image(self):
		# Concatinate src="%s" and (self.ven_image.url)
		# s in "%s" = src, src = self.ven_image.url
		return mark_safe('<img src="%s" width="50" height="50" />' %(self.ven_image.url))

	def __str__(self):
		return self.ven_title 



# Model: Product
class Product(models.Model):

	# Creating tupples for product choices, status
	PRODUCT_STATUS_CHOICES = (	
		('draft', 'Draft'),
		('disabled', 'Disabled'),
		('rejected', 'Rejected'),
		('in_review', 'In_review'),
		('published', 'Published'),
	) 

	pid = ShortUUIDField(
					unique=True, length=10, max_length=20,
					prefix='prod', alphabet='abcdefgh12345')
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=100, default='Fresh pear')
	image = models.ImageField(upload_to='user_directory_path', default='product.jpg')
	description = models.TextField(null=True, blank=True, default='This is the product')

	new_price = models.DecimalField(max_digits=100, decimal_places=2, default='1.99')
	old_price = models.DecimalField(max_digits=100, decimal_places=2, default='2.99')

	specifications = models.TextField(null=True, blank=True)
	tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

	pro_status_choice = models.CharField(choices=PRODUCT_STATUS_CHOICES, max_length=10, default='in_review')

	status = models.BooleanField(default=True)
	in_stock = models.BooleanField(default=True)
	featured = models.BooleanField(default=False)
	digital = models.BooleanField(default=False)

	sku = ShortUUIDField(unique=True, length=4, max_length=10, prefix='sku', alphabet='1234567890')

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Products'

	def product_image(self):
		# Concatinate src="%s" and (self.image.url)
		# s in "%s" = src, src = self.image.url
		return mark_safe('<img src="%s" width="50" height="50" />' %(self.image.url))

	def __str__(self):
		return self.title 

	# Define discounted price
	def get_procentage(self):
		prod_current_price = (self.prod_new_price / self.prod_old_price) * 100
		return prod_current_price



# Model: Product Image
class ProductImage(models.Model):
	prodim_image = models.ImageField(upload_to='product-images', default='product.jpg')
	prodim_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	prodim_created = models.DateTimeField(auto_now_add=True)
	prodim_updated = models.DateTimeField(null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Product images'



# # ===============================CartOrder, CartOrderItems========================
# # ===============================CartOrder, CartOrderItems========================
# # ===============================CartOrder, CartOrderItems========================


# Model: Cart Order
class CartOrder(models.Model):

	PRODUCT_PROCESS_STATUS_CHOICES = (
		('process', 'Processing'),
		('shipped', 'Shipped'),
		('delivered', 'Delivered'),
	) 

	cartor_user = models.ForeignKey(User, on_delete=models.CASCADE)
	cartor_price = models.DecimalField(max_digits=100, decimal_places=2, default='1.99')
	cartor_paid_status = models.BooleanField(default=False)
	cartor_date = models.DateTimeField(auto_now_add=True)
	cartor_process_status = models.CharField(choices=PRODUCT_PROCESS_STATUS_CHOICES, max_length=30, default='Processing') 

	class Meta:
		verbose_name_plural = 'Cart orders'	


# Model: Cart Order Item
class CartOrderItem(models.Model):
	cartoritem_order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
	cartoritem_invoice_number = models.CharField(max_length=200)
	cartoritem_status = models.CharField(max_length=200)
	cartoritem_item = models.CharField(max_length=200)
	cartoritem_image = models.CharField(max_length=200)
	cartoritem_quantity = models.ImageField(default=0)
	cartoritem_price = models.DecimalField(max_digits=100, decimal_places=2, default='1.99')	
	cartoritem_total_price = models.DecimalField(max_digits=100, decimal_places=2, default='1.99')

	class Meta:
		verbose_name_plural = 'Cart order items'	

	def cart_order_item_image(self):
		# Concatinate src="%s" and (self.cartoritem_image.url)
		# s in "%s" = src, src = self.cartoritem_image.url
		return mark_safe('<img src="/media/%s" width="50" height="50" />' %(self.cartoritem_image))



# # ===============================ProductReview, Wishlist and Address ========================
# # ===============================ProductReview, Wishlist and Address ========================
# # ===============================ProductReview, Wishlist and Address ========================


# Model: ProductReview
class ProductReview(models.Model):

	PRODUCT_RATING_CHOICES = (
		(1, '★☆☆☆☆'),
		(2, '★★☆☆☆'),
		(3, '★★★☆☆'),
		(4, '★★★★☆'),
		(5, '★★★★'),
	)

	prodrev_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	prodrev_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	prodrev_review = models.TextField()
	prodrev_rating = models.ImageField(choices=PRODUCT_RATING_CHOICES, default=None)
	prodrev_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'Product reviews'

	def product_image(self):
		# Concatinate src="%s" and (self.prod_image.url)
		# s in "%s" = src, src = self.prod_image.url
		return mark_safe('<img src="%s" width="50" height="50" />' %(self.prod_image.url))

	def __str__(self):
		return self.prodrev_product.prod_title 


	def get_rating(self):
		return self.prodrev_rating



# Model: Wishlist
class Wishlist(models.Model):
	wish_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	wish_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	wish_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'Wishlist'

	def __str__(self):
		return self.wish_product.prod_title 


# Model: Address
class Address(models.Model):
	addr_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	addr_address = models.CharField(max_length=100, null=True)
	addr_status = models.BooleanField(default=False)

	class Meta:
		verbose_name_plural = 'Addresses'

