from django.views.generic import ListView, DetailView
from .models import Ramen

class RamenList(ListView):
    model = Ramen
    pagenate_by = 5

    def get_queryset(self):
    # 作成日順に並び替え
        return super().get_queryset().order_by('-created_at')

class RamenDetail(DetailView):
    model = Ramen
    
