from django import forms
from django.forms.fields import ChoiceField, FilePathField


INSTRUMENT_CHOICE = (
    (u'O', u'Orbitrap'),
    (u'L', u'LTQ'),
)

DBASE_CHOICE = (
    (u'Y', u'Yeast'),
    (u'H', u'Human'),
    (u'E', u'Eighteen mix'),
    (u'B', u'BSA'),
)

class DocumentForm(forms.Form):

    filepath = forms.CharField(max_length=200,
        label = 'Input the directory of your mzML file(s)',
        widget=forms.Textarea(attrs={'cols': 100, 'rows': 1})
    )

    instrument = forms.CharField(max_length=2,
        label = 'Choose an instrument',
        widget = forms.Select(choices=INSTRUMENT_CHOICE))

    database = forms.CharField(
        label = 'Choose a database for the search',
        widget = forms.Select(choices=DBASE_CHOICE))

    email = forms.CharField(max_length=50,
        label = 'Your email address')
