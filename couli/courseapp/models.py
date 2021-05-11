from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Foramteur(models.Model):
    """Model definition for Foramteur."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='foramteur')
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Foramteur.objects.create(user=instance)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Foramteur."""

        verbose_name = 'Foramteur'
        verbose_name_plural = 'Foramteurs'

    def __str__(self):
        """Unicode representation of Foramteur."""
        self.user.username

class Cours(models.Model):
    """Model definition for Cours."""
    prof = models.ForeignKey(Foramteur, on_delete=models.CASCADE, related_name='cours_prof')
    titre = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FileField(upload_to="cours/image")
    publication = models.DateField()
    slug = AutoSlugField(populate_from='titre', unique=True)
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    

    # TODO: Define fields here

    class Meta:
        """Meta definition for Cours."""

        verbose_name = 'Cours'
        verbose_name_plural = 'Cours'

    def __str__(self):
        """Unicode representation of Cours."""
        return f'{self.titre}'

class Chapitre(models.Model):
    """Model definition for Chapitre."""
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name='cours_chapitre')
    titre = models.CharField(max_length=250)
    description = models.TextField()
    slug = AutoSlugField(populate_from='titre', unique=True)
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Chapitre."""

        verbose_name = 'Chapitre'
        verbose_name_plural = 'Chapitres'

    def __str__(self):
        """Unicode representation of Chapitre."""
        return f"{self.cours.titre} - {self.titre}"


