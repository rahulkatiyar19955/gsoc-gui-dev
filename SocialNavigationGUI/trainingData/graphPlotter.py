import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
import os


fig, ax = plt.subplots()
ax.set_title('Click on legend line to toggle line on/off')
lines = []


def open_file(fileName):
    data = np.genfromtxt(fileName,delimiter=",", names=["initialPosX","initialPosZ","finalPosX","finalPosZ","RobotPoseX","RobotPoseZ","RobotPoseRot","MinObstacleAngle","MinObstacleDistance"])
    dataPlot, = ax.plot(data['RobotPoseX'], data['RobotPoseZ'],lw=2, label=fileName)
    lines.append(dataPlot)

def clearLines():
    for dataLine in lines:
        dataLine.set_visible(False)

def createMenu():
    menu = {}
    menu[1]="internal_Force"
    menu[2]="External_Force"
    menu[3]="Robot_Speed"
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


def onpick(event):
    # on the pick event, find the orig line corresponding to the
    # legend proxy line, and toggle the visibility
    legline = event.artist
    origline = lined[legline]
    vis = not origline.get_visible()
    origline.set_visible(vis)
    # Change the alpha on the line in the legend so we can see what lines
    # have been toggled
    if vis:
        legline.set_alpha(1.0)
    else:
        legline.set_alpha(0.2)
    fig.canvas.draw()

def func(evt):
    if leg.contains(evt):
        bbox = leg.get_bbox_to_anchor()
        bbox = Bbox.from_bounds(bbox.x0, bbox.y0+d[evt.button], bbox.width, bbox.height)
        tr = leg.axes.transAxes.inverted()
        leg.set_bbox_to_anchor(bbox.transformed(tr))
        fig.canvas.draw_idle()


selected = createMenu()

open_file('reference.csv')

# iterate over all file that are present in the directory
for file in os.listdir():
    if file[:10] == selected[:10]:
        open_file(file)


leg = ax.legend(loc='upper left',fancybox=True, shadow=True,bbox_to_anchor=(-0.15,0, 1, 1))
leg.get_frame().set_alpha(0.01)
lined = dict()
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(5)  # 5 pts tolerance
    lined[legline] = origline

# this will hide all the lines, and user can later click on the legend to view specific dataplots
# based on their intrest.
clearLines()

# pixels to scroll per mousewheel event
d = {"down" : 30, "up" : -30}


fig.canvas.mpl_connect('pick_event', onpick)
fig.canvas.mpl_connect("scroll_event", func)

plt.show()


