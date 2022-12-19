from django.urls import path
from main.views import *

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", index, name="index"),
    path('vozaci/', VozacList.as_view()),
    path('autobusi/', AutobusList.as_view()),
    path('stanice/', StanicaList.as_view()),
    path('linije/', LinijaList.as_view()),
]