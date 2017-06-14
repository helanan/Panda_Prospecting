from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /prospect/
    url(r'^$', views.index, name='index'),
    # ex: /prospect/5/
    url(r'^(?P<account_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /prospect/5/results/
    url(r'^(?P<account_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /prospect/5/vote/
    url(r'^(?P<account_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
