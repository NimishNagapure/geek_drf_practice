from rest_framework import serializers
from .models import Student



class StudentSerializer(serializers.ModelSerializer):


    # # validators
    def start_with_n(value):
        if value[0].lower() != 'n':
            raise serializers.ValidationError('Name Should start with N')

    name = serializers.CharField(validators=[start_with_n])
    class Meta:
        model = Student
        fields =['id', 'name', 'roll','city']
        # read_only_fields =['name', 'roll']
        # extra_kwargs = {'name':{'read_only':True}}




    # Field level Validations 
    def validate_roll(self,value):
        if value >=200:
            raise serializers.ValidationError('Seat Full')
        return value


    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'don' and ct.lower() != 'pune':
            raise serializers.ValidationError("City Must Be Pune !!!")
        return data





# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)

#     def create(self,validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self,instance ,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.roll = validated_data.get('roll',instance.roll)
#         instance.city = validated_data.get('city',instance.city)

#         instance.save()
#         return instance