python
from Main1 import rectangle_area

def test_rectangle_area():
    assert rectangle_area(5, 3) == 15, "Area of rectangle with length 5 and width 3 should be 15"

if __name__ == '__main__':
    test_rectangle_area()
    print("✓ Test passed!")
