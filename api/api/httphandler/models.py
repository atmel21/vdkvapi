from django.db import models

class KeyValueStore(models.Model):
    rownum = models.AutoField(primary_key=True)
    keyid = models.TextField(blank=False,null=False)
    val = models.BinaryField(blank=True, null=True)
    modified = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'key_value_store'
        unique_together = (('keyid', 'modified'),)
        
    def __unicode__(self):
        return self.val