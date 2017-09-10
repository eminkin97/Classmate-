from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

import logging
import random
from datetime import datetime
import json

from .models import User, Schools, Classes, Messages
from .serializers import SchoolSerializer, ClassSerializer, MessageSerializer

# Create your tests here.
class Tests(TestCase):
	def setUp(self):
		s1 = Schools(name="kent", email_address_key="kent.edu")
		s1.save()
		s2 = Schools(name="rutgers", email_address_key="rutgers.edu")
		s2.save()

		c1 = Classes(class_name="chem", professor="Barchi", section_numb=1, school=s1)
		c1.save()
		c2 = Classes(class_name="math", professor="Saks", section_numb=1, school=s1)
		c2.save()
		c3 = Classes(class_name="bio", professor="Murray", section_numb=5, school=s2)
		c3.save()

		u1 = User(username="eli", password="bla", email="eli.minkin@rutgers.edu", school=s2)
		u1.save()
		u2 = User(username="bob", password="bla", email="bob.bobson@kent.edu", school=s1)
		u2.save()
		u3 = User(username="kat", password="bla", email="kat.dickson@kent.edu", school=s1)
		u3.save()

		m1 = Messages(content="bla bla bla", author=u1, numLikes=0, datetimeadded=datetime.now(), class_related=c1)
		m1.save()
		m2 = Messages(content="hi whats up", author=u2, numLikes=0, datetimeadded=datetime.now(), class_related=c1)
		m2.save()
		m3 = Messages(content="Not much", author=u2, numLikes=0, datetimeadded=datetime.now(), class_related=c1)
		m3.save()

	def test_authentication(self):
		client = APIClient()

		response = self.client.get('/auth/', {'username': 'randy', 'password': 'lol', 'email': 'meow@kent.edu'})	
		
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data.get('name'), 'kent')

		response = self.client.get('/auth/', {'username': 'john', 'password': 'ehh', 'email': 'eli.minkin@rutgers.edu'})	
		
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data.get('name'), 'rutgers')

	def test_get_classes(self):
		client = APIClient()

		response = self.client.get('/classes/', {'school': 'kent'})

		data = Classes.objects.filter(section_numb=1)
		serializer=ClassSerializer(data, many=True)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)


	def test_add_class_user(self):
		client = APIClient()

		class_id_1 = Classes.objects.get(class_name="chem").pk
		class_id_2 = Classes.objects.get(class_name="math").pk

		response = self.client.post('/add_user_class/', {'user': 'bob', 'class_id': class_id_1})
		response1 = self.client.post('/add_user_class/', {'user': 'bob', 'class_id': class_id_2})

		data = User.objects.get(username="bob").classes.all()
		serializer = ClassSerializer(data, many=True)

		data1 = Classes.objects.filter(section_numb=1).order_by("class_name")
		serializer1 = ClassSerializer(data1, many=True)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response1.status_code, status.HTTP_200_OK)
		self.assertEqual(serializer.data, serializer1.data)


	def test_get_user_classes(self):
		client = APIClient()

		class_id_1 = Classes.objects.get(class_name="chem").pk
		class_id_2 = Classes.objects.get(class_name="math").pk

		response = self.client.post('/add_user_class/', {'user': 'bob', 'class_id': class_id_1})
		response1 = self.client.post('/add_user_class/', {'user': 'bob', 'class_id': class_id_2})

		data = User.objects.get(username="bob").classes.all()
		serializer = ClassSerializer(data, many=True)

		data1 = Classes.objects.filter(section_numb=1).order_by("class_name")
		serializer1 = ClassSerializer(data1, many=True)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response1.status_code, status.HTTP_200_OK)
		self.assertEqual(serializer.data, serializer1.data)

		response = self.client.get('/user_classes/', {'username': 'bob'})

		data = Classes.objects.filter(section_numb=1).order_by("class_name")
		serializer = ClassSerializer(data, many=True)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)


	def test_delete_class_user(self):
		client = APIClient()

		class_id_1 = Classes.objects.get(class_name="chem").pk
		class_id_2 = Classes.objects.get(class_name="math").pk

		response = self.client.post('/add_user_class/', {'user': 'bob', 'class_id': class_id_1})
		response1 = self.client.post('/add_user_class/', {'user': 'bob', 'class_id': class_id_2})

		data = User.objects.get(username="bob").classes.all()
		serializer = ClassSerializer(data, many=True)

		data1 = Classes.objects.filter(section_numb=1).order_by("class_name")
		serializer1 = ClassSerializer(data1, many=True)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response1.status_code, status.HTTP_200_OK)
		self.assertEqual(serializer.data, serializer1.data)

		response = self.client.post('/delete_user_class/', {'user': 'bob', 'class_id': class_id_2})

		data = User.objects.get(username="bob").classes
		serializer = ClassSerializer(data, many=True)

		data1 = Classes.objects.get(class_name="chem")
		serializer1 = ClassSerializer(data1)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(json.dumps(serializer.data[0]), json.dumps(serializer1.data))

	def test_get_messages(self):
		client = APIClient()
		logger = logging.getLogger('django')

		response = self.client.get('/messages/', {'class': 'chem', 'sectionNumb': 1})

		data = Messages.objects.filter(numLikes=0).order_by('datetimeadded')
		serializer=MessageSerializer(data, many=True)

		logger.warning(serializer.data)
		logger.warning(response.data)
		logger.info("hello")

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)

	def test_add_msg(self):
		client = APIClient()
		
		class1 = Classes.objects.get(class_name="chem")

		self.assertEqual(len(Messages.objects.filter(class_related__class_name="chem")), 3)

		response = self.client.post('/sendmsg/', {'content': 'lol that was funny', 'author': 'kat', 'class_id': class1.pk})

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(Messages.objects.filter(class_related__class_name="chem")), 4)

	def test_send_like(self):
		client = APIClient()

		random_idx = random.randint(0, Messages.objects.count() - 1)
		random_obj_id = Messages.objects.all()[random_idx].pk

		previousLikeStatus = Messages.objects.get(pk=random_obj_id).numLikes
		response = self.client.post('/like/', {'like_change': 1, 'msg_id': random_obj_id})

		currentLikeStatus = Messages.objects.get(pk=random_obj_id).numLikes

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(previousLikeStatus + 1, currentLikeStatus)

		random_idx = random.randint(0, Messages.objects.count() - 1)
		random_obj_id = Messages.objects.all()[random_idx].pk

		previousLikeStatus = Messages.objects.get(pk=random_obj_id).numLikes
		response = self.client.post('/like/', {'like_change': -1, 'msg_id': random_obj_id})

		currentLikeStatus = Messages.objects.get(pk=random_obj_id).numLikes

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(previousLikeStatus - 1, currentLikeStatus)

