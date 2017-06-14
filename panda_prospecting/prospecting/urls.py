from django.conf.urls import url

from . import views

app_name = 'prospecting'
urlpatterns = [
    # ex: /prospect/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /prospect/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /prospect/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /prospect/5/view/
    url(r'^(?P<account_id>[0-9]+)/prospect_view/$', views.ProspectViewView, name='prospect_view'),
]
