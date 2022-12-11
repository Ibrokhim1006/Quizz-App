from django.urls import path
from quizz_app.auth import *
from quizz_app.views import *

urlpatterns = [
    # urls authorization
    path('',sigin_in,name='sigin_in'),
    path('sigin_up/',sigin_up,name='sigin_up'),
    path('logout_user/',logout_user,name='logout_user'),

    # urls quizz app
    path('home_personal/',home,name='home_personal'),
    path('quizz/<int:id>/',quizz,name='quizz'),
]