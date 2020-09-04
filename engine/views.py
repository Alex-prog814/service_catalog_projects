from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)

from .forms import AddItemForm, UpdateItemForm
from .models import Item, Category


class ItemsListView(ListView):
    model = Item
    template_name = 'engine/item_list.html'
    context_object_name = 'items'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(text__icontains=search) | Q(category__name__icontains=search))
        if category is not None:
            queryset = queryset.filter(category_id=category)
        return queryset


class ItemDetailsView(DetailView):
    model = Item
    template_name = 'engine/item_details.html'
    context_object_name = 'item'


class ViewsMixin:
    def get_success_url(self):
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['item_form'] = self.get_form(self.get_form_class())
        return context


class AddItemView(LoginRequiredMixin, ViewsMixin, CreateView):
    model = Item
    template_name = 'engine/add_item.html'
    form_class = AddItemForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddItemView, self).form_valid(form)


class UpdateItemView(LoginRequiredMixin, UserPassesTestMixin, ViewsMixin, UpdateView):
    model = Item
    template_name = 'engine/update_item.html'
    form_class = UpdateItemForm
    context_object_name = 'item'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class DeleteItemView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    template_name = 'engine/delete_item.html'
    success_url = reverse_lazy('home-page')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CategoriesListView(ListView):
    model = Category
    template_name = 'engine/index.html'
    context_object_name = 'categories_list'

