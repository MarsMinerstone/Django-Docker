from rest_framework import serializers
from services.models import Subsciprtion


class SubscriptionSerializer(serializers.ModelSerializer):
	client_name = serializers.CharField(source='client.company_name')
	email = serializers.CharField(source='client.user.email')

	class Meta:
		model = Subsciprtion
		fields = ('id', 'plan_id', 'client_name', 'email')