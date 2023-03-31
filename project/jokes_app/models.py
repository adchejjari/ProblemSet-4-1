from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"


class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.CharField(max_length=120, null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} : {self.content} : {self.date_published}"
    