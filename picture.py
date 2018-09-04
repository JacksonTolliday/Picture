"""
picture.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
clear = Color(0xffffff, 0.0)
brown = Color(0x6E2c00, 1.0)

thinline = LineStyle(1, black)
thickline = LineStyle(5, black)
noline = LineStyle(1, clear)

base = RectangleAsset(40, 50, thinline, brown)
leaf = PolygonAsset([(0,0), (100,-75), (200,0), (0,0)], noline, green)
leaf2 = PolygonAsset([(0,0), (150,-100), (300,0), (0,0)], noline, green)
apple = CircleAsset(10, thinline, red)

Sprite(apple)

# add your code here /\  /\  /\


myapp = App()
myapp.run()
