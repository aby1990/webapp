from django.db import models


QUAL_CHOICES = (
            
    ('hs', 'High School'),
    ('ss', 'Secondary School'),
    ('Bach', 'Bachelors'),
    ('Masters', 'Masters'),
    
)

class Details(models.Model):
    name = models.CharField(max_length=30)
    bdate = models.DateField(verbose_name="Birthdate (yyyy-mm-dd)");
    email = models.EmailField(max_length=30)
    mobile = models.CharField(max_length=10, verbose_name="Cell No.")
    qual = models.CharField(max_length=20, choices=QUAL_CHOICES, verbose_name="Qualification")
    skill = models.CharField(max_length=60, verbose_name="Skills")

    def __unicode__(self):
        return self.name
