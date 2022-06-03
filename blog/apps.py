from django.apps import AppConfig

#2. Add Blog app to settings

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
