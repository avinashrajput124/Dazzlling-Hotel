from rest_framework.decorators import api_view
from rest_framework.response import Response
from ello.models import Add_Hotal,promotions,exclusive_partners,offer_for_you,Holiday_packages,youtube_video,whats_new
from ello.serializers import Add_hotelSerializer,UserSerializer,all_promotionsSerializer,all_exclusivepartnersSerializer,all_offer_for_youSerializer,all_holiday_packagesSerializer,all_youtube_videoSerializer,all_whats_newSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import logout
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

#---------------------------------------------  user apii----------------------------

@api_view(['POST'])
@permission_classes([AllowAny])
def registeruser(request):
    if request.method=="POST":
        serializer=UserSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            newuser=serializer.save()
            data['Message']="Sucessfully Created user"
            data['email']=newuser.email
            data['username']=newuser.username
            data['phone']=newuser.phone
            token=Token.objects.get(user=newuser).key
            data['token']=token
        else:
            data=serializer.errors
        return Response(data)



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def User_logout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response('User Logged out successfully')




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    if request.method=="GET":
        content = {
            'id': str(request.user.id),
            'user': str(request.user),
            'email':str(request.user.email),
            'Password':str(request.user.password),
            'phone':str(request.user.phone),
            'Gender':str(request.user.gender),
        }
        return Response(content)
    


# -------------------------------------all hotl data api-----------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hotel(request):
    data=Add_Hotal.objects.all()
    serializer=Add_hotelSerializer(data,many=True)
    print(serializer)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_promotions(request):
    data=promotions.objects.all()
    serializer=all_promotionsSerializer(data,many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_exclusive_partners(request):
    data=exclusive_partners.objects.all()
    serializer=all_exclusivepartnersSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_offer_for_you(request):
    data=offer_for_you.objects.all()
    serializer=all_offer_for_youSerializer(data,many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_holidays_packages(request):
    data=Holiday_packages.objects.all()
    serializer=all_holiday_packagesSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_youtube_video(request):
    data=youtube_video.objects.all()
    serializer=all_youtube_videoSerializer(data,many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_whats_new(request):
    data=whats_new.objects.all()
    serializer=all_whats_newSerializer(data,many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def filter_hotel(request, format=None):
#     # queryset = Add_Hotal.objects.all()
#     filter_backends = [SearchFilter]
#     data=Add_Hotal.objects.filter(Hotal_Name=filter_backends).all()
#     serialiizer = Add_hotelSerializer(data,many=True)
#     return Response(serialiizer.data)


class hotelListView(ListAPIView):
    permission_classes=[(IsAuthenticated)]
    queryset = Add_Hotal.objects.all()
    serializer_class = Add_hotelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['Hotal_Name']