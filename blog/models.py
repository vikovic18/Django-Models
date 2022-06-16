
from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 200)
    text = models.TextField()
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title