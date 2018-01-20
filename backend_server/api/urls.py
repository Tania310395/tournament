"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from core import views as core_views
from tournament import views as tournament_views

urlpatterns = [
    url(r'^api/login$', core_views.login_view),
    url(r'^api/hello$', core_views.hello_view),
    url(r'^admin/', admin.site.urls),
    url(r'^api/signup$', core_views.signup_view),
    url(r'^api/tournaments$', tournament_views.home_view),
    url(r'^api/players/(?P<tour_id>[0-9]+)$', tournament_views.player_view),
    url(r'^api/playerdetails/(?P<tour_id>[0-9]+)$', tournament_views.player_details),
    #url(r'^api/tournaments$', tournament_views.tour_view),
    url(r'^api/tournaments/(?P<tour_id>[0-9]+)$', tournament_views.tour_status),
    url(r'^api/standings/(?P<tour_id>[0-9]+)$', tournament_views.standing_view),
    url(r'^api/swisspairing/(?P<tour_id>[0-9]+)$',
        tournament_views.swiss_pairing),
    url(r'^api/reset_db$', tournament_views.reset_db),
    url(r'^api/matchs/(?P<tour_id>[0-9]+)$', tournament_views.match_data),
    url(r'^api/reportmatch/(?P<tour_id>[0-9]+)/(?P<round_id>[0-9]+)$', tournament_views.report_match),
    url(r'^api/status/(?P<tour_id>[0-9]+)$', tournament_views.status_match),
    url(r'^api/round/(?P<tour_id>[0-9]+)$', tournament_views.round_view),
    url(r'^api/currentround/(?P<tour_id>[0-9]+)$', tournament_views.current_round)
]
