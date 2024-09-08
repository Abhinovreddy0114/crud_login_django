from django.urls import path
from vegi import views

urlpatterns = [
    path('receipes/', views.receipes, name='receipe'),
    path('delete_receipe/<id>/', views.delete_receipe, name='delete_receipe'),
    path('update_receipe/<id>/', views.update_receipe, name='update_receipe'),
    path('login/',views.login_page,name='login'),
    path('register/',views.register,name='register'),
]
