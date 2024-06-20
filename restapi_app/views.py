
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
from.models import *
from.serializers import *

@api_view(['GET'])
def get(request):
    student_obj=student.objects.all()
    serializers_obj=studentserializers(student_obj,many=True)
    return Response({'status':200,"payload":"serializers_obj.data"})


@api_view(['POST'])
def post1(request):
    data=request.data
    print(data)
  
    return Response({'status':200,"payload":data})


#crud operation

@api_view(["GET"])
def read_student(request):
    student_obj=student.objects.all()
    serializer_obj=studentserializer(student_obj,many=True)
    return Response(serializer_obj.data)

@api_view(["POST"])
def create_student(request):
    student_obj=student.objects.all()
    serializer_obj=studentserializer(data=request.data)
    if serializer_obj.is_valid():
        serializer_obj.save()
        
    return Response(serializer_obj.data)


@api_view(['POST'])
def student_info(request,id):
    student_obj=student.objects.get(id=id)
    serializer_obj=studentserializer(instance=student_obj,data=request.data)
    if serializer_obj.is_valid():
        serializer_obj.save()       
    return Response(serializer_obj.data)

@api_view(["DELETE"])
def delete_student(request,id):
    student_obj=student.objects.get(id=id)     
    return Response("book is deleted")
