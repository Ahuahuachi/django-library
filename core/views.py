from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from core.forms import ContactForm

# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = "core/index.html"
    page_title = "Index"
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        # Llama al metodo get_context_data de la clase padre
        context = super().get_context_data(**kwargs)

        # Añado atributos al contexto
        context["page_title"] = self.page_title
        context["form"] = self.form_class

        # Retorno el contexto
        return context


class ContactFormView(FormView):
    template_name = "core/contact-us.html"
    form_class = ContactForm
    success_url = "/thank-you/"

    def form_valid(self, form):

        form.save_contact()

        form.save_file()

        form.send_email()

        return super().form_valid(form)

    def form_invalid(self, form):

        return super().form_invalid(form)


class ThankYouTemplateView(TemplateView):
    template_name = "core/thank-you.html"