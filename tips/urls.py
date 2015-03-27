from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tips.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^entry/', include('entry.urls')),
    url(r'^entry/admin/', include('entry_admin.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name="accounts_login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name="accounts_logout"),
    url(r'^admin/', include(admin.site.urls)),
)
