from django.shortcuts import render
from .producer import kafka_producer
from rest_framework.views import APIView
from rest_framework.response import Response
from .consumer import kafka_consumer
from rest_framework import status


class ProduceData(APIView):

    def get(self,request):
        try:
            result = kafka_producer()
            return Response({'response_code': status.HTTP_200_OK,
                             'message': "data consumed",
                             'status_flag': True,
                             'status': "success",
                             'error_details': None})
        except Exception as e:
            return Response({'response_code': status.HTTP_400_BAD_REQUEST,
                             'message': "data consumed",
                             'status_flag': True,
                             'status': "success",
                             'error_details': e})


class ConsumeData(APIView):

    def get(self,request):
        try:
            result = kafka_consumer()
            return Response({'response_code': status.HTTP_200_OK,
                             'message': "data consumed",
                             'status_flag': True,
                             'status': "success",
                             'error_details': None})
        except Exception as e:
            return Response({'response_code': status.HTTP_400_BAD_REQUEST,
                             'message': "data consumed",
                             'status_flag': True,
                             'status': "success",
                             'error_details': e})