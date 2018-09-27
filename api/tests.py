from django.test import TestCase
from urllib.parse import quote
from django.urls import reverse


class TestFENUrl(TestCase):

  def setUp(self):
    self.fen1 = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    self.fen2 = \
        'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2'
    self.fen3 = '8/8/8/8/5R2/2pk4/5K2/8 b - - 0 1'
    self.fen1_encoded = quote(self.fen1)
    self.fen2_encoded = quote(self.fen2)
    self.fen3_encoded = quote(self.fen3)

    self.uri_begin = '/api'

  def test_fen_url_reverse(self):
    """django.urls.reverse should find matches"""
    url1 = reverse(
        'fen_url', kwargs=dict(fen_url_string=self.fen1, file_extension='png'))
    self.assertEqual(
        url1, '{}/fen/{}.png'.format(self.uri_begin, self.fen1_encoded))
    url2 = reverse(
        'fen_url', kwargs=dict(fen_url_string=self.fen2, file_extension='jpg'))
    self.assertEqual(
        url2, '{}/fen/{}.jpg'.format(self.uri_begin, self.fen2_encoded))
    url3 = reverse(
        'fen_url', kwargs=dict(fen_url_string=self.fen3, file_extension='svg'))
    self.assertEqual(
        url3, '{}/fen/{}.svg'.format(self.uri_begin, self.fen3_encoded))
