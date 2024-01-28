import torch
import unittest
from rubik import encode, twist_right, rotate_right, flip_away, RUBIKS_CUBE

class Q1(unittest.TestCase):

    def test_encode(self):
        expected = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
        assert encode(RUBIKS_CUBE) == expected, 'encode test failed!'

class Q2(unittest.TestCase):

    def test_flip_away(self):
        desired_result = torch.tensor([[[ 7,  8,  9],
                                        [15, 16, 17],
                                        [24, 25, 26]],
        
                                       [[ 4,  5,  6],
                                        [13,  0, 14],
                                        [21, 22, 23]],
        
                                       [[ 1,  2,  3],
                                        [10, 11, 12],
                                        [18, 19, 20]]])
        assert encode(flip_away(RUBIKS_CUBE)) == encode(desired_result), 'flip away test failed!'

    def test_flip_away_immutability(self):
        flipped = flip_away(RUBIKS_CUBE)
        flipped[0][0][0] = 22
        assert encode(RUBIKS_CUBE) == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'flip away immutability test failed!'

    def test_flip_away_composability(self):
        desired_result = torch.tensor([[[24, 25, 26],
                                        [21, 22, 23],
                                        [18, 19, 20]],

                                       [[15, 16, 17],
                                        [13,  0, 14],
                                        [10, 11, 12]],

                                       [[ 7,  8,  9],
                                        [ 4,  5,  6],
                                        [ 1,  2,  3]]])
        assert encode(flip_away(flip_away(RUBIKS_CUBE))) == encode(desired_result), 'flip away composability test failed!'
        assert encode(RUBIKS_CUBE) == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'flip away composability test failed!'




class Q3(unittest.TestCase):

    def test_twist_right(self):
        desired_result = torch.tensor([[[ 7,  4,  1],
                                        [ 8,  5,  2],
                                        [ 9,  6,  3]],
        
                                       [[10, 11, 12],
                                        [13,  0, 14],
                                        [15, 16, 17]],
        
                                       [[18, 19, 20],
                                        [21, 22, 23],
                                        [24, 25, 26]]])
        assert encode(twist_right(RUBIKS_CUBE)) == encode(desired_result), 'twist right test failed!'

    def test_twist_right_immutability(self):
        flipped = twist_right(RUBIKS_CUBE)
        flipped[0][0][0] = 22
        assert encode(RUBIKS_CUBE) == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'twist right immutability test failed!'

    def test_twist_right_composability(self):
        desired_result = torch.tensor([[[ 9,  8,  7],
                                        [ 6,  5,  4],
                                        [ 3,  2,  1]],
        
                                       [[10, 11, 12],
                                        [13,  0, 14],
                                        [15, 16, 17]],
        
                                       [[18, 19, 20],
                                        [21, 22, 23],
                                        [24, 25, 26]]])
        assert encode(twist_right(twist_right(RUBIKS_CUBE))) == encode(desired_result), 'twist right composability test failed!'
        assert encode(RUBIKS_CUBE) == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'twist right composability test failed!'


class Q4(unittest.TestCase):

    def test_rotate_right(self):
        desired_result = torch.tensor( [[[ 7,  4,  1],
                                         [ 8,  5,  2],
                                         [ 9,  6,  3]],
                                
                                        [[15, 13, 10],
                                         [16,  0, 11],
                                         [17, 14, 12]],
                                
                                        [[24, 21, 18],
                                         [25, 22, 19],
                                         [26, 23, 20]]])
        assert encode(rotate_right(RUBIKS_CUBE)) == encode(desired_result), 'rotate right test failed!'

    def test_rotate_right_immutability(self):
        flipped = rotate_right(RUBIKS_CUBE)
        flipped[0][0][0] = 22
        assert encode(RUBIKS_CUBE) == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'rotate right immutability test failed!'

    def test_rotate_right_composability(self):
        desired_result = torch.tensor([[[ 9,  8,  7],
                                        [ 6,  5,  4],
                                        [ 3,  2,  1]],

                                       [[17, 16, 15],
                                        [14,  0, 13],
                                        [12, 11, 10]],

                                       [[26, 25, 24],
                                        [23, 22, 21],
                                        [20, 19, 18]]])
        assert encode(rotate_right(rotate_right(RUBIKS_CUBE))) == encode(desired_result), 'rotate right composability test failed!'
        assert encode(RUBIKS_CUBE) == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'rotate right composability test failed!'


if __name__ == "__main__":
    unittest.main() # run all tests