from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 20)
    content = models.TextField()
    writer = models.CharField(max_length = 20)
    createdAt = models.DateTimeField(auto_now_add = True)
    # 과제
    email = models.CharField(max_length = 30)
    comment = models.TextField()


    def __str__(self):
        return self.title