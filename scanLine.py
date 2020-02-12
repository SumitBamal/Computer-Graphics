from drawLine import ViewPort,bresenham
import sys,random,math
from collections import defaultdict as dd
sys.setrecursionlimit(2*10**8)
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
def scanLine(edge_table,y_min,y_max,win):
	active_edge = []
	for curr_y in range(y_min,y_max+1):
		i=0
		#Del used
		while i<len(active_edge):
			if active_edge[i][2]==curr_y:
				active_edge.pop(i)
			else:
				i+=1
		#update x
		for e in range(len(active_edge)):
			if e%2: active_edge[e][1]+=active_edge[e][3];active_edge[e][0]=math.floor(active_edge[e][1]);
			else:	 active_edge[e][1]+=active_edge[e][3];active_edge[e][0]=math.ceil(active_edge[e][1]);
		#Add New
		active_edge+=edge_table[curr_y]
		active_edge.sort()
		#print(active_edge)
		#Fill all
		for cur in range(0,len(active_edge)-1,2):
			for x in range(active_edge[cur][0],active_edge[cur+1][0]+1):
				r=random.randint(0,255)
				g=random.randint(0,255)
				b=random.randint(0,255)
				win.plot(x,curr_y,color=color_rgb(r,g,b))
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
	
	vert+=[vert[0]]
	win = new_view.init_view()
	edge_table =dd(list)
	for i in range(len(vert)-1):
		#Edge table
		x,y,x1,y1 =*vert[i],*vert[i+1]
		if y>y1:
			x,y,x1,y1 =x1,y1,x,y 
		if y==y1:
			continue
		if x1==x:
			slope_inv = 0
		else:	
			slope_inv = (x1-x)/(y1-y)
				 
		edge_table[y].append([x,x,y1,slope_inv])
	#edge_table.sort()

	y_max = max(v[1] for v in vert)
	y_min = min(v[1] for v in vert)
	
	scanLine(edge_table,y_min,y_max,win)	
	
	
	input('Exit?')	
if __name__=='__main__':
	main()				
