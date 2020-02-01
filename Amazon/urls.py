from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Sales/',include('Sales.urls')),
    path('Purchase/',include('Purchase.urls')),
]
