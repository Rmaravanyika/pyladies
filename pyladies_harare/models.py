from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField


class Category(models.Model):
    category = models.CharField(max_length=120)
    shortdesc = models.CharField(max_length=120)
    description = models.CharField(max_length=255)

    class Meta:
        managed = True

    def __str__(self):
        return self.category


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    summary = models.TextField()
    text = models.TextField()
    picture = models.ImageField(max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    category = models.ForeignKey(Category)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField("full name", max_length=120)
    phone = models.CharField("phone number", max_length=30)
    email = models.CharField("email address", max_length=120)
    subject = models.CharField(max_length=120)
    message = models.TextField()
    emaildate = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.name


class Page(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    picture = models.ImageField(max_length=200, null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Meetup(models.Model):
    name = models.CharField(max_length=200)
    fromdate = models.DateTimeField('From date', default=timezone.now)
    todate = models.DateTimeField('To date', default=timezone.now)
    location = models.CharField(max_length=200)
    website = models.TextField()
    comments = models.TextField()
    dateposted = models.DateTimeField('Date posted', default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    ispast = models.BooleanField(default=True)
    isdisplayed = models.BooleanField(default=False)

    class Meta:
        managed = True

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Comment(models.Model):
    name = models.CharField("full name", max_length=120)
    email = models.CharField("email address", max_length=120)
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    post = models.ForeignKey('Post')

    class Meta:
        managed = True

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()