from django.db import models

# Create your models here.

difficulty_choices = (
    ('آسان', 'آسان'),('متوسط', 'متوسط'),('سخت','سخت')
)

class Instruction(models.Model):
    title = models.CharField('title', max_length=200)
    description = models.TextField('Description', null=True, blank=True)
    img = models.ImageField('Image', null= True, blank= True)
    time = models.SmallIntegerField('Time', default=0)
    difficulty = models.CharField('Difficulty', choices= difficulty_choices, max_length=20, default='آسان')
    recipe = models.TextField('Recipe', null=True, blank=True)
    ingredients = models.TextField('Ingredients',null=True, blank=True)

class Article(models.Model):
    title = models.CharField('title', max_length=200)
    description = models.TextField('Description', null=True, blank=True)
    img = models.ImageField('Image', null= True, blank= True)