from rest_framework import serializers
from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="get_username")
    
    class Meta:
        model = Task
        fields = ('id','user','title', 'completed', 'created_date')
    
    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user # type: ignore
        return super().create(validated_data)
    
    
