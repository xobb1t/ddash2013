from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='index.html')),
)
