from django.views.generic import TemplateView
from django.urls import path, include 
from sentimentAnalysis import views as SV
from userAuth import views as UV
urlpatterns = [

    path('',UV.home,name="home"),
    path('analyze/', SV.senti_analyse.as_view()),
    path('record/', SV.getsentirecord.as_view()),
    path('create-user/', UV.UserView.as_view()),
    path('get-user/', UV.UserLoginView.as_view()),
    path('login-user/', UV.UserLoginView.as_view()),
    path('chat/',SV.chatbot.as_view())
]



    # path('accounts/', include('allauth.urls')),