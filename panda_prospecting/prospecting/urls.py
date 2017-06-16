from django.conf.urls import url

from . import views

app_name = 'prospecting'
urlpatterns = [
    # ex: /prospecting/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /prospecting/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /prospecting/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /prospecting/5/views/
    url(r'^(?P<account_id>[0-9]+)/prospect_view/$', views.ProspectViewView, name='prospect_view'),
    # page for adding a new topic
    url(r'^new_account/$', views.new_account, name='new_account'),
    # page for adding a new prospect
    url(r'^new_prospect/(?P<account_id>\d+)/$', views.new_prospect, name='new_prospect'),
]
