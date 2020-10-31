from django.db import models

# Create your models here.
class Employee(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	age = models.IntegerField()
	pic = models.ImageField(upload_to="images/",blank=True)

	class Meta:
		db_table = "CRUDemployee"