import sys
import math

def subtract(p1, p2):
    return [p1[0] - p2[0], p1[1] - p2[1]]

def lineCross(aP1, aP2, bP1, bP2):
    dA = subtract(aP2, aP1)
    dB = subtract(bP2, bP1)
    CompareA = dA[0]*aP1[1] - dA[1]*aP1[0]
    CompareB = dB[0]*bP1[1] - dB[1]*bP1[0]
    return (((dA[0]*bP1[1] - dA[1]*bP1[0]) < CompareA) ^ ((dA[0]*bP2[1] - dA[1]*bP2[0]) < CompareA)) and (((dB[0]*aP1[1] - dB[1]*aP1[0]) < CompareB) ^ ((dB[0]*aP2[1] - dB[1]*aP2[0]) < CompareB) )

def lineTouch(aP1, aP2, bP1, bP2):
    dA = subtract(aP2, aP1)
    dB = subtract(bP2, bP1)
    CompareA = dA[0]*aP1[1] - dA[1]*aP1[0]
    CompareB = dB[0]*bP1[1] - dB[1]*bP1[0]
    return (((dA[0]*bP1[1] - dA[1]*bP1[0]) <= CompareA) ^ ((dA[0]*bP2[1] - dA[1]*bP2[0]) <= CompareA)) and (((dB[0]*aP1[1] - dB[1]*aP1[0]) <= CompareB) ^ ((dB[0]*aP2[1] - dB[1]*aP2[0]) <= CompareB) )


def project(p1, p2, t):
    if p2[0] == p1[0]:
#        Vertical Line
        return [p1[0], t[1]]
    m = 1.0*(p2[1] - p1[1]) / (p2[0] - p1[0])
    b = 1.0* p1[1] - (m * p1[0])
    x = (m * t[1] + t[0] - m * b) / (m * m + 1)
    y = (m * m * t[1] + m * t[0] + b) / (m * m + 1)
    return [x, y]

def normalize(v):
    mag = math.sqrt(v[0]* v[0] + v[1]*v[1])
    if mag == 0:
        return [0, 0]
    return [v[0]/mag, v[1]/mag]

def planeTest(l1, l2, t1, t2):
    v1 = normalize(subtract(project(l1, l2, t1), t1))
    v2 = normalize(subtract(project(l1, l2, t2), t2))
#    print(v1, v2)
    diff = subtract(v1, v2)
    mag = math.sqrt(diff[0] * diff[0] + diff[1] * diff[1])
    return mag < 1.001

def containsOrigin(tri):
    p1 = [tri[0], tri[1]]
    p2 = [tri[2], tri[3]]
    p3 = [tri[4], tri[5]]
    origin = [0,0]
#    intersections = 0
#    if lineCross([tri[0], tri[1]], [tri[2], tri[3]], [0, 0], [0, 1001]):
#        intersections += 1
#    if lineCross([tri[0], tri[1]], [tri[4], tri[5]], [0, 0], [0, 1001]):
#        intersections += 1
#    if lineCross([tri[4], tri[5]], [tri[2], tri[3]], [0, 0], [0, 1001]):
#        intersections += 1
#    return intersections == 1
    if not planeTest(p1, p2, p3, origin):
        return False
    if not planeTest(p1, p3, p2, origin):
        return False
    if not planeTest(p2, p3, p1, origin):
        return False
    return True

def readFile():
    count = 0
    with open("./triangles.txt") as file:
        for line in file:
            coords = [int(x) for x in line.strip().split(",")]
            if containsOrigin(coords):
                count += 1
    return count

def main(argv):
    print("RETURN ", readFile())
#    print(lineCross([-100, 0], [100, 0], [0, 0], [0, 1001]))
#A(-340,495), B(-153,-910), C(835,-947)
#X(-175,41), Y(-421,-714), Z(574,-645)
    print(containsOrigin([0, 0, 1, 0, 0, 1]))
    print(containsOrigin([-1, 0, 1, 0, 1, 1]))
    print(containsOrigin([-340,495,-153,-910,835,-947]))
    print(containsOrigin([-175,41,-421,-714,574,-645]))
#    print(lineCross([-100, 0], [100, 0], [0, 0], [0, 1001]))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
