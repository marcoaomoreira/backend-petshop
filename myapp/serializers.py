from rest_framework import serializers
from .models import Canil

class CanilSerializer(serializers.ModelSerializer):

    class Meta:

        model = Canil
        fields = '__all__'