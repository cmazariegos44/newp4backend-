from .models import Task, Reminder
from rest_framework import serializers


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'complete', 'created', 'id']

class ReminderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reminder
        fields = ['title', 'created', 'id']
        