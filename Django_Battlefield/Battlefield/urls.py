from django.conf.urls import url
from Battlefield.views import index, result

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^result', result, name='result'),
]