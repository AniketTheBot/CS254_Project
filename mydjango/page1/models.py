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
    date = models.DateField()

    def __str__(self) -> str:
        return self.booktitle

class BookReview(models.Model):
    name = models.CharField(max_length=30)
    booktitle = models.CharField(max_length=30)
    review = models.TextField()
    date = models.DateField()

    # def __str__(self) -> str:
    #     return self.username

class User(models.Model):
    username = models.CharField(unique=True)
    password = models.TextField()
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.username

class Author(models.Model):
    authorname = models.CharField(max_length=30)
    authorID = models.IntegerField()
    authoremail = models.EmailField()
    no_of_works = models.IntegerField()

    def __str__(self) -> str:
        return self.authorname