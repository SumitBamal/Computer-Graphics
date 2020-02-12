from drawLine import ViewPort,bresenham,drawLine
import sys,random
from graphics import *
'''
100 100
50 0
100 -100
0 -50
-100 -100
-50 0
-100 100
0 50
'''
def drawPoly(vert,win,color='white'):
	vert+=[vert[0]]
	for i in range(len(vert)-1):
		x1,y1,x2,y2 = *vert[i],*vert[i+1]
		print(win,color,x1,y1,x2,y2)
		drawLine(win,color,x1,y1,x2,y2)

def main():
	vert = []
	
	while(1):
		try:
			x,y=map(int,input('Next vert?').split())
			vert.append((x,y))
		except:
			print(vert)
			break
	if(input('Defualt viewPort is (-400 -400, 400 400). Change?(y/Y)')in ('y','Y')):
		x,y=map(int,input('viewPort\'s xMax yMax : ').split())
		new_view = ViewPort(-x,-y,x,y)
	else:
		new_view =ViewPort(-400,-400,400,400)	
	print('ViewPort :',new_view)
	
	pixel = []
	filled= []
	pixel_dict={}
	vert+=[vert[0]]
	win = new_view.init_view()
	
	for i in range(len(vert)-1):
		pixel+=bresenham(*vert[i],*vert[i+1])

	for i in pixel:
		x,y= i
		win.plot(*i)
		pixel_dict[(x,y)]=1
	stack=[(0,0)]	

	
	input('Exit?')	
if __name__=='__main__':
	main()				
