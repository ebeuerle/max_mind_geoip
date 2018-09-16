
class FileController(object):
     def __init__(self):
         return

     def read_file(self):
         f = open('access.log', 'r')
         x = f.read().splitlines()
         f.close()
         return x
