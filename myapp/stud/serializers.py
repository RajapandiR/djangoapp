from rest_framework import serializers
from .models import Computer

class studApi(serializers.ModelSerializer):
	class Meta:
		model = Computer
		fields = '__all__'