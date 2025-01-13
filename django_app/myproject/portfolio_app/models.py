from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()  # Optional field to link to the project
    image = models.ImageField(upload_to='project_images/', default='project_images/img.jpg')  # Default image

    def __str__(self):
        return self.title
