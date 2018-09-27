from django.urls import path, re_path
from . import views

urlpatterns = [
  re_path(
      r'^fen/(?P<fen_url_string>[^\.]{8,100})\.(?P<file_extension>[svjpng]{3})$',
      views.hello, name='fen_url'),
]
