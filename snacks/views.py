from django.views.generic import TemplateView

# Create your views here.
class SnackPageView(TemplateView):
    template_name = 'snacks.html'