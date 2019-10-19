from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import  ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View

from webapp.forms import PollForm
from webapp.models import Poll, Choice, Answer


class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    ordering = '-created_at'
    paginate_by = 2
    paginate_orphans = 1


class PollAnswerView(View):
    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        choices = poll.text_poll.all()
        context = {
            'poll': poll,
            'choices': choices
        }
        return render(request, 'poll/answer.html', context)

    def post(self, request, *args, **kwargs):
        pk = request.POST['answer']
        answer = get_object_or_404(Choice, pk=pk)
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        Answer.objects.create(answer=answer, poll=poll)
        return redirect('index')


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