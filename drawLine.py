import sys
from graphics import *

class ViewPort:
	def __init__(self,xVmin,yVmin,xVmax,yVmax):
		self.xVmin,self.yVmin,self.xVmax,self.yVmax  =xVmin,yVmin,xVmax,yVmax
	def __repr__(self): 
		return 'ViewPort(%s, %s, %s, %s)' % (self.xVmin,self.yVmin,self.xVmax,self.yVmax) 
	def init_view(self):
		
		win = GraphWin('ViewPort',800,800)
		win.setCoords(self.xVmin,self.yVmin,self.xVmax,self.yVmax)
		win.setBackground(color_rgb(44,44,44))
		t=Text(Point(0,0),'(0,0)')
		t.setSize(8)
		t.draw(win)
		t=Text(Point(self.xVmax,self.yVmax),'('+str(self.xVmax)+str(self.yVmax)+')')
		t.setSize(8)
		t.draw(win)
		for i in range(self.xVmin,self.xVmax):
			pt= Point(i,0)
			pt.draw(win)
			pt.setFill('blue')
		for i in range(self.yVmin,self.yVmax):
			pt= Point(0,i)
			pt.draw(win)	
			pt.setFill('blue')	
		return win
		
	
class Window:
	def __init__(self, xwmin,ywmin,xwmax,ywmax):
		self.xwmin,self.ywmin,self.xwmax,self.ywmax = xwmin,ywmin,xwmax,ywmax
	def __repr__(self): 
		return 'Window(%s, %s, %s, %s)' % (self.xwmin,self.ywmin,self.xwmax,self.ywmax) 
	def map_to(self,x_win,y_win,ViewPort):
					x_view = (x_win-self.xwmin)*(ViewPort.xVmax - ViewPort.xVmin)/(self.xwmax-self.xwmin)  + ViewPort.xVmin
					y_view = (y_win-self.ywmin)*(ViewPort.yVmax - ViewPort.yVmin)/(self.ywmax-self.ywmin)  + ViewPort.yVmin
					return int(x_view),int(y_view)


def bresenham(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0
    pixel=[]
    for x in range(dx + 1):
        pixel.append((x0 + x*xx + y*yx, y0 + x*xy + y*yy))
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy
    return pixel		          


def drawLine(win,color='red',x1=-1,y1=-1,x2=-1,y2=-1):
	if x2==x1==-1:
		x1,y1,x2,y2 = map(int,input('Enter Line\'s Endpoints <x1> <y1> <x2> <y2>  :').split())
	pixel=bresenham(x1,y1,x2,y2)
	for i in pixel:
		x,y= i
		win.plot(*i,color)
	return x1,y1,x2,y2

def main(win=None):
	
	if len(sys.argv[1:])!=4:
		exit(print('Wrong Number of Arguments','\nUsage :python3 drawLine.py <x1> <y1> <x2> <y2>'))
	if(input('Defualt viewPort is (-400 -400, 400 400). Change?(y/Y)')in ('y','Y')):
		x,y=map(int,input('viewPort\'s xMax yMax : ').split())
		new_view = ViewPort(-x,-y,x,y)
	else:
		new_view =ViewPort(-400,-400,400,400)
	if(input('Defualt Window is (-200 -200, 200 200). Change?(y/Y)')in ('y','Y')):
		x,y=map(int,input('Window\'s xMax yMax : ').split())
		new_win = Window(-x,-y,x,y)
	else:
		new_win = Window(-200,-200,200,200)

	x1,y1,x2,y2 = int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])	
	print('ViewPrt :',new_view)
	print("Window :",new_win)
	point_1 = new_win.map_to(x1,y1,new_view)
	point_2 = new_win.map_to(x2,y2,new_view)
	print("Given points after mapping to viewPort.. ",point_1,point_2)	
	win = new_view.init_view()	
	pixel=bresenham(*point_1,*point_2)
	for i in pixel:
		x,y= i
		win.plot(*i)
	input('Exit?')

if __name__ == "__main__" : 
	main()	
 
