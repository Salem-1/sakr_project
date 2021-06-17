from django.db import models

# Create your models here.
#creating table to save all retrieved articles
class Articles(models.Model):
    """Saving all retrieved articles link, title and datetime stamp for the inquery"""
    url = models.TextField()
    title = models.TextField()
    datetime = models.TextField()


    def __str__(self):
        """admin friendly django shell interface code"""
        return f"url :{self.url[:10]}: \nTitile: ({self.title}) \nDate:{self.datetime}"
