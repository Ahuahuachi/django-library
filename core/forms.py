from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(required=False)
    phone = forms.CharField(required=False)
    message = forms.CharField(required=False, widget=forms.Textarea)
    file = forms.FileField(required=False)

    def send_email(self):

        # Instanciar modelo
        # colocar datos en modelo
        # guardar modelo

        # logica para enviar nuestro correo

        print("Se envio el correo")

    def save_file(self):
        # logica para guardar el archivo
        print("Archivo guardado...")

    def save_contact(self):
        # logica para guardar el contacto

        print("Contacto guardado...")