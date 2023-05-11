import  pytest
class Rectange:
  def __init__(self, length,breadth):
    self.length = length
    self.breadth = breadth

  def rect_perimeter(self):
    return 2 * (self.length + self.breadth)
  

# def test_perimeter():
#   rect = Rectange(3,4)
#   assert rect.rect_perimeter() == 14

# @pytest.mark.parametrize("x,y,z",[(2,2,4),(3,4,5)])
# def test_add(x,y,z):
#   assert x +y == z

@pytest.fixture
def fx():
  print('In fixture setup')

def test_fixt1(fx):
  print("In Test")
  assert 4 == 4

  
