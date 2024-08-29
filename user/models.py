from django.db import models
from django.utils.text import slugify

# Create your models here.
class User(models.Model):
    pseudo = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=15)
    slug = models.SlugField(blank=True)
    creation_date = models.DateField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        #pour eviter les doublons dans le slug
        if not self.slug: 
            self.slug = slugify(self.pseudo)
            original_slug = slugify(self.pseudo)
            for i in range(1, 100):
                if not User.objects.filter(slug=original_slug).exists():
                    break
                original_slug = f"{original_slug}-{i}"
            super(User, self).save(*args, **kwargs)
        self.slug = slugify(self.pseudo)
        super(User, self).save(*args, **kwargs)
    
    
    def __str__(self):
        return self.pseudo, self.creation_date
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    