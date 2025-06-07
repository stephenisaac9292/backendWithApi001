from django.db import models

class StaffRegistry(models.Model):
    staff_number = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=150)  
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.staff_number
 