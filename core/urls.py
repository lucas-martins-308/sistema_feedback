from django.contrib import admin
from django.urls import path, include
from avaliacoes.views import home, logout_view  
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('disciplinas/', include('avaliacoes.urls')),
]
