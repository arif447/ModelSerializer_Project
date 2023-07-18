from django.contrib import admin
from .models import Movie, UserProfile, Comment

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'release_date', 'rating', 'us_gross', 'worldwide_gross']
    list_filter = ['release_date']

    class Meta:
        model = Movie

# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(UserProfile)
admin.site.register(Comment)
