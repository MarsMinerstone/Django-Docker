from rest_framework.viewsets import ReadOnlyModelViewSet
from services.models import Subsciprtion
from services.serializers import SubscriptionSerializer


class SubscriptionView(ReadOnlyModelViewSet):
	queryset = Subsciprtion.objects.all()
	serializer_class = SubscriptionSerializer
