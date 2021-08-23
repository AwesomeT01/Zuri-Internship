from django.db import models

# Create your models here.
#Createsuperuser Username = Admin

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    date_of_contact = models.DateTimeField(auto_now_add=True, null=True)

    def __str__ (self):
        return self.name
