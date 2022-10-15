from rest_framework.decorators import api_view
from rest_framework.response import Response
from ello.models import Add_Hotal
from ello.serializers import Add_hotelSerializer


# all hotel data api
@api_view(['GET'])
def hotel(request):
    data=Add_Hotal.objects.all()
    serializer=Add_hotelSerializer(data,many=True)
    print(serializer)
    return Response(serializer.data)


@api_view(['GET'])
def add_single_hotel(request,Hotal_id):
    data=Add_Hotal.objects.get(Hotal_id=Hotal_id)
    serializer=Add_hotelSerializer(data,many=False)
    return Response(serializer.data)


