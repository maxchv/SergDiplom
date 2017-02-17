"""xXx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import logout

from landing import views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('landing.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^orders/', include('orders.urls')),
    url(r'^login_ajax/$', views.login_ajax, name='login_ajax'),
    url(r'^register_ajax/$', views.registration_ajax, name='registration_ajax'),
    url(r'^logout/$', logout, {"next_page": "/"}, name='landing_logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
