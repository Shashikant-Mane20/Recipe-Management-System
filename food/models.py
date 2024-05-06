from django.db import models

# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_name
    item_name=models.CharField(max_length=200)
    item_ingre=models.TextField(max_length=1000)
    item_desc=models.TextField(max_length=1000)
    item_image=models.CharField(max_length=500,default='https://media.istockphoto.com/id/936182806/vector/no-image-available-sign.jpg?s=612x612&w=0&k=20&c=9HTEtmbZ6R59xewqyIQsI_pQl3W3QDJgnxFPIHb4wQE=')