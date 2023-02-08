from django.urls import path

from main.views import (AutobusCreate, AutobusDelete, AutobusList,
                        AutobusUpdate, LinijaCreate, LinijaDelete, LinijaList,
                        LinijaUpdate, StanicaCreate, StanicaDelete,
                        StanicaList, StanicaUpdate, VozacCreate, VozacDelete,
                        VozacList, VozacUpdate, index)

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", index, name="index"),
    path('vozaci/', VozacList.as_view(), name="vozaci"),
    path('autobusi/', AutobusList.as_view(), name="autobusi"),
    path('stanice/', StanicaList.as_view(), name="stanice"),
    path('linije/', LinijaList.as_view(), name="linije"),
    path('vozaci/create/', VozacCreate.as_view(), name="vozaci-create"),
    path('vozaci/<int:pk>/update/', VozacUpdate.as_view(), name="vozaci-update"),
    path('vozaci/<int:pk>/delete/', VozacDelete.as_view(), name="vozaci-delete"),
    path('autobusi/create/', AutobusCreate.as_view(), name="autobusi-create"),
    path('autobusi/<int:pk>/update/', AutobusUpdate.as_view(), name="autobusi-update"),
    path('autobusi/<int:pk>/delete/', AutobusDelete.as_view(), name="autobusi-delete"),
    path('stanice/create/', StanicaCreate.as_view(), name="stanice-create"),
    path('stanice/<str:pk>/update/', StanicaUpdate.as_view(), name="stanice-update"),
    path('stanice/<str:pk>/delete/', StanicaDelete.as_view(), name="stanice-delete"),
    path('linije/create/', LinijaCreate.as_view(), name="linije-create"),
    path('linije/<str:pk>/update/', LinijaUpdate.as_view(), name="linije-update"),
    path('linije/<str:pk>/delete/', LinijaDelete.as_view(), name="linije-delete"),
]
