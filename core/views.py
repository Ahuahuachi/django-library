from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = "core/index.html"
    page_title = "Index"

    def get_context_data(self, **kwargs):
        # Llama al metodo get_context_data de la clase padre
        context = super().get_context_data(**kwargs)

        # Añado atributos al contexto
        context["page_title"] = self.page_title

        # Retorno el contexto
        return context
