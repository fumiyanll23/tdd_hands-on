import pytest

from .calc import add
from .calc import mul

@pytest.mark.parametrize('x, y, expected',[
  (2, 3, 5),
  ('Hello', 'World', 'Hello World'),
])
def test_add(x, y, expected):
  assert add(x, y) == expected

@pytest.mark.parametrize('x, y, expected', [
  (2, 3, 6),
  ('Hello', 3, 'HelloHelloHello'),
  ('World', 1.0, ''),
  ('hogehoge', 0, ''),
])
def test_mul(x, y, expected):
  assert mul(x, y) == expected
