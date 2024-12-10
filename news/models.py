from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


#python manage.py makemigrations
#python manage.py migrate