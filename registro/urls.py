from django.urls import path,include
from .views import SingupPageView


urlpatterns = [
    #compa la ruta accounts/ es obligatorio ese nombre

    path("accounts/",include("django.contrib.auth.urls")),
    path("singup",SingupPageView.as_view(),name="singup")

]
