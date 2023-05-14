from django.contrib import admin
from page1.models import BookPublish,User,BookIssue,BookReview


# Register your models here.
admin.site.register(BookPublish)
admin.site.register(BookReview) 
admin.site.register(BookIssue)
admin.site.register(User) 
