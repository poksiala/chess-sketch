import chess
import chess.svg
from cairosvg import svg2png


def svg_from_board(board: chess.Board, **board_options):
  return chess.svg.board(board=board, **board_options)


def png_from_board(board: chess.Board, **board_options):
  svg = svg_from_board(board, **board_options)
  return svg2png(bytestring=svg)


def jpg_from_board(board: chess.Board, **board_options):
  pass


def image_from_board(board: chess.Board, ext: str, **board_options):
  if ext == 'svg':
    return svg_from_board(board, **board_options) 
  elif ext == 'jpg':
    return jpg_from_board(board, **board_options)
  elif ext == 'png':
    return png_from_board(board, **board_options)
  else:
    raise ValueError('Unsupported file extension `{}`'.format(ext))


def content_type_from_extension(ext: str) -> str:
  if ext == 'svg':
    return 'image/svg+xml'
  elif ext == 'jpg':
    return 'image/jpg'
  elif ext == 'png':
    return 'image/png'
  else:
    raise ValueError('Unsupported file extension `{}`'.format(ext))
    