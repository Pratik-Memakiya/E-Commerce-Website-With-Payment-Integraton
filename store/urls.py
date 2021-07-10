from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.Men_Product, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('Men_Product/', views.Men_Product, name="men"),
	path('Women_Product/', views.Women_Product, name="Women_Product"),
	path('Electronic_Gadgets/', views.Electronic_Gadgets, name="Electronic_Gadgets"),
	path('Shoes/', views.Shoes, name="Shoes"),
	path('Badminton_Product/', views.Badminton_Product, name="Badminton_Product"),


]