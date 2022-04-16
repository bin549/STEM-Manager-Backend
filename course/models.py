import uuid
from django.db import models
from users.models import Profile


class Genre(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '%s' % self.name


class Entity(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    cover_img = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, null=True, blank=True, on_delete=models.CASCADE)
    is_visible = models.BooleanField(default=False, null=True)
    serial_number = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return f'/course/{self.title}/'

    def get_image(self):
        if self.cover_img:
            return self.cover_img.url
        return ''

    def get_student_url(self):
        return f'/course_student/{self.id}/'
