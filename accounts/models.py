
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	picture = models.ImageField(max_length=100, null=True, blank=True)
	about = models.TextField(max_length=500, null=True, blank=True)
	twitter = models.CharField(max_length=100, null=True, blank=True)
	facebook = models.CharField(max_length=100, null=True, blank=True)

	class Meta:
		verbose_name_plural = "Profiles"

	def __str__(self):
		return self.user.username

