from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Prospect, Account


class IndexView(generic.ListView):
    """Docstring goes here."""

    template_name = 'prospecting/index.html'
    context_object_name = 'latest_account_list'

    def get_queryset(self):
        """Return the last five added accounts (not including those set to be
        published in the future)."""
        return Account.objects.order_by('-date_added')[:5]


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
