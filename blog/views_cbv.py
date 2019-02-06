from django import forms
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import Post

# /?page= 로 페이지 접근
post_list = ListView.as_view(model=Post, paginate_by=3)
post_detail = DetailView.as_view(model=Post)
post_new = CreateView.as_view(model=Post, fields='__all__')
post_edit = UpdateView.as_view(model=Post, fields='__all__')
post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))
