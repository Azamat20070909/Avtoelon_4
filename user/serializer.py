from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
	# password = serializers.CharField(max_length=100, write_only=True)	
	class Meta:
		model = User
		fields  = ['id', 'username', 'last_name','email', 'password', 'address', 'phone', 'image']
		write_only_fields = ('password',)
		read_only_fields = (['id'])
		extra_kwargs = {'password': {'write_only':True}}