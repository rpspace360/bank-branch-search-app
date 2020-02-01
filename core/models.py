from django.db import models
import uuid


class Bank(models.Model):
    id = models.BigIntegerField(primary_key=True, help_text='ID bank')
    name = models.CharField(max_length=49, help_text='Bank Name')
    

class Branch(models.Model):
    """
    ifsc     | character varying(11)  | not null
    bank_id  | bigint                 | 
    branch   | character varying(74)  | 
    address  | character varying(195) | 
    city     | character varying(50)  | 
    district | character varying(50)  | 
    state    | character varying(26)  | 
    """
    branch = models.CharField(max_length=74, null=True, help_text='Branch Name')
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE)
    address = models.CharField(max_length=195, help_text='Branch Address')
    ifsc = models.CharField(max_length=11, null=False, blank=False, help_text='Branch IFSC code')
    city = models.CharField(max_length=300, help_text='Branch City')
    district = models.CharField(max_length=50, help_text='Branch District')
    state = models.CharField(max_length=26, null=False, help_text='branch state')

    def __str__(self):
        return self.branch
