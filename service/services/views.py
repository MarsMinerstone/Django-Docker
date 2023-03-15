from rest_framework.viewsets import ReadOnlyModelViewSet
from services.models import Subsciprtion
from services.serializers import SubscriptionSerializer
from django.db.models import Prefetch, F, Sum
from clients.models import Client

from pprint import pprint


class SubscriptionView(ReadOnlyModelViewSet):
	queryset = Subsciprtion.objects.all().prefetch_related(
		'plan',
		# 'service',
		Prefetch('client', queryset=Client.objects.all().select_related('user').only(
			'company_name',
			'user__email'))
	).annotate(price=F('service__full_price') - 
		F('service__full_price') * F('plan__discount_percent') / 100.00) # annotate

	serializer_class = SubscriptionSerializer

	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		response = super().list(request, *args, **kwargs)

		# response_data = {'result': response.data} 
		response.data['total_amount'] = queryset.aggregate(total=Sum('price')).get('total')
		# response.data = response_data

		return response
