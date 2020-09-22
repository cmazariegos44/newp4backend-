from .models import Task, Reminder
from rest_framework import serializers



class ReminderSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Reminder
        fields = ['title', 'created', 'id', 'owner']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    reminder = ReminderSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Task
        fields = ['title', 'complete', 'created', 'id', 'reminder', 'owner']
        