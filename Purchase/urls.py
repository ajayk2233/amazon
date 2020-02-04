from django.urls import path
from . import views
app_name = 'purchase'
urlpatterns = [
    path('show/', views.show,name='purchase.show'),
]
