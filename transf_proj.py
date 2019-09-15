import numpy as np 
from PIL import Image

picture = Image.open(r"C:\Users\GitHub\graphic_comp\img\texture.jpg")
destination = Image.open(r"C:\Users\GitHub\graphic_comp\img\base.jpg")

def destinationCoordinates():
    with open(r"C:\Users\GitHub\graphic_comp\config\points.txt", "r+") as f:
        points = [[], [], [], []]
        i = 0
        data = f.readlines()
        for line in data:
            points[i] += [int(n) for n in line.strip().split(", ")]
            i += 1
        return points


def solveLinearSystem(x, y, p):
    # (x, y) = source image width, height in pixels
    # p = destination coordinates array [[x1, xy], [x2, y2], [x3,y3], [x4,y4]]
    A = [
            [0, 0, 1, 0, 0, 0, 0, 0, -p[0][0],        0,        0,        0],
            [x, 0, 1, 0, 0, 0, 0, 0,        0, -p[1][0],        0,        0],
            [x, y, 1, 0, 0, 0, 0, 0,        0,        0, -p[2][0],        0],
            [0, y, 1, 0, 0, 0, 0, 0,        0,        0,        0, -p[3][0]],
            [0, 0, 0, 0, 0, 1, 0, 0, -p[0][1],        0,        0,        0],
            [0, 0, 0, x, 0, 1, 0, 0,        0, -p[1][1],        0,        0],
            [0, 0, 0, x, y, 1, 0, 0,        0,        0, -p[2][1],        0],
            [0, 0, 0, 0, y, 1, 0, 0,        0,        0,        0, -p[3][1]],
            [0, 0, 0, 0, 0, 0, 0, 0,       -1,        0,        0,        0],
            [0, 0, 0, 0, 0, 0, x, 0,        0,       -1,        0,        0],
            [0, 0, 0, 0, 0, 0, x, y,        0,        0,       -1,        0],
            [0, 0, 0, 0, 0, 0, 0, y,        0,        0,        0,       -1]
        ]
    
    b = [0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1]
    return np.linalg.solve(A, b)


def projectiveTransformation(v):

    # v = array of projective transformation parameters
    T = np.array([
            [v[0], v[1], v[2]],
            [v[3], v[4], v[5]],
            [v[6], v[7],   1 ]
        ])
    return T
    
def backwardTransformation(T):
    return np.linalg.inv(T)



def replace():
    x_max, y_max = picture.size
    p = destinationCoordinates()
    v = solveLinearSystem(x_max -1, y_max -1, p)
    T = projectiveTransformation(v)
    
    for x in range(x_max -1):
        for y in range(y_max -1):
            s = [x, y, 1]
            d = T.dot(s)
            color = picture.getpixel((x, y))
            destination.putpixel( (int(round(d[0]/d[2])), int(round(d[1]/d[2]))), (color))
    
    destination.save(r"C:\Users\GitHub\graphic_comp\img\res1.jpg")

def backwardReplace():
    x_max, y_max = picture.size
    x_des, y_des = destination.size
    
    p = destinationCoordinates()
    v = solveLinearSystem(x_max -1, y_max -1, p)
    T = projectiveTransformation(v)
    H = backwardTransformation(T)
    
    for x in range(x_des -1):
        for y in range(y_des -1):
            s = [x, y, 1]
            d = H.dot(s)
            if(int(round(d[0]/d[2])) in range(x_max) and int(round(d[1]/d[2])) in range(y_max)):
                color = picture.getpixel((int(round(d[0]/d[2])), int(round(d[1]/d[2]))))
                destination.putpixel( (x, y), (color))
    
    destination.save(r"C:\Users\GitHub\graphic_comp\img\res2.jpg")

replace()
backwardReplace()