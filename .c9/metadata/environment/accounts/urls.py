{"filter":false,"title":"urls.py","tooltip":"/accounts/urls.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["from django.conf.urls import url, include","from accounts.views import logout, login, registration, user_profile","from accounts import url_reset","","urlpatterns = [","    url(r'^logout/', logout, name=\"logout\"),","    url(r'^login/', login, name=\"login\"),","    url(r'^register/', registration, name=\"registration\"),","    url(r'^profile/', user_profile, name=\"profile\"),","    url(r'^password-reset/', include(url_reset))","]"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":1},"end":{"row":10,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1562073745200,"hash":"6dae2d85a62c56bb69494b829e02c662c83c7df6"}