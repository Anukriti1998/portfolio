from django.db import models

# Create your models here.

# 1. create a blog model
#title
#pubdate
#body
#image

class Blog(models.Model):
    title = models.CharField(max_length= 255)
    pubdate = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to= 'images/')

#2. Add Blog app to settings

#3. Create migration
#python manage.py makemigrations

#4. Migrate
#python manage.py migrate

#5. Add to admin

#python manage.py runserver

