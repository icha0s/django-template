"""URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Function views:
    1. Add an import:  from my_app import views;
    2. Add a URL to urlpatterns:  path('', views.home, name='home');
Class-based views:
    1. Add an import:  from other_app.views import Home;
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home');
Including another URLconf:
    1. Import the include() function: from django.urls import include, path;
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'));
"""
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("grappelli/", include("grappelli.urls")),
    path("management/", admin.site.urls),
    path("health/", include("watchman.urls")),
    path("api/", include("api.urls")),
    path("", include('web.urls')),
]

if "rosetta" in settings.INSTALLED_APPS:
    urlpatterns += [path("rosetta/", include("rosetta.urls"))]

if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
