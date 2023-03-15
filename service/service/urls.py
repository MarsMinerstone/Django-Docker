from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from services.views import SubscriptionView

router = routers.DefaultRouter()
router.register(r'subscriptions', SubscriptionView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
    # path('docs/', include('rest_framework_docs.urls')),
]


