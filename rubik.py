import torch

"""
An order-3 tensor representing a solved Rubik's cube.

You can imagine it as if the Rubik's cube is sitting on a table and we're 
looking at it top-down. The first matrix are the 9 blocks we can see.
The second matrix is the next layer down, and the third matrix is the
layer of blocks closest to the table. 

"""
RUBIKS_CUBE = torch.tensor([[[1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9]],
                    
                            [[10, 11, 12],
                             [13, 0, 14],
                             [15, 16, 17]],
                    
                            [[18, 19, 20],
                             [21, 22, 23],
                             [24, 25, 26]]])

def encode(rubik):
    """
    Takes a Rubik's cube (order-3 tensor) and turns it into a string 
    by "reading" each block (starting from the top layer) as the kth 
    letter of the alphabet. Conveniently, there are exactly 26 blocks that 
    we'll ever see (since the middle block always remains in the middle of
    the Rubik's cube). When encoding, ignore the middle block (with 
    the value 0).
    
    e.g. encode(RUBIKS_CUBE) = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    """
    raise NotImplementedError('Exercise 1.')


def flip_away(rubik):
    """
    Takes a Rubik's cube (order-3 tensor) and "flips" the Rubik's cube away
    from us (assuming we're looking at it top-down, sitting on a table), so
    that the blocks we now see are the blocks we would have seen by crouching
    down and looking at the cube from the front.
    
    Immutable operation -- this should return a new tensor that looks like
    the original Rubik's cube after flipping it away. It should not modify the
    input tensor.
    
    """
    raise NotImplementedError('Exercise 2.')


def twist_right(rubik):
    """
    Takes a Rubik's cube (order-3 tensor) and "twists" the top layer of the
    Rubik's cube (assuming we're looking at it top-down, sitting on a table)
    clockwise 90 degrees.
    
    Immutable operation -- this should return a new tensor that looks like
    the original Rubik's cube after doing the twist right operation. It 
    should not modify the input tensor.
    
    """
    raise NotImplementedError('Exercise 3.')


def rotate_right(rubik):
    """
    Takes a Rubik's cube (order-3 tensor) and rotates it (assuming we're 
    looking at it top-down, sitting on a table) clockwise 90 degrees.
    
    Immutable operation -- this should return a new tensor that looks like
    the original Rubik's cube after doing the rotate right operation. It 
    should not modify the input tensor.
    
    """
    raise NotImplementedError('Exercise 4.')


def answer():
    """
    Once the above functions are correctly implemented, this should return
    a secret password.
    
    """
    operations = [flip_away, rotate_right, rotate_right, rotate_right, 
                  twist_right, twist_right, twist_right, twist_right, 
                  rotate_right, flip_away]
    result = RUBIKS_CUBE
    for op in operations:
        result = op(result)
    return encode(result)[7:11]
              

