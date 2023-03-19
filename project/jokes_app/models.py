from django.db import models


class StoryPost(models.Model):
    author = models.CharField(max_length=20, null=False, blank=False)
    content = models.CharField(max_length=120, null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.author} : {self.content} : {self.date_published}"
    

