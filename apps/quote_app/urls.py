from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
    url(r'^add/(?P<user_id>\d+)$', views.add),
    url(r'^additem$', views.additem),
    url(r'^add_item$', views.add_item),
    url(r'^delete/(?P<quote_id>\d+)$', views.delete),
    url(r'^addto/(?P<quote_id>\d+)$', views.addto),
    url(r'^remove/(?P<quote_id>\d+)$', views.remove),
    url(r'^info/(?P<quote_id>\d+)$', views.info),
]
