from django.conf.urls import patterns, include, url
from zipcode import views
from django.views.generic import TemplateView


urlpatterns = patterns('',
   url(r'^robots\.txt$', TemplateView.as_view(template_name='zipcode/robots.txt'), name="robots"),
   url(r'^$', views.home, name="home"),
   url(r'^search/$', views.get_zip,),
   url(r'^search/(?P<postcode>\d{5})$', views.results, name='results'),
   url(r'^(?P<f>\w+)\/(?P<id>\d+)\/(?P<l>\w+)\/$', views.contractor_detail_view, name="contractor"),
   url(r'contact/$', views.get_contact, name="contact"),
   url(r'testimonial_post\/(?P<id>\d+)', views.post_testimonial, name="post_testimonial"),
   url(r'thanks/$', TemplateView.as_view(template_name="thanks.html"), name="thanks"),
   url(r'careers/$', views.get_resume, name="careers"),
   url(r'gallery/$', views.show_gallery, name="gallery"),
   url(r'schedule/$', views.request_event, name="schedule"),
   url(r'^(?P<id>\d+)\/(?P<currentyear>\d{4})\/(?P<currentmonth>0?[1-9]|1[012])', views.last_month_request , name="last_month_request"),
   url(r'^(?P<id>\d+)\/(?P<currentmonth>0?[1-9]|1[012])\/(?P<currentyear>\d{4})', views.next_month_request , name="next_month_request"),
   url(r'^(?P<id>\d+)\/monthly-specials\/(?P<special>\w+(?:\-\w+)*)', views.monthly_special_detail , name="monthly_special"),
   url(r'^cm/(?P<currentdate>\d+)/(?P<uid>\d+)/(?P<currentyear>20[0-9]{2})/(?P<currentmonth>\d+)', views.calendar_manager , name="calendar_manager"),
)
