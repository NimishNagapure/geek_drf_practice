from rest_framework import serializers
from .models import Student

# validators
def start_with_n(value):
    if value[0].lower() != 'n':
        raise serializers.ValidationError('Name Should start with N')


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100,validators=[start_with_n])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)

    def update(self,instance ,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)

        instance.save()
        return instance

    # Field level Validations 
    def validate_roll(self,value):
        if value >=200:
            raise serializers.ValidationError('Seat Full')
        return value

    # Object level Validations

    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'don' and ct.lower() != 'pune':
            raise serializers.ValidationError("City Must Be Pune !!!")
        return data