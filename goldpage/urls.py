from . import views
from django.urls import path
urlpatterns=[
    path('gold/<filvalue>',views.product),
    path('home/',views.showhomepage),
    path('gold/<filvalue1>/<filp>/<filw>/<filo>/',views.filtercategory),
    path('prod/<proname1>/',views.showprodpage),
]