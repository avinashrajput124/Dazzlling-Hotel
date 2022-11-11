from rest_framework import serializers
from ello.models import Add_Hotal,User,promotions,exclusive_partners,offer_for_you,Holiday_packages,youtube_video,whats_new
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    phone = serializers.CharField( required=True)
    gender = serializers.CharField( required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'phone','gender')

    def validate(self, match):
        if match['password'] != match['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return match

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            gender  =validated_data['gender']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


        
class Add_hotelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Add_Hotal
        fields='__all__'


class all_promotionsSerializer(serializers.ModelSerializer):
    class Meta:
        model= promotions
        fields='__all__'


class all_exclusivepartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model= exclusive_partners
        fields='__all__'

class all_offer_for_youSerializer(serializers.ModelSerializer):
    class Meta:
        model= offer_for_you
        fields='__all__'


class all_holiday_packagesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Holiday_packages
        fields='__all__'

class all_youtube_videoSerializer(serializers.ModelSerializer):
    class Meta:
        model= youtube_video
        fields='__all__'


class all_whats_newSerializer(serializers.ModelSerializer):
    class Meta:
        model= whats_new
        fields='__all__'


