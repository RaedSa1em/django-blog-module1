from rest_framework import serializers
from ..models import User



class UserSerializer(serializers.ModelSerializer):


    #password = serializers.CharField(write_only=True, required=True)


    class Meta:
        model = User
        fields = [
            'user_name',
            'email',
            'first_name',
            'last_name',
            #'password',
        ]
        read_only_fields = ('id',)



    
    #def create(self, validated_data):
      
        #password = validated_data.pop('password')
        
       
        #user = User.objects.create(**validated_data)
        
        #user.set_password(password)
        #return user
