from django.contrib import admin
# Register your models here.
from .models import Post, Profile

admin.site.register(Post) # this allows our user posts accessible on the admin side     # And for this to show up it has got to be registered.
admin.site.register(Profile)