from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import *
from .froms import AddInductorForm


# Create your views here.

def main(request: HttpRequest):
    return render(request, 'main_app/main.html')


def create_inductors(request: HttpRequest):
    if request.method == 'POST':
        form = AddInductorForm(request.POST, request.FILES)
        if form.is_valid():
            # try:
            #     Inductors.objects.create(**form.cleaned_data)
            #     return redirect('main')
            # except:
            #     form.add_error(None, "ERrror")
            form.save()
            return redirect('main')
    else:
        form = AddInductorForm()
    context = {'form': form}
    return render(request, 'main_app/inductor.html', context=context)


class InductorsListView(ListView):
    model = Inductors
    template_name = 'main_app/inductor_list.html'
    context_object_name = 'posts'

class InductorDetailView(DetailView):
    model = Inductors
    context_object_name = 'inductor'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tests'] = TestInductor.objects.filter(inductor_id=context.get('object').pk)
        print(context)
        return context

class TestsListView(ListView):
    model = TestInductor
    template_name = 'main_app/test_list.html'
    context_object_name = 'tests'