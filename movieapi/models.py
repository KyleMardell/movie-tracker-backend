from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    tmdb_id = models.IntegerField()
    image_path = models.CharField(max_length=255)
    watched = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'tmdb_id'],
                name='unique_user_tmdb_movie'
            )
        ]
        
    def __str__(self):
        return self.title