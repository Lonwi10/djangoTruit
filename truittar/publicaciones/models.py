from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

class Post(models.Model):
    Post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.Post_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Respuesta(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    Respuesta_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.Respuesta_text

class Usuario(models.Model):
	nick = models.CharField(max_length = 200)
	def __str__(self):
		return self.nick
