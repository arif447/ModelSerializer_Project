from rest_framework import serializers
from api import models
""" ModelSerializer is a shortcut and automatically generate a serializer with correspond model field  
and provide create , update method
"""


class MovieSerializer(serializers.ModelSerializer):
    positions = serializers.SerializerMethodField() #add extra field in the model using modelserializer

    class Meta:
        model = models.Movie
        # if we want a subset of default field when using fields and exclude
        # fields = '__all__'
        # exclude = ['id']
        fields = ['id', 'title', 'description', 'release_date', 'rating', 'us_gross', 'worldwide_gross', 'positions']

        # extra_kwargs = {
        #     'title': {'read_only': True}
        # }

    def get_positions(self, obj):

      if obj.rating > 8:
        return 'Better'

      elif obj.rating < 7:
        return 'good'

    # custom field validation
    def validate_rating(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError('ratting will be between 1 and 10')
        return value

    # Object-level validation
    def validate(self, data):
        if data['us_gross'] > data['worldwide_gross']:
            raise serializers.ValidationError('worldwide_gross cannot be bigger than us_gross')
        return data

    # Functional validators
    # def is_rating(value):
    #     if value < 1:
    #         raise serializers.ValidationError('Value cannot be lower than 1.')
    #     elif value > 10:
    #         raise serializers.ValidationError('Value cannot be higher than 10')


"""user and userprofile serializer """


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        exclude = ['id']


class UserSerializer(serializers.ModelSerializer):
    # ami = UserProfileSerializer()
    # using source keyword
    active = serializers.BooleanField(source='is_active')  # Rename serializer output fields
    # bio = serializers.CharField(source='userprofile.bio') # here urerprofile is model name
    # birth_date = serializers.DateField(source='userprofile.birth_date')

    class Meta:
        model = models.User
        fields = ['id', 'username',  'email', 'is_staff', 'active']
    #
    # def create(self, validated_data):
    #     profile_user_data = validated_data.pop('ami')
    #     profile_user = UserProfileSerializer.create(UserProfileSerializer(), validated_data=profile_user_data)
    #     user = models.User.objects.create(
    #         profile_user=profile_user,
    #         username=validated_data.pop('username'),
    #         email=validated_data.pop('email'),
    #         is_staff=validated_data.pop('is_staff'),
    #         active=validated_data['active']
    #
    #     )
    #     return user


"""comment serializer"""


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    # author = UserSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = ['author', 'content']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author = UserSerializer.create(UserSerializer(),
                                       validated_data=author_data)
        comment = models.Comment.objects.create(
            author=author,
            content=validated_data.pop('content')
        )
        return comment


