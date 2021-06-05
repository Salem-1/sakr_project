from django.db import models

# Create your models here.
#creating table to save all retrieved articles
class Articles(models.Model):
    """Saving all retrieved articles link, title and datetime stamp for the inquery"""
    url = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    datetime = models.CharField(max_length=64)


    def __str__(self):
        """admin friendly django shell interface code"""
        return f"{self.url}: \n({self.title}) \n{self.datetime}"
