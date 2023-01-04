# app/core/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.core.models import (
	Product, Category, Vendor, CartOrder,
	CartOrderItem, ProductImage, ProductReview,
	Wishlist, Address)


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
	inlines = [ProductImageAdmin]
	list_display = ['prod_user', 'prod_title',
			'product_image', 'prod_new_price', 
			'prod_featured', 'prod_status']


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['cat_title', 'category_image']


class VendorAdmin(admin.ModelAdmin):
	list_display = ['ven_title', 'vendor_image']


class CartOrderAdmin(admin.ModelAdmin):
	list_display = ['cartor_user', 'cartor_price', 
			'cartor_paid_status', 'cartor_date', 
			'cartor_process_status' ]


class CartOrderItemAdmin(admin.ModelAdmin):
	list_display = ['cartoritem_order', 'cartoritem_invoice_number', 
			'cartoritem_item', 'cartoritem_image', 
			'cartoritem_quantity', 'cartoritem_price',
			'cartoritem_total_price', 'cartoritem_status']


class ProductReviewAdmin(admin.ModelAdmin):
	list_display = ['prodrev_user', 'prodrev_product',
			'prodrev_rating']


class WishlistAdmin(admin.ModelAdmin):
	list_display = ['wish_user', 'wish_product',
			'wish_created']


class AddressAdmin(admin.ModelAdmin):
	list_display = ['addr_user', 'addr_address',
			'addr_status']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItem, CartOrderItemAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Address, AddressAdmin)
