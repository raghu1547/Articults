"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from accounts import views
from django.conf import settings
from django.conf.urls.static import static
from newsletter import views as newsletter_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Homepage.as_view(),name='home'),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('post/',include('posts.urls',namespace='posts')),
    path('groups/',include('groups.urls',namespace='groups')),
    path('test/',views.TestPage.as_view(),name='test'),
    path('about/',views.AboutPage.as_view(),name='about'),
    path('thanks/',views.ThanksPage.as_view(),name='thanks'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('subscribe/', newsletter_views.new, name='subscribe'),
    path('confirm/', newsletter_views.confirm, name='confirm'),
    path('delete/', newsletter_views.delete, name='delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#from django.conf import settings
#from django.urls import include, path

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
