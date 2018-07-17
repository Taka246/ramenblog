from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Ramen
from io import BytesIO
from .lib import predict
from PIL import Image
import numpy as np
import base64


def Index(request):
    return render(request, 'index.html')

class RamenList(ListView):
    model = Ramen
    paginate_by = 7

    def get_queryset(self):
    # 作成日順に並び替え
        return super().get_queryset().order_by('-created_at')

class RamenDetail(DetailView):
    model = Ramen

class Mnist(TemplateView):
    template_name = 'RamenBlog/paint.html'

    def post(self, request):
        base_64_string = request.POST['img-src'].replace(
            'data:image/png;base64,', '')
        file = BytesIO(base64.b64decode(base_64_string))
        img = Image.open(file).resize((28, 28)).convert('L')
        img_array = np.asarray(img) / 255
        img_array = img_array.reshape(1, 784)

        # 推論した結果を、テンプレートへ渡して表示
        context = {
            'result': predict(img_array),
        }
        return render(self.request, 'RamenBlog/result.html', context)
