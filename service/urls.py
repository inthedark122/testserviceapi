from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'providers', views.ProviderView)
router.register(r'provider_locations', views.ProviderLocationView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/v1/', include(router.urls))
]
