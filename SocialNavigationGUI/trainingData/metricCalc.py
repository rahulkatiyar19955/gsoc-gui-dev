import matplotlib.pyplot as plt
import numpy as np
import os

pathLengthList = dict()
angleCummulative = dict()

def pathLengthSorted():
    print("\n\n####  pathLengthSorted ####")
    sort_orders = sorted(pathLengthList.items(), key=lambda x: x[1])
    for pl in sort_orders:
        print(pl[0],pl[1])

def pathSmoothnessSorted():
    print("\n\n####  pathSmoothnessSorted ####")
    sort_orders = sorted(angleCummulative.items(), key=lambda x: x[1])
    for pl in sort_orders:
        print(pl[0],pl[1])

def dist(x1,y1,x2,y2):
    if x1==None:
        return 0
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def getPathLength(x,y):
    distSum=0
    for index in range(1,len(x)-1):
        distSum += dist(x[index],y[index],x[index+1],y[index+1])
    return distSum

def getCummalativeAngle(angle):
    cumm_angle=0
    # converting the range into -pi <-> +pi  that is -3.14 <-> +3.14
    for index in range(1,len(angle)-1):
        temp_angle1 = angle[index] - 1.57
        temp_angle2 = angle[index+1] - 1.57
        diff_angle = abs(temp_angle1 - temp_angle2)
        if (diff_angle > 3.14):
            diff_angle = 6.28 - diff_angle

        cumm_angle += diff_angle
    return cumm_angle/len(angle)

def open_file(fileName):
    data = np.genfromtxt(fileName,delimiter=",", names=["initialPosX","initialPosZ","finalPosX","finalPosZ","RobotPoseX","RobotPoseZ","RobotPoseRot","MinObstacleAngle","MinObstacleDistance"])
    # plt.plot(data['RobotPoseX'], data['RobotPoseZ'])
    # plt.axis('equal')
    pl= getPathLength(data['RobotPoseX'], data['RobotPoseZ'])
    pathLengthList[fileName]=pl
    an = getCummalativeAngle(data['RobotPoseRot'])
    angleCummulative[fileName] = an
    # print(fileName,pl)

def createMenu():
    menu = {}
    menu[1]="internal_Force"
    menu[2]="External_Force"
    menu[3]="Robot_Speed"
    menu[4]="IF_Graph"
    menu[5]="EF_Graph"
    while True:
        options=list(menu.keys())
        options.sort()
        for entry in options:
          print(entry, menu[entry])

        selection=int(input("Please Select:"))
        try:
            return menu[selection]
        except Exception as e:
            print("unknown entry")


selected = createMenu()

open_file('reference.csv')

for file in os.listdir():
    if file[:10] == selected[:10]:
        open_file(file)

# plt.show()
# print(pathLengthList)
pathLengthSorted()
pathSmoothnessSorted()
print("over")
