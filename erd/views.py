from .Serializers import pSerializers,ESerializers,RSerializers,DOSerializers,DSerializers,MSerializers
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import patient,Escort,Medicine,Diseases,Document,Reminder



class GetPatient(viewsets.ModelViewSet):
    queryset = patient.objects.all()
    serializer_class = pSerializers
    # def get_extra_actions(self):
    #     return []

class GetEscort(viewsets.ModelViewSet):
    queryset = Escort.objects.all()
    serializer_class = ESerializers

class GetReminder(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = RSerializers

class GetDocument(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DOSerializers

class GetMedicine(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MSerializers

class GetDiseases(viewsets.ModelViewSet):
    queryset =Diseases.objects.all()
    serializer_class = DSerializers



# @api_view(['GET'])
# def showmultiplemodels(request):
#     patientt=patient.objects.all()
#     Escortt=Escort.objects.all()
#     ppSerializers=pSerializers(patientt,many=True)
#     EESerializers=ESerializers(patientt,many=True)
#     Resultmodel=ppSerializers.data+EESerializers.data
#     return response(Resultmodel)

from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response
from.models import patient, Escort, Reminder, Diseases, Document, Medicine
from .Serializers import pSerializers,ESerializers,RSerializers,DOSerializers,DSerializers,MSerializers

class PatientList(generics.ListAPIView):
    queryset = patient.objects.all()
    serializer_class = pSerializers
    def get_extra_actions(self):
        return []

    @swagger_auto_schema(responses={
        200: pSerializers(many=True)
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class EscortList(generics.ListAPIView):
    queryset = Escort.objects.all()
    serializer_class = ESerializers

    @swagger_auto_schema(responses={
        200: ESerializers(many=True)
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ReminderList(generics.ListAPIView):
    queryset = Reminder.objects.all()
    serializer_class = RSerializers

    @swagger_auto_schema(responses={
        200: RSerializers(many=True)
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class DiseasesList(generics.ListAPIView):
    queryset = Diseases.objects.all()
    serializer_class = DSerializers

    @swagger_auto_schema(responses={
        200: DSerializers(many=True)
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class DocumentList(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DOSerializers

    @swagger_auto_schema(responses={
        200: DOSerializers(many=True)
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class MedicineList(generics.ListAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MSerializers

    @swagger_auto_schema(responses={
        200: MSerializers(many=True)
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
