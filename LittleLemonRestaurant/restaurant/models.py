from django.db import models

class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name

   
class MenuItem(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField()
   description = models.TextField(max_length=1000)
   image = models.ImageField(upload_to = 'restaurant\static\img\menu_items',null= False,default='logo_footer.png')

   def __str__(self):
       return self.name
