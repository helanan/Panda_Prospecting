from django.http import HttpResponse

from .models import Account


def index(request):
    """Docstring goes here."""
    latest_account_list = Account.objects.order_by('date_added')[:5]
    output = ', '.join([q.account_text for q in latest_account_list])
    return HttpResponse(output)

# Create your views here.
def detail(request, account_id):
    return HttpResponse("You're looking at an account%s." % account_id)

def results(request, account_id):
    response = "You're looking at the results of accounts %s."
    return HttpResponse(response % account_id)

def vote(request, account_id):
    return HttpResponse("You're voting on an account %s." % account_id)
