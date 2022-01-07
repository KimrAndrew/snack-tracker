from django.views.generic import TemplateView, ListView
from .models import Snack

# Create your views here.
class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack

class SnackPageView(TemplateView):
    template_name = 'snacks.html'