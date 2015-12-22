from django.db import models

# Guest model where the guest name and id are saved
class Guest(models.Model):
    guest_name = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % (self.guest_name)

# Coordinates model where the coordinates are saved in relation with the Guest model
class Coordinates(models.Model):
    lat_value = models.FloatField()
    lng_value = models.FloatField()
    id_guest = models.ForeignKey(Guest)

    def __unicode__(self):
        return u'%s %s %s' % (self.lat_value, self.lng_value, self.id_guest)

