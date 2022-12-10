# def punit():
#     x = input.store()
#     print(x)
def makemydir(whatever):
  try:
    os.makedirs(whatever)
  except OSError:
    pass