from dataclasses import fields
from django.contrib import admin

from .models import Post
# Register your models here.


# class PostAdmin(admin.PostAdmin):

#     class Meta:
#         model = Post

#         fields = [
#             'title',
#             'slug',
#             'author',
#             'body',
#             'publish',
#             'created',
#             'updated',
#             'status',
#         ]


admin.site.register(Post)
