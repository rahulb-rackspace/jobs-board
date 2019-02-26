from rest_framework import serializers
from tracker.models import *


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        model = BaseModel
        fields = ('id', 'created_date', 'updated_date', 'active')


class JobHistorySerializer(BaseSerializer):
    class Meta:
        model = JobHistoryModel
        fields = ('job_id', 'status', 'start_time', 'end_time', 'comments')

