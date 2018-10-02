from django.test import TestCase, Client
from urllib.parse import quote
from django.urls import reverse
import chess
from . import utils


class TestFENUrl(TestCase):

  def setUp(self):
    self.fen1 = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    self.fen2 = \
        'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2'
    self.fen3 = '8/8/8/8/5R2/2pk4/5K2/8 b - - 0 1'
    self.fen_invalid = '7/8/8/8/8/rR6/8'
    self.fen1_encoded = quote(self.fen1)
    self.fen2_encoded = quote(self.fen2)
    self.fen3_encoded = quote(self.fen3)
    self.fen_invalid_encoded = quote(self.fen_invalid)

    self.uri_begin = '/api'
    self.uri_template = '{}/fen/{{}}.{{}}'.format(self.uri_begin)

  def test_fen_url_reverse(self):
    """django.urls.reverse should find matches"""
    url1 = reverse(
        'fen_url', kwargs=dict(fen_url_string=self.fen1, file_extension='png'))
    self.assertEqual(
        url1, self.uri_template.format(self.fen1_encoded, 'png'))
    url2 = reverse(
        'fen_url', kwargs=dict(fen_url_string=self.fen2, file_extension='jpg'))
    self.assertEqual(
        url2, self.uri_template.format(self.fen2_encoded, 'jpg'))
    url3 = reverse(
        'fen_url', kwargs=dict(fen_url_string=self.fen3, file_extension='svg'))
    self.assertEqual(
        url3, self.uri_template.format(self.fen3_encoded, 'svg'))

  def test_fen_code(self):
    """Should return 200 on valid fen and 400 on invalid"""
    c = Client()
    res_valid = c.get(self.uri_template.format(self.fen1, 'png'))
    self.assertEqual(res_valid.status_code, 200)
    res_invalid = c.get(self.uri_template.format(self.fen_invalid, 'png'))
    self.assertEqual(res_invalid.status_code, 400)

  def test_file_extensions(self):
    """Should return 200 on valid file extension and 404 on invalid"""
    c = Client()
    res_valid_list = []
    for ext in ('jpg', 'svg', 'png'):
      res_valid_list.append(
          c.get(self.uri_template.format(self.fen1, ext)).status_code)
    self.assertEqual(res_valid_list, [200, 200, 200])

    res_invalid_list = []
    for ext in ('jpge', 'html', 'php'):
      res_invalid_list.append(
          c.get(self.uri_template.format(self.fen1, ext)).status_code)
    self.assertEqual(res_invalid_list, [404, 404, 404])


class TestImageFromBoard(TestCase):
  def setUp(self):
    self.board = chess.Board()

  def test_invalid_extension(self):
    ext = 'asd'
    self.assertRaises(ValueError, utils.image_from_board, 
                      board=self.board, ext=ext)

  def test_svg(self):
      svg_image = utils.image_from_board(self.board, 'svg')
      self.assertEqual(type(svg_image), str)

  def test_png(self):
      png_image = utils.image_from_board(self.board, 'png')
      self.assertEqual(type(png_image), bytes)

  def test_jpg(self):
      jpg_image = utils.image_from_board(self.board, 'jpg')
      self.assertEqual(type(jpg_image), bytes)