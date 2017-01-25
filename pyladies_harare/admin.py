from django.contrib import admin
from .models import Post, Contact, Page, Meetup, Category, Comment

admin.site.register(Page)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Meetup)
admin.site.register(Comment)
