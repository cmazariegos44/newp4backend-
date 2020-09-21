from .models import Task, Reminder
from rest_framework import serializers



class ReminderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reminder
        fields = ['title', 'created', 'id']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    reminder = ReminderSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Task
        fields = ['title', 'complete', 'created', 'id', 'reminder']
        