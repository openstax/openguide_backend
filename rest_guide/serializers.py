# from django.contrib.auth.models import User, Group 
# from rest_framework import serializers
# 

from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
     model = User
     fields = ('url', 'username', 'email', 'groups')
     
class GroupSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
     model = Group 
     fields = ('url', 'name')

class ThemeSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Theme
    fields = (
      'url',
      'title',
      'pub_date',
      'mod_date',
    )

class BookSerializer(serializers.HyperlinkedModelSerializer):
  theme = ThemeSerializer()
  class Meta:
    model = Book
    fields = (
      'url',
      'title',
      'pub_date',
      'mod_date',
      'theme',
    )
    
class BookPartSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = BookPart
    fields = (
      'section',
    )
    
class ElementAttributeTypeSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ElementAttributeType
    fields = (
      'label',
    )


class ElementAttributesSerializer(serializers.HyperlinkedModelSerializer):
  #attribute_type = ElementAttributeTypeSerializer()
  attribute_type = serializers.SlugRelatedField(
        read_only=True,
        slug_field='label'
    )
  class Meta:
    model = ElementAttributes
    fields = (
      'attribute_type',
      'data',
      )
   

class ElementSerializer(serializers.HyperlinkedModelSerializer):
  book = BookSerializer()
  #book_part = BookPartSerializer()
  book_part = serializers.SlugRelatedField(
        read_only=True,
        slug_field='section'
    )
  attributes = ElementAttributesSerializer(many=True, required=False)
  class Meta:
    model = Element 
    fields = (
      'url',
      'name',
      'book',
      'pub_date',
      'mod_date',
      'book_part',
      'attributes',
      )
    extra_kwargs = {
            #'url': {'view_name': 'accounts', 'lookup_field': 'account_name'}
            #'book_part': {'lookup_field': 'section'}
        }
    
    