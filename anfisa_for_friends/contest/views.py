from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContestForm
from .models import Contest


def proposal(request, pk=None):
    if pk:
        instance = get_object_or_404(Contest, id=pk)
    else:
        instance = None
    form = ContestForm(request.POST or None, instance=instance)
    context = {'form': form}
    if form.is_valid():
        form.save()
        context.update({'form': form})
    return render(request, 'contest/form.html', context)


def proposal_list(request):
    claims = Contest.objects.all().order_by('id')
    context = {'claims': claims}
    return render(request, 'contest/contest_list.html', context)


def delete_proposal(request, pk):
    instance = get_object_or_404(Contest, id=pk)
    print(instance.__dict__)
    form = ContestForm(instance=instance)
    context = {'form': form}
    if request.method == 'POST':
        instance.delete()
        return redirect('contest:list')
    return render(request, 'contest/form.html', context)
