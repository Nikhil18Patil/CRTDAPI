from rest_framework import serializers
from .models import Register, Passkey , JobCode


class registerserializer(serializers.ModelSerializer):
    class Meta:
        model =Register
        fields=['uid', 'email', 'password', 'name' ,'father_name' ,'gender' ,'dob' , 'place_of_birth_city' ,'birth_state','contact_number','whatsapp_no','college_state','college_name','branch','passing_year','role' ,'permanent_address']


class Passkeyserializer(serializers.ModelSerializer):
    class Meta:
        model=Passkey
        fields=['uid' ,'passkey' , 'active']     


class JobcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCode
        fields = ('jobcode', 'active', 'campus')