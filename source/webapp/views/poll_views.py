from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import  ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import PollForm
from webapp.models import Poll




class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    ordering = '-created_at'
    paginate_by = 2
    paginate_orphans = 1




class PollView(DetailView):
    template_name = 'poll/poll.html'
    pk_url_kwarg = 'pk'
    model = Poll


class PollCreateView(CreateView):
    template_name = 'poll/create.html'
    model = Poll
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    model = Poll
    template_name = 'poll/update.html'
    form_class = PollForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    template_name = 'poll/delete.html'
    model = Poll
    context_object_name = 'poll'
    success_url = reverse_lazy('index')