from django.urls import path

from . import views

urlpatterns = [
    path('', views.image_list_create_view),
    path('<int:pk>/', views.image_detail_view),
    # path('<int:pk>/update/', views.image_update_view),
    # path('<int:pk>/delete/', views.image_destroy_view),
]