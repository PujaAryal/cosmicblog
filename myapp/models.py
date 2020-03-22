from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Admin(Timestamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='admin')

    def save(self, *args, **kwargs):
        grp, created = Group.objects.get_or_create(name='admin')
        self.user.groups.add(grp)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Visitor(Timestamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='customer', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        grp, created = Group.objects.get_or_create(name='visitor')
        self.user.groups.add(grp)

        super().save(*args, **kwargs)

class Article(Timestamp):
	title=models.CharField(max_length=200)
	slug=models.SlugField(unique=True)
	content=models.TextField()
	date=models.DateTimeField(auto_now_add=True)
	author=models.ForeignKey(Visitor,on_delete=models.CASCADE)
	views=models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.title
	"""docstring for """

class Comment(Timestamp):
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    commenter=models.ForeignKey(Visitor,on_delete=models.CASCADE)
    text=models.TextField()
    reply=models.ForeignKey('ReplyComment',on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return " comment for "+ self.text + " by " + self.commenter.username

class ReplyComment(Timestamp):
    text=models.TextField()

    def __str__(self):
                return self.text      