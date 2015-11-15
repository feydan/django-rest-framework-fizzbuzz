from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from fizzbuzz.models import FizzBuzz
from random import randint
import json

class FizzBuzzTests(APITestCase):
    def test_create_fizzbuzz(self):
        """
        Ensure we can create a new fizzbuzz object.
        """
        message = 'Random message: ' + str(randint(0,99999))
        response = self.client.post('/fizzbuzz/', json.dumps({'message': message}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        fizbuzzId = response.data['fizzbuzz_id']
        self.assertEqual(FizzBuzz.objects.get(pk=fizbuzzId).message, message)

    def test_list_fizzbuzz(self):
    	"""
        Ensure we can list fizzbuzz objects.
        """
        message = 'Random message: ' + str(randint(0,99999))
        fizzbuzz1 = FizzBuzz(message=message)
        fizzbuzz1.save()

        message = 'Random message: ' + str(randint(0,99999))
        fizzbuzz2 = FizzBuzz(message=message)
        fizzbuzz2.save();

        response = self.client.get('/fizzbuzz/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0].get('fizzbuzz_id'), fizzbuzz1.fizzbuzz_id)
        self.assertEqual(response.data[0].get('message'), fizzbuzz1.message)
        self.assertEqual(response.data[1].get('fizzbuzz_id'), fizzbuzz2.fizzbuzz_id)
        self.assertEqual(response.data[1].get('message'), fizzbuzz2.message)

    def test_get_fizzbuzz(self):
    	"""
        Ensure we can get a fizzbuzz object.
        """
    	message = 'Random message: ' + str(randint(0,99999))
        fizzbuzz1 = FizzBuzz(message=message)
        fizzbuzz1.save()

        response = self.client.get('/fizzbuzz/' + str(fizzbuzz1.fizzbuzz_id) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['fizzbuzz_id'], fizzbuzz1.fizzbuzz_id)
        self.assertEqual(response.data['message'], fizzbuzz1.message)

    def test_put_fizzbuzz(self):
        """
        Ensure we cannot update a fizzbuzz object.
        """
        response = self.client.put('/fizzbuzz/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_fizzbuzz(self):
        """
        Ensure we cannot delete a fizzbuzz object.
        """
        response = self.client.delete('/fizzbuzz/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)