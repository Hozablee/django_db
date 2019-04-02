from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from polls import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^create_register/$', views.create_register, name='create_register'),
    url(r'^login/$', views.login , name='login'),
    url(r'^main_page/$', views.main_page , name='main_page'),
    url(r'^logout_view/$', views.logout_view , name='logout_view'),
    url(r'^check_login/$', views.check_login , name='check_login'),
    url(r'^home_page/$', views.home_page, name='home_page'),
    url(r'^goods1/(?P<item>\w+)/$', views.goods1, name='goods1'),
    url(r'^create_shipment/$', views.create_shipment, name='create_shipment'),
    url(r'^show_shipment/$', views.show_shipment, name='show_shipment'),
    # url(r'^buying/$', views.buying, name='buying'),
]
