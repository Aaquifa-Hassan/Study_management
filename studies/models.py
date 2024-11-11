#create model here
from django.db import models
class Study(models.Model):
    study_name = models.CharField(max_length=255)
    study_description = models.TextField()
    study_phase = models.CharField(
        max_length=20,
        choices=[
            ('Phase I', 'Phase I'),
            ('Phase II', 'Phase II'),
            ('Phase III', 'Phase III'),
            ('Phase IV', 'Phase IV')
        ]
    )
    sponsor_name = models.CharField(max_length=255)

    def __str__(self):
        return self.study_name


