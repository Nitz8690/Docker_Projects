from django.urls import path

from . import views

urlpatterns = [
    path("shop/", views.index, name="ShopHome"),
    path("shop/basic", views.basic, name="ShopHome"),
    path("shop/about/", views.about, name="AboutUs"),
    path("shop/contact/", views.contact, name="ContactUs"),
    path("shop/tracker/", views.tracker, name="TrackingStatus"),
    path("shop/search/", views.search, name="Search"),
    path("shop/products/<int:myid>", views.productView, name="ProductView"),
    path("shop/checkout/", views.checkout, name="Checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path("shop/logout/", views.handleLogout, name='handleLogout'),
    path('shop/signup/', views.handleSignup, name='handleSignup'),
    path('shop/login', views.handleLogin, name='handleLogin'),

]
