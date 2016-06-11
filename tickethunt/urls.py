"""tickethunt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from backend.views import TicketViewSet, TicketTypeViewSet, TicketTypeAliasViewSet
from tickethunt import settings
from django.views.static import serve

router = routers.DefaultRouter()
router.register(r'ticket', TicketViewSet, base_name="ticket")
router.register(r'tickettype', TicketTypeViewSet, base_name="tickettype")
router.register(r'tickettypealias', TicketTypeAliasViewSet, base_name="tickettypealias")

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', serve ,{'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
]