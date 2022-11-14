from django.db import models
# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=100)

  class Meta:
     ordering = ['id']

  def __str__(self):
        return self.name

class File(models.Model):
  title = models.CharField(max_length=200)
  user_name = models.CharField(max_length=100)
  file = models.FileField()
  date = models.DateField(auto_now_add=True)
  like = models.IntegerField(default=0)
  categories = models.ManyToManyField('Category', related_name="files", blank=True)


  def __str__(self):
        return self.title

class Suscription(models.Model):
  user_name = models.CharField(max_length=200)
  email = models.EmailField(max_length=254)
