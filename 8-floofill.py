from drawLine import ViewPort,bresenham
import sys,random
sys.setrecursionlimit(2*10**8)
from graphics import *
'''
0 -1
50 50
100 0
150 50
200 0
250 50
250 150
-50 150
-50 50
'''
def boundaryFill(pixel,stack,filled,win,fillColor='red2'):
	while(stack!=[]):		
			x,y=stack.pop()
			if((x,y) not in pixel and (x,y) not in filled):
				r=random.randint(0,255)
				g=random.randint(0,255)
				b=random.randint(0,255)
				win.plot(x,y,color=color_rgb(r,g,b))
				stack+=[(x+1,y),(x,y+1),(x,y-1),(x-1,y)]
		
				if((x+1,y) not in pixel) and ((x,y+1) not in pixel):
					stack.append((x+1,y+1))
					
				if((x+1,y) not in pixel) and ((x,y-1) not in pixel):
					stack.append((x+1,y-1))
					
				if((x-1,y) not in pixel) and ((x,y-1) not in pixel):
					stack.append((x-1,y-1))
					
				if((x-1,y) not in pixel) and ((x,y+1) not in pixel):
					stack.append((x-1,y+1))
				filled.append((x,y))


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
	point = win.getMouse()
	stack=[(int(point.getX()),int(point.getY()))]		
	
	#Comment this line for just polygon
	boundaryFill(pixel_dict,stack,filled,win)	
	
	
	input('Exit?')	
if __name__=='__main__':
	main()				
