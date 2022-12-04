from django.db import models

class Wreck(models.Model):
  vessel_name = models.CharField(max_length=200, unique=True)
  # TODO (Heath): This can be a GIS point in a database that supports that, but
  # for now just going to keep it as lat / lon as we're using sqlite.
  # There's only about 150 records in the first version, so no need to go too
  # crazy in IMO.
  latitude = models.FloatField()
  longitude= models.FloatField()
  year = models.IntegerField(default=None, null=True)
  wreckhunter_link = models.URLField(default='', null=True)
  beavertail_link = models.URLField(default='', null=True)

  ordering = ['vessel_name']
  def __str__(self):
    return self.vessel_name