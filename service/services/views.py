from rest_framework.viewsets import ReadOnlyModelViewSet
from services.models import Subsciprtion
from services.serializers import SubscriptionSerializer
from django.db.models import Prefetch
from clients.models import Client


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subsciprtion.objects.all().prefetch_related(
    	'plan',
        Prefetch('client', queryset=Client.objects.all().select_related('user').only(
            'company_name',
            'user__email'))
    )
    serializer_class = SubscriptionSerializer
