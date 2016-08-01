from django import forms
import decimal


class QueryForm(forms.Form):
<<<<<<< HEAD
    latitude = forms.DecimalField(widget=forms.HiddenInput())
    longitude = forms.DecimalField(widget=forms.HiddenInput())
=======
	latitude = forms.DecimalField(widget = forms.HiddenInput())
	longitude = forms.DecimalField(widget = forms.HiddenInput())
    
	radius = forms.DecimalField(max_digits=6, decimal_places=3, min_value=decimal.Decimal(0), initial=1.0, \
	                            widget = forms.NumberInput(attrs={'class':'form-control',\
	                                'placeholder':'1.0', 'autofocus':'on'}))
	limit = forms.IntegerField(min_value=0, initial=10, \
								widget = forms.NumberInput(attrs={'class':'form-control',\
	                                'placeholder':'10', 'autofocus':'on'}))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> parent of b0ac281... addded pep8 code styling using autopep8
=======
>>>>>>> parent of b0ac281... addded pep8 code styling using autopep8
=======
>>>>>>> parent of b0ac281... addded pep8 code styling using autopep8

    radius = forms.DecimalField(max_digits=6, decimal_places=3, min_value=decimal.Decimal(0), initial=1.0,
                                widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                'placeholder': '1.0', 'autofocus': 'on'}))
    limit = forms.IntegerField(min_value=0, initial=10,
                               widget=forms.NumberInput(attrs={'class': 'form-control',
                                                               'placeholder': '10', 'autofocus': 'on'}))
