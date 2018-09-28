from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FENStringConverter, 'fen')
register_converter(converters.FileExtensionConverter, 'fext')


urlpatterns = [
    path('fen/<fen:fen_url_string>.<fext:file_extension>',
         views.image_from_fen, name='fen_url'),
]
