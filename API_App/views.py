from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import *

# Create your views here.
from API_App.models import *


class TemaView(viewsets.ViewSet):
    def get(self, request, pk=None):
        model = Tema.objects.get(id=pk)
        serializers = TemaSerializer(model)
        return Response(serializers.data)

    def list(self, request):
        model = Tema.objects.all()
        serializers = TemaSerializer(model, many=True)
        return Response(serializers.data)

    def create(self, request):
        try:
            serializer = TemaSerializer(data=request.data, context={'request': request})
            serializer.is_valid()
            serializer.save()
            return Response({
                'error': False,
                'message': 'Success'
            })
        except:
            return Response({
                'error': True,
                'message': 'Error',
            })

    def update(self, request, pk=None):
        try:
            model = Tema.objects.get(id=pk)
            serializer = TemaSerializer(model, data=request.data, context={'request': request})
            serializer.is_valid()
            serializer.save()
            return Response({
                'error': False,
                'message': 'Success'
            })
        except:
            return Response({
                'error': True,
                'message': 'Error',
                'data': request.data
            })

    def delete(self, request, pk=None):
        model = Tema.objects.get(id=pk)
        model.delete()
        return Response({
            'error': False,
            'message': 'Delete'
        })


class Sorag_TypeView(viewsets.ViewSet):
    def get(self, request):
        model = Sorag_Type.objects.all()
        serializer = Sorag_TypeSerializer(model, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            serializer = Sorag_TypeSerializer(data=request.data, context={'request': request})
            serializer.is_valid()
            serializer.save()
            return Response({
                'error': False,
                'message': 'Success'
            })
        except:
            return Response({
                'error': False,
                'message': 'Error'
            })


class ResponsePagination(PageNumberPagination):
    page_query_param = 'p'
    page_size = 1
    page_size_query_param = 'page_size'


class SoragView(viewsets.ViewSet):
    def get(self, request, pk=None):
        model = Sorag.objects.get(id=pk)
        serializers = SoragSerializer(model)
        return Response(serializers.data)

    def list(self, request):
        model = Sorag.objects.all()
        serializer = SoragSerializerGet(model, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            serializer = SoragSerializer(data=request.data, context={'request': request})
            serializer.is_valid()
            serializer.save()
            return Response({
                'error': False,
                'message': 'Success'
            })
        except:
            return Response({
                'error': True,
                'message': 'Error Post'

            })

    def update(self, request, pk=None):
        try:
            model = Sorag.objects.get(id=pk)
            serializer = SoragSerializer(model, data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response({
                'error': False,
                'message': 'Success'
            })
        except:
            return Response({
                'error': True,
                'message': 'Error Post'
            })

    def delete(self, request, pk=None):
        model = Sorag.objects.get(id=pk)
        model.delete()
        return Response({
            'error': False
        })


class StartTest(viewsets.ViewSet):
    def create(self, request):
        serializers = StartTestSerializer(data=request.data,context={'request':request})
        serializers.is_valid()
        serializers.save()
        return Response({
            'error':False
        })



tema_list = TemaView.as_view({'get': 'list'})
tema_post = TemaView.as_view({'post': 'create'})
tema_put = TemaView.as_view({'put': 'update'})
tema_delete = TemaView.as_view({'delete': 'delete'})
