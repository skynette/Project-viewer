from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

def slugifyy(text):
	text = text.replace(' ', "+")
	return text

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=50, null=True, blank=True)
	image = models.ImageField(upload_to='posts/%Y/%m/%d/', max_length=250, null=True, blank=True)
	document = models.FileField(upload_to='files/%Y/%m/%d', max_length=100, null=True, blank=True)
	snippet = models.CharField(max_length=500, null=True, blank=True)
	content = models.TextField(max_length=5000, null=True, blank=True)
	slug = models.CharField(max_length=50, null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Posts"

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugifyy(self.title)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('detail', slug=self.slug)
	
	def ImgUrl(self):
		return self.image.url
