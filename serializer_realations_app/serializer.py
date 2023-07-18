from serializer_realations_app.models import Singer, Song
from rest_framework import serializers


class SingerSerializer(serializers.ModelSerializer):
    # singer_song = serializers.StringRelatedField(many=True, read_only=True)
    # singer_song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # singer_song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
    singer_song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='song_name')
    # singer_song = SongSerializer(many=True, read_only=True)  # nested serializer

    class Meta:
        model = Singer()
        fields = '__all__'
        # fields = ['id', 'name', 'gender', 'singer_song'] # here "singer_song" is related name
        # fields = ['id', 'name', 'gender', 'singer_song']
        # fields = ['id', 'name', 'gender', 'singer_song']


class SongSerializer(serializers.ModelSerializer):
    # nested serializer use korly  j serializer ta nested hobe oita upore hobe
    # r serializer er object hobe j objet diye relation kora hoyce oita
    # but without nested related name hobe object
    author = SingerSerializer()

    class Meta:
        model = Song()
        fields = ['author', 'song_name', 'duration', 'release', ]






