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
    # ex:
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    # ex: /prospecting/5/prospect_views/
    url(r'^(?P<account_id>[0-9]+)/prospect_view/$', views.ProspectViewView, name='prospect_view'),
    # page for adding a new account
    url(r'^new_account/$', views.new_account, name='new_account'),
    # page for adding a new prospect
    url(r'^new_prospect/(?P<account_id>\d+)/$', views.new_prospect, name='new_prospect'),
    # editing account information view
    url(r'^edit_account/(?P<account_id>\d+)/$', views.edit_account, name='edit_account'),
    # editing prospect information view
    url(r'^edit_prospect/(?P<prospect_id>\d+)/$', views.edit_prospect, name='edit_prospect'),

]
