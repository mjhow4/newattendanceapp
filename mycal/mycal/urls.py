"""mycal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from attendance import views as attend_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', attend_views.registerPage, name='register'),
    path('user/', attend_views.userPage, name='user-page'),
    path('hub/', attend_views.hub, name='hub'),
    path('login/', attend_views.loginPage, name='login'),
    path('logout/', attend_views.loginPage, name='logout'),
    path('list/', attend_views.list_cases, name='list_cases'),
    path('lista/', attend_views.lista_cases, name='lista_cases'),
    path('listp/', attend_views.listp_cases, name='listp_cases'),
    path('submit/', attend_views.submit, name='submit'),
    path('contact/', attend_views.contact, name='contact'),
    # path('edita/', attend_views.edita_case, name='edita_case'),
    path('', attend_views.index, name='index'),
    path('signup/', attend_views.signup, name='signup'),
    path('attend/add/', attend_views.add_case, name='add_case'),
    path('attend/<int:pk>/delete/',
         attend_views.delete_case,
         name='delete_case'),
    path('attend/<int:pk>/edit/',
         attend_views.edit_case,
         name='edit_case'),
        path('attend/<int:pk>/edita/',
         attend_views.edita_case,
         name='edita_case'),
    
]
