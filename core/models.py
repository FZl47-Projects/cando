from django.db import models
from core.utils import get_time, get_timesince_persian, random_str


def upload_file_src(instance, path):
    frmt = str(path).split('.')[-1]
    tm = get_time('%Y-%m-%d')
    return f'files/{tm}/{random_str()}.{frmt}'


def upload_image_src(instance, path):
    frmt = str(path).split('.')[-1]
    tm = get_time('%Y-%m-%d')
    return f'images/{tm}/{random_str()}.{frmt}'


class BaseModelManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super(BaseModelManager, self).get_queryset().filter(_is_deleted=False)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    _is_deleted = models.BooleanField(default=False)

    objects = BaseModelManager()

    class Meta:
        abstract = True

    def get_created_at(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')

    def get_created_at_timepast(self):
        return get_timesince_persian(self.created_at)


class File(models.Model):
    file = models.FileField(upload_to=upload_file_src, max_length=400)

    class Meta:
        ordering = '-id',

    def __str__(self):
        return f'#{self.id} File'


class Image(models.Model):
    image = models.ImageField(upload_to=upload_image_src, max_length=400)

    class Meta:
        ordering = '-id',

    def __str__(self):
        return f'#{self.id} Image'

    def get_image_url(self):
        try:
            return self.image.url
        except:
            # default image
            # TODO: should be completed
            return ''
