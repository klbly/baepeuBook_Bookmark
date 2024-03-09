# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

from .models import Bookmark

# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6     # 페이지 화 처리: 한 페이지에 몇 개씩 출력할건지

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')  # 이번 작업이 성공하면 이동할 페이지, views.py의 success_url 또는 model.py의 get_absolute_url 메서드를 통해 결정된다.
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):   # ListView와 다르게 DetailView는 하나의 정보만 출력한다.
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')  # 이번 작업이 성공하면 이동할 페이지, views.py의 success_url 또는 model.py의 get_absolute_url 메서드를 통해 결정된다.