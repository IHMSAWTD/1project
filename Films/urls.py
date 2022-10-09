from django.conf.urls.static import static
from django.urls import path
from Films.views import *
from django.conf import settings
urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path("watch/<int:film_id>/", watch, name='watch'),
    path('watch/', wotch, name='wotch'),
    path('register/', register, name='register'),
    path('login/', LoginUser, name='login'),
    path('logout/',LogoutUser,name='logout'),
    path('category/<int:category_id>',search_category,name = 'category'),
    path('test',FilmsByCassssssssssstegories.as_view(),name = 'watch')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)