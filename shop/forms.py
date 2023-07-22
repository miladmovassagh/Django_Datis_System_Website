from django import forms

class SearchProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="search")