from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('blog_list/',views.blog_list,name='blog_list'),
    path('contact/',views.contact,name='contact'),
    path('product/',views.product,name='product'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('change-password/',views.change_password,name="change-password"),
    path('profile/',views.profile,name='profile'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('new_password/',views.new_password,name="new_password"),
    path('seller-index/',views.seller_index,name="seller-index"),
    path('seller-add-product',views.seller_add_product,name='seller-add-product'),
    path('seller-view-product',views.seller_view_product,name='seller-view-product'),
    path('seller-product-details/<int:pk>/',views.seller_product_details,name='seller-product-details'),
    path('seller-edit-product/<int:pk>/',views.seller_edit_product,name='seller-edit-product'),
    path('seller-delete-product/<int:pk>/',views.seller_delete_product,name='seller-delete-product'),
    path('product-details/<int:pk>/',views.product_details,name='product-details'),
    path('add-to-wishlist/<int:pk>',views.add_to_wishlist,name='add-to-wishlist'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('remove-from-wishlist/<int:pk>/',views.remove_from_wishlist,name='remove-from-wishlist'),
    path('add-to-cart/<int:pk>',views.add_to_cart,name='add-to-cart'),
    path('cart/',views.cart,name='cart'),
    path('remove-to-cart/<int:pk>/',views.remove_to_cart,name='remove-to-cart'),
    path('change-qty/',views.change_qty,name='change-qty'),
    path('pay/', views.initiate_payment, name='pay'),
    path('callback/',views.callback, name='callback'),
    path('myorder',views.myorder,name='myorder'),
     path('ajax/validate_email/',views.validate_email,name='validate_email'),
]

