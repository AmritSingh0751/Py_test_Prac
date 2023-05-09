
class Rectange:
  def __init__(self, length,breadth):
    self.length = length
    self.breadth = breadth
    
  
  def rect_perimeter(self):
    return 2 * (self.length + self.breadth)
  



def test_perimeter():
  rect = Rectange(3,4)
  assert rect.rect_perimeter() == 14



  
