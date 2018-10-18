import chess
from django.http import HttpResponse
from .utils import image_from_board, content_type_from_extension


def image_from_fen(request, fen_url_string: str, file_extension: str):
  try:
    board = chess.Board(fen=fen_url_string)
  except ValueError:
    return HttpResponse(status=400)
  content = image_from_board(board, file_extension)
  content_type = content_type_from_extension(file_extension)
  return HttpResponse(content=content, content_type=content_type)
