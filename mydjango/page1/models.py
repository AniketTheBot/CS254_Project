from django.db import models

class BookPublish(models.Model):
    booktitle = models.CharField(max_length=30)
    authorname = models.CharField(max_length=30)
    ISBN = models.IntegerField()
    publdate = models.DateField()
    desc = models.TextField()

    def __str__(self) -> str:
        return self.booktitle


class BookIssue(models.Model):
    booktitle = models.CharField(max_length=30)
    authorname = models.CharField(max_length=30)
    ISBN = models.IntegerField()

    def __str__(self) -> str:
        return self.booktitle

class BookReview(models.Model):
    username = models.CharField(max_length=30)
    booktitle = models.CharField(max_length=30)
    review = models.TextField()

    def __str__(self) -> str:
        return self.username

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.TextField()
    email = models.EmailField()

    def __str__(self) -> str:
        return self.username

