from django.db import models

# Create your models here.
class Computer(models.Model):
	YEARS = (
		( None, 'Select Year'),
		('I', 'I'),
		('II', 'II'),
		('II', 'III'),
	)
	GENDER = (
		( None, 'Select Gender'),
		('Male', 'Male'),
		('FeMale', 'FeMale')
	)
	DEGREE = (
		( None, 'Select Degree'),
		('BA', 'BA'),
		('BSC', 'BSC'),
		('BCOM', 'BCOM'),
		('MA', 'MA'),
		('MSC', 'MSC'),
		('MCOM', 'MCOM'),
	)
	DEPT = (
		( None, 'Select Department'),
		('TAMIL','TAMIL'),
		('ENGLISH','ENGLISH'),
		('MATHS','MATHS'),
		('CS','CS'),
		('COMMERCE', 'COMMERCE'),
	)	
	fullName = models.CharField(max_length=30)
	fatherName = models.CharField(max_length=30)
	dob = models.CharField(max_length=30)
	gender = models.CharField(max_length=30, null=True, choices = GENDER)
	email = models.EmailField(max_length=30)
	degree = models.CharField(max_length=30, null=True, choices = DEGREE)
	dept = models.CharField(max_length=30, null=True, choices = DEPT)
	year = models.CharField(max_length=30,null=True, choices= YEARS)
	address = models.CharField(max_length=50, null=True)
	city = models.CharField(max_length=30, null=True)
	state = models.CharField(max_length=30, null=True)
	pin = models.CharField(max_length=30, null=True)
	def __str__(self):
		return self.fullName
