from django.contrib import admin
from django.urls import path
from paginaweb.views import home

urlpatterns = [
    #rota, view responsável, nome de referência
    #neste caso, a view vai ser a pagina inicial "path(''),"
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]