from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import os
"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from Client_User import views as views
from client import views as client
from user import views as user

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path('admin/', admin.site.urls),
    path('appoint/<appointment>/',user.backtest,name="appointment"),
    path("login/", views.login,name="login"),
    path("appointmentView/", views.appointmentView, name="appointmentView"),
    path("appointmentCreate/", views.appointmentCreate,name ="appointmentCreate"),
    path("rateVet/<appointment_id>/", client.rateVet, name = "rateVet"),
    path("petView/",user.viewPets,name= "viewPets"),
    path("homeClient/<int:id_cliente>/",client.homeClient,name= "homeClient"),
    path("registerPet/<int:id_cliente>/",client.registerPet,name= "registerPet"),
    path("vetInformation/<int:id_cliente>/",client.vetInformation,name= "vetInformation"),
    path('save/',user.save,name='save'),
    path('appointmentOutside/',user.appointmentOutside,name='appointmentOutside'),
    path('appointmentInside/',user.appointmentInside,name='appointmentInside'),
    path('appointmentViewClient/<int:id_pet>',client.appointmentViewClient,name='appointmentViewClient'),
    path('clinicalUserView/',user.clinicalUserView,name= 'clinicalUserView' ),
    path('viewRate/<int:client_id>/',client.viewRate,name='viewRate'),
]

urlpatterns += static('/report/',document_root=os.path.join(BASE_DIR,'report'))
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
