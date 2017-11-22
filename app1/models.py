from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length = 30,blank = True,default = '')
    desc = models.TextField()

    def __str__(self):
        return self.name
   
    # if we want to specifically named the table for this model
    class Meta:
        db_table = "item_table"
