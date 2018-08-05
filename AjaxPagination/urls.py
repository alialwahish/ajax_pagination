
from django.conf.urls import url,include

urlpatterns = [
    url(r'^ajaxP',include('apps.ajaxP.urls')),
]
