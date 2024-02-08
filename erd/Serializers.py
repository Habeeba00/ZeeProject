from rest_framework import serializers
from .models import patient,Escort,Medicine,Diseases,Document,Reminder

class pSerializers(serializers.ModelSerializer):
    class Meta:
        model= patient 
        fields="__all__"


class ESerializers(serializers.ModelSerializer):
    class Meta:
        model= Escort
        fields="__all__"


class DSerializers(serializers.ModelSerializer):
    class Meta:
        model= Diseases
        fields="__all__"


class MSerializers(serializers.ModelSerializer):
    class Meta:
        model= Medicine
        fields="__all__"


class DOSerializers(serializers.ModelSerializer):
    class Meta:
        model= Document
        fields="__all__"


class RSerializers(serializers.ModelSerializer):
    class Meta:
        model= Reminder
        fields="__all__"
