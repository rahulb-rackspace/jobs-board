# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from models import *
from serializers import *

from django.shortcuts import render

# Create your views here.

class BaseApiView(APIView):

    def __init__(self):
        APIView.__init__(self)
        self.model_class = BaseModel
        self.serializer_class = BaseSerializer
        self.filter_list = []
        self.filter = {}

    def post(self, request):
        data = request.body
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        print serializer.errors
        return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

    def get(self, request):
        # Only accept first tenant, so no matter what user cannot see data of more than one tenant
        return_obj = self.model_class.objects.filter(**self.filter)
        serializer = self.serializer_class(return_obj, many=True)
        return Response(serializer.data)


class JobHistory(BaseApiView):
    def __init__(self):
        super(JobHistory, self).__init__()
        self.serializer_class = JobHistorySerializer
        self.model_class = JobHistoryModel

    def post(self, request):
        print "RAMPAPA"
        return super(JobHistory, self).post(request)

    def get(self, request):
        print "RAHUL"
        return super(JobHistory, self).get(request)


class JobHistorySync(BaseApiView):
    def __init__(self):
        super(JobHistorySync, self).__init__()
        self.serializer_class = JobHistorySerializer
        self.model_class = JobHistoryModel

    def post(self, request):
        return super(JobHistorySync, self).post(request)

    def get(self, request):
        return super(JobHistorySync, self).get(request)
