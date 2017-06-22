from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.utils import timezone

from .models import Prospect, Account
from .forms import AccountForm, ProspectForm


class IndexView(generic.ListView):
    """Docstring goes here."""

    template_name = 'prospecting/index.html'
    context_object_name = 'latest_account_list'

    def get_queryset(self):
        """Return the last five added accounts (not including those set to be
        published in the future)."""
        return Account.objects.order_by('-date_added')


# Create your views here.

class DetailView(generic.DetailView):
    """Docstring goes here."""
    model = Account
    template_name = 'prospecting/detail.html'

    def get_queryset(self):
        """
        Excludes any accounts that aren't added yet.
        """
        return Account.objects.filter(date_added__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Account
    template_name = 'prospecting/results.html'

@login_required
def ProspectViewView(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    try:
        selected_prospect = account.prospect_set.get(pk=request.POST['prospect'])
    except (KeyError, Prospect.DoesNotExist):
        # Redisplay the prospect selection form.
        return render(request, 'prospecting/detail.html', {
            'account': account,
            'error_message': "You didnt select a prospect.",
        })
    else:
        selected_prospect.prospect_views += 1
        selected_prospect.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a user
        # hits the back button
    return HttpResponseRedirect(reverse('prospecting:results', args=(account.id,)))

def single_prospect(request, prospect):
    """View single prospect."""
    all_prospects = Prospect.objects.all()
    selected_prospect = all_prospects(id=pk)
    context = {'selected_prospect': selected_prospect}
    return render(request, 'prospecting/results.html', context)

@login_required
def new_account(request):
    """Add a new account."""
    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = AccountForm()
    else:
        # POST data submitted; process data
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('prospecting:index'))

    context = {'form': form}
    return render(request, 'prospecting/new_account.html', context)

@login_required
def new_prospect(request, account_id):
    """Adds a new prospect for a selected account."""
    account = Account.objects.get(id=account_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ProspectForm()

    else:
        # POST data submitted; process data.
        form = ProspectForm(data=request.POST)
        if form.is_valid():
            new_prospect = form.save(commit=False)
            new_prospect.account = account
            new_prospect.save()
            return HttpResponseRedirect(reverse('prospecting:results', args=[account_id]))

    context = {'account': account, 'form': form}
    return render(request, 'prospecting/new_prospect.html', context)

@login_required
def edit_account(request, account_id):
    """Edit an existing account."""
    account = Account.objects.get(id=account_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current prospect info
        form = AccountForm(instance=account)
    else:
        # POST data submitted; process data.
        form = AccountForm(instance=account, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('prospecting:detail', args=[account.id]))
    context = {'account': account, 'form': form}
    return render(request, 'prospecting/edit_account.html', context)

@login_required
def edit_prospect(request, prospect_id):
    """Edit an existing prospect."""
    prospect = Prospect.objects.get(id=prospect_id)
    account = prospect.account

    if request.method != 'POST':
        # Initial request; pre-fill form with the current prospect info
        form = ProspectForm(instance=prospect)
    else:
        # POST data submitted; process data.
        form = ProspectForm(instance=prospect, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('prospecting:detail', args=[account.id]))
    context = {'prospect': prospect, 'account': account, 'form': form}
    return render(request, 'prospecting/edit_prospect.html', context)

@login_required
def dashboard(request):
    """Analyses of accounts within a dashboard view."""
    prospect = Prospect.objects.all()
    context = {'prospect': prospect}
    return render(request, 'prospecting/dashboard.html', context)
