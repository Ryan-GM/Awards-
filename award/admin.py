from django.contrib import admin
from .models import Rating,Post,Profile

# Register your models here.
admin.site.register(Rating)
admin.site.register(Profile)
admin.site.register(Post)