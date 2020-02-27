from django.urls import path, include
from . import views
from .views import schema_view

from .views import InfoView

from django.conf.urls import url


app_name = 'info'

urlpatterns = [
    path('info/', InfoView.as_view()),
    path('', views.index, name='index'),
    url(r'^docs/', schema_view)
]
