from .models import Schools, Classes, Messages

from rest_framework import serializers

class SchoolSerializer(serializers.ModelSerializer):
	class Meta:
		model = Schools
		fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classes
		fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Messages
		fields = '__all__'
