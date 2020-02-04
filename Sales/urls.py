from django.urls import path
from . import views

urlpatterns = [
    path('ShowView/', views.ShowView,name='show'),
    path('AddView/', views.AddView.as_view(),name='add'),
    path('DetailsView/<int:id>', views.DetailsView,name='details'),
    path('EditView/<int:pk>',views.EditView.as_view(),name='edit'),
]