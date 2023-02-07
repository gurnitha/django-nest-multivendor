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