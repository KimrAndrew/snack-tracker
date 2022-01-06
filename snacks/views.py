from django.views.generic import TemplateView

# Create your views here.
class SnackPageView(TemplateView):
    template_name = 'home.html'