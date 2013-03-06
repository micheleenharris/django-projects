from django.db import models
#from django.forms import ModelForm

#INSTRUMENT_CHOICE = (
#    (u'O', u'Orbitrap'),
#    (u'L', u'LTQ'),
#)

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

#class Instrument(models.Model):
#    instrument = models.CharField(max_length=2, choices=INSTRUMENT_CHOICE)

#    def __unicode__(self):
#        return self.instrument

#class InstrumentForm(ModelForm):
#    class Meta:
#        model = Instrument
