from .calc import add
from .calc import sub

def test_add():
  assert add(2, 3) == 5
  assert add(1, 100) == 101
  assert sub(4, 2) == 2
