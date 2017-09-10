from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from datetime import datetime

from .models import User, Schools, Classes, Messages
from .serializers import SchoolSerializer, ClassSerializer, MessageSerializer

# Create your views here.
@api_view(['GET'])
def auth(request):

	user_email = request.query_params.get('email')
	user_name = request.query_params.get('username')
	user_pw = request.query_params.get('password')

	em = user_email[user_email.index("@")+1:]
	school = Schools.objects.get(email_address_key__contains=em)

	if school is None:
		return Response(status=status.HTTP_417_EXPECTATION_FAILED)
	else:
		usr = User(username=user_name, password=user_pw, email=user_email, school=school)
		usr.save()

		serializer = SchoolSerializer(school)
		return Response(serializer.data, content_type="json")

@api_view(['GET'])
def getUserClasses(request):
	user_name = request.query_params.get('username')
	data = User.objects.get(username=user_name).classes
	
	serializer = ClassSerializer(data, many=True)

	return Response(serializer.data, content_type="json")

@api_view(['GET'])
def getAllClasses(request):
	school_name = request.query_params.get('school')

	classes = Classes.objects.filter(school__name=school_name)
	serializer = ClassSerializer(classes, many=True)

	return Response(serializer.data, content_type="json")

@api_view(['POST'])
def addClassForUser(request):
	username = request.data.get('user')
	class_id = int(request.data.get('class_id'))

	user = User.objects.get(username=username)

	class_to_add = Classes.objects.get(pk=class_id)

	user.classes.add(class_to_add)

	return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def deleteClassForUser(request):
	user_name = request.data.get('username')
	class_id = int(request.data.get('class_id'))

	user = User.objects.get(username="bob")
	user_class_to_delete = Classes.objects.get(pk=class_id)
	
	user.classes.remove(user_class_to_delete)

	return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def getMessages(request):
	class_name = request.query_params.get('class')
	section_numb = int(request.query_params.get('sectionNumb'))
	
	messages = Messages.objects.filter(class_related__class_name=class_name).filter(class_related__section_numb=section_numb).order_by('datetimeadded')

	serializer = MessageSerializer(messages, many=True)
	return Response(serializer.data, content_type="json")

@api_view(['POST'])
def addMessage(request):
	content = request.data.get('content')
	author = request.data.get('author')
	class_id = request.data.get('class_id')
	
	user = User.objects.get(username=author)
	class1 = Classes.objects.get(pk=class_id)
	msg = Messages(content=content, author=user, numLikes=0, datetimeadded=datetime.now(), class_related=class1)
	msg.save()

	return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def sendLike(request):
	msg_id = request.data.get('msg_id')
	likechange = int(request.data.get('like_change'))

	msg = Messages.objects.get(pk=msg_id)
	msg.numLikes = msg.numLikes + likechange
	msg.save()

	return Response(status=status.HTTP_200_OK)
