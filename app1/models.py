from django.db import models

# Create your models here.
class TransactionDT(models.Model):
    """Het ozo bekende timestamp model, nog aan te vullen met de userid van de login.
    De Transaction Time"""
    created_dt = models.DateTimeField(auto_now_add=True, null=True)
    modified_dt = models.DateTimeField(auto_now=True, null=True)
    last_modified_user = models.ForeignKey('auth.User', verbose_name='User who last modified record',
                                           null=True, blank=True)

    class Meta:
        abstract = True

