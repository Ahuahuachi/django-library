from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(, max_length=, required=False)
    message = forms.Textarea()
    date = forms.DateField()




class BookForm(forms.Form):
    title = forms.CharField()
    author = forms.ChoiceField()
    publishing_year = forms.DateField()
    publishing_house = forms.ChoiceField()
    pages = forms.IntegerField()