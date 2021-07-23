from django import forms
from core.models import Contact


class ContactForm(forms.Form):
    email = forms.EmailField(required=False)
    phone = forms.CharField(required=False)
    message = forms.CharField(required=False, widget=forms.Textarea)
    file = forms.FileField(required=False)

    def send_email(self):

        print("Se envio el correo")

    def save_file(self):
        # logica para guardar el archivo
        print("Archivo guardado...")

    def save_contact(self):
        # Instancia objeto
        contact = Contact()

        # Rellena datos en objeto
        contact.email = self.cleaned_data["email"]
        contact.phone = self.cleaned_data["phone"]

        # Salva los datos en BD
        contact.save()

        print("Contacto guardado...")