# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.core.urlresolvers import reverse

User = get_user_model()

types = (
    ('a', 'Sheet'),
    ('b', 'Exam'),
    ('c', 'others'),
)


def upload_location(instance, filename):
    if instance.id:
        new_id = instance.id
    else:
        try:
            new_id = Answer.objects.order_by("id").last().id + 1
        except:
            new_id = 1
    return "answers/%s/%s" % (new_id, filename)


# Create your models here.

class Answer(models.Model):
    user = models.ForeignKey(User, default=1, null=False)
    title = models.CharField(null=False, max_length=50)
    note = models.TextField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    wait = models.BooleanField(default=False)
    type = models.CharField(choices=types, max_length=3, default=1)
    file = models.FileField(null=False,
                            blank=False,
                            upload_to=upload_location)
    class Meta:
        ordering = ["-timestamp"]

    def __unicode__(self):
        return "%s:%s" % (self.user, self.title)

    def get_absolute_url(self):
        return reverse("answers:detail", kwargs={'slug': self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Answer.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Answer)
