# untuk mendefinisikan url yang kita buat

from django.urls import path

from . import views #mengambil semua function yang ada di file views

urlpatterns = [
    path('', views.get_semua_user, name="get_semua_user"),
    path('<int:id>', views.get_user_by_id, name="get_user_by_id"),
    path('create', views.create_user, name="create_user"), # tidak perlu token
    path('<int:id>/update', views.update_user, name="update_user"),
    path('login', views.login, name="login"),
    path('<int:id>/delete', views.delete_user_by_id, name="delete_user_by_id")
]