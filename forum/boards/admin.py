from django.contrib import admin
from boards.models import Thread, Post, Board

admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Thread)
