from rest_framework import serializers

from posts.models import Post, Category


class PostSerializer(serializers.HyperlinkedModelSerializer):
    def title_validator(value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError('Title shouldnt have numbers.')

    title = serializers.CharField(validators=[title_validator])

    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'created_on']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
