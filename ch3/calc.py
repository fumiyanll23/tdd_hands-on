def add(x, y):
  if isinstance(x, str) and isinstance(y, str):
    return x + ' ' + y
  elif isinstance(x, int) and isinstance(y, int):
    return x + y
  else:
    raise(ValueError)

def sub(x, y):
  return x - y

def mul(x, y):
  if isinstance(y, int):
    return x * y
  elif not(isinstance(y, int)) or y<=0:
    return ''
