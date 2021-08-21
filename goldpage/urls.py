from . import views
from django.urls import path
from .views import Index
urlpatterns=[
    path('gold/<filvalue>',views.product),
    path('home/',views.showhomepage,name='home'),
    path('gold/<filvalue1>/<filp>/<filw>/<filo>/',views.filtercategory),
    path('prod/<proname1>/',Index.showprodpage,name='productpage'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.logout,name="logout"),
    path('cart/',views.cart,name='cart'),
    path('confirmorder/',views.confirmorder,name="confirmorder"),
    path('wishlist/',views.wishlist,name="wishlist"),
    path('payment/',views.payment,name="payment"),
]