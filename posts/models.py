from django.db import models
from django.contrib.auth.models import User

def slugifyy(text):
	text = text.replace(' ', "+")
	return text

class Post(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=50, null=True, blank=True)
	snippet = models.CharField(max_length=50, null=True, blank=True)
	content = models.TextField(max_length=5000, null=True, blank=True)
	slug = models.SlugField(max_length=50, null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Posts"

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugifyy(self.title)
		super().save(*args, **kwargs)

	def get_absolute_url():
		return reverse('detail', slug=slug)