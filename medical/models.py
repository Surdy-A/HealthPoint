from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

BLODD_GROUP = (
    ('A RhD positive', 'A+'),
    ('A RhD negative', 'A-'),
    ('B RhD positive', 'B+'),
    ('B RhD negative', 'B-'),
    ('O RhD positive', 'O+'),
    ('O RhD negative', 'O-'),
)

GENOTYPE = (
    ('AA', 'AA'),
    ('AS', 'AS'),
    ('AC', 'AC'),
    ('SS', 'SS'),
    ('SC', 'SC'),
    ('CC', 'CC'),
)


class Patient(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    middle_name = models.CharField(max_length=100, default='')
    email = models.EmailField()
    age = models.PositiveIntegerField()
    blood_group = models.CharField(choices=BLODD_GROUP,
                                   max_length=100,
                                   default='')
    gentotype = models.CharField(choices=GENOTYPE, max_length=100, default='')
    ailment = models.CharField(max_length=100, default='')
    doctor_last_seen = models.CharField(max_length=100, default='')

    image = models.ImageField(upload_to='images/freeclancers',
                              default='images/freelancerAvatar.png')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(120, 120)],
                                     format='JPEG',
                                     options={'quality': 60})


class Practitioner(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    middle_name = models.CharField(max_length=100, default='')
    specialization = models.CharField(max_length=100, default='')
    email = models.EmailField()
    age = models.PositiveIntegerField()
    ailment = models.CharField(max_length=100, default='')
    seen_hours = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='images/freeclancers',
                              default='images/freelancerAvatar.png')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(120, 120)],
                                     format='JPEG',
                                     options={'quality': 60})
