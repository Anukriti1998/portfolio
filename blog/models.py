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

    def __str__(self): #so this is the automatic fnunction the server of admin site will look for naming the nuber of blog objects you made if not provided it default is Blog No.1, Blog No. 2
        return self.title

    def summary(self):
        return self.body[:100] + str('...')
    def formatTime(self):
        return self.pubdate.strftime('%b %e %Y')

#2. Add Blog app to settings

#3. Create migration
#python manage.py makemigrations

#4. Migrate
#python manage.py migrate

#5. Add to admin

#python manage.py runserver

