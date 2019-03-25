"""
    abook_proj URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin

# wire up API using automatic URL routing
# additionally, we include login URLs for browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
]
