from django.db import models
from jsignature.fields import JSignatureField

# Create your models here.

class SignatureModel(models.Model):
	signature = JSignatureField()

class Resguardos(models.Model):
	class Meta:
		verbose_name_plural = 'resguardos'
	name = models.CharField(max_length=32, blank=True, null=True)
	gid = models.CharField(max_length=50, blank=True, null=True)
	department = models.CharField(max_length=20, blank=True, null=True)
	position = models.CharField(max_length=50, blank=True, null=True)
	device = models.CharField(max_length=50, blank=True, null=True)
	detail = models.CharField(max_length=50, blank=True, null=True)
	signature = models.ForeignKey(SignatureModel, on_delete=models.CASCADE)

	def __str__(self):

		return str(self.name)