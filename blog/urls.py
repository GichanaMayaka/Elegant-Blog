from django.conf.urls import url, include
from . import views
from . import feed
from qblog import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^home/$', views.BlogIndex.as_view(), name='index'),
    url(r'^entry/(?P<slug>\S+)/$', views.BlogDetail.as_view(), name='entry_detail'),
    url(r'^register/$', views.register, name='register'),
    url(r'^feed/$', feed.LatestPosts(), name='feed'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += staticfiles_urlpatterns()
