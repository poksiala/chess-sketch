import chess
import cairosvg
from django.shortcuts import render
from django.http import HttpResponse



def image_from_fen(request, fen_url_string: str, file_extension: str):
  try:
    board = chess.Board(fen=fen_url_string)
  except ValueError:
    return HttpResponse(status=400)
  return HttpResponse(status=200)
