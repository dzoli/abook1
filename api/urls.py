"""
    App-level urlpatterns settings

"""
from django.conf.urls import url, include
from api import views
from rest_framework import routers
from .views import ApiObtainAuthToken

# Default router for browsable API
# At main page it shows 2 ViewSet's
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# wire up API using automatic URL routing
# additionally, we include login URLs for browsable API.
urlpatterns = [
    url(r'', include(router.urls)),

    # URLs login/logout for restframework API
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Obtaining token for authentification
    url(r'^authenticate/', ApiObtainAuthToken.as_view()),
]
