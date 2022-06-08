from rest_framework import serializers
from booksapp.models import Books,Roles,Users

class BookSerializer(serializers.ModelSerializer):
  name = serializers.CharField(max_length=70, required=True)

  def create(self, validated_data):
    return Books.objects.create(
      name=validated_data.get('name')
    )

  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.save()
    return instance

  class Meta:
    model=Books
    fields=('id', 'name')

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model=Users
    fields=('id','Email','password','roles')


class RoleSerializer(serializers.ModelSerializer):
  class Meta:
    model=Roles
    fields=('id','role') 

