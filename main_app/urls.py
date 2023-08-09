from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dogs_index, name='index'),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
    path('dogs/create', views.DogCreate.as_view(), name='dogs_create'),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
    path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('dogs/<int:dog_id>/assoc_dogwalker/<int:dogwalker_id>/', views.assoc_dogwalker, name='assoc_dogwalker'),
    path('dogs/<int:dog_id>/unassoc_dogwalker/<int:dogwalker_id>/', views.unassoc_dogwalker, name='unassoc_dogwalker'),
    path('dogwalker/', views.DogWalkerList.as_view(), name='dogwalker_index'),
    path('dogwalker/<int:pk>/', views.DogWalkerDetail.as_view(), name='dogwalker_detail'),
    path('dogwalker/create', views.DogWalkerCreate.as_view(), name='dogwalker_create'),
    path('dogwalker/<int:pk>/update/', views.DogWalkerUpdate.as_view(), name='dogwalker_update'),
    path('dogwalker/<int:pk>/delete/', views.DogWalkerDelete.as_view(), name='dogwalker_delete'),
        
 ]