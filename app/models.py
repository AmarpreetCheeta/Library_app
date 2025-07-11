from django.db import models

# Create your models here.




class Book(models.Model):
    bookid = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    Average_Rating = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20)
    Isbn13 = models.CharField(max_length=20)
    Language_Code = models.CharField(max_length=255, blank=True)
    Num_page = models.PositiveIntegerField(null=True, blank=True)
    Ratings_Count = models.PositiveIntegerField(null=True, blank=True)
    Text_Reviews_Count = models.PositiveIntegerField(null=True, blank=True)
    Publication_Date = models.CharField(null=True, blank=True, max_length=220)
    publisher = models.CharField(max_length=255, blank=True)
    Actions = models.CharField(max_length=225, blank=True)

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    debt = models.CharField(blank=True, default=0, max_length=225)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    rent_fee = models.CharField(max_length=225)

    def __str__(self):
        return f"{self.member.name} - {self.book.title}"