from rest_framework import serializers
from fizzbuzz.models import FizzBuzz


class FizzBuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = FizzBuzz
        fields = ('fizzbuzz_id', 'useragent', 'creation_date', 'message')