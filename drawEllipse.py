from drawLine import Window,ViewPort
import sys


def bresenham_for_ellipse(rx,ry,xc,yc):  
	pixels =[]
	x = 0  
	y = ry  
	d1 = ((ry * ry) - (rx * rx * ry) + (0.25 * rx * rx))  
	dx = 2 * ry * ry * x  
	dy = 2 * rx * rx * y  

	while (dx < dy):  
		pixels +=[(x+xc,y+yc),(-x+xc,y+yc),(x+xc,-y+yc),(-x+xc,-y+yc)]
		if (d1 < 0):  
		    x += 1
		    dx = dx + (2 * ry * ry)  
		    d1 = d1 + dx + (ry * ry)  
		else: 
		    x += 1  
		    y -= 1
		    dx = dx + (2 * ry * ry)  
		    dy = dy - (2 * rx * rx)
		    d1 = d1 + dx - dy + (ry * ry)  

	d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +((rx * rx) * ((y - 1) * (y - 1))) - (rx * rx * ry * ry));  

	while (y >= 0): 
		pixels +=[(x+xc,y+yc),(-x+xc,y+yc),(x+xc,-y+yc),(-x+xc,-y+yc)] 
		if (d2 > 0): 
		    y -= 1
		    dy = dy - (2 * rx * rx)  
		    d2 = d2 + (rx * rx) - dy  
		else: 
		    y -= 1  
		    x += 1
		    dx = dx + (2 * ry * ry)  
		    dy = dy - (2 * rx * rx)
		    d2 = d2 + dx - dy + (rx * rx)  
	return pixels	    
def main():
    if len(sys.argv[1:])!=4:
        exit(print('Wrong Number of Arguments','\nUsage :python3 drawEllipse.py <xc> <yc> <rx> <ry>'))
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
    x1,y1,rx,ry = int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])      
    print('ViewPort :',new_view)
    print("Window :",new_win)
    x,y = new_win.map_to(x1,y1,new_view)
    _,yr = new_win.map_to(x1,y1+ry,new_view)
    ry=yr - y
    xr,_=new_win.map_to(x1+rx,y1,new_view)
    rx =xr-x 
    print("Given points(xc,yc) and radius(rx,ry) after mapping to viewPort.. ",x,y,rx,ry)	
    win = new_view.init_view()	
    pixel=bresenham_for_ellipse(rx,ry,x,y)
    for i in pixel:
        x,y= i
        win.plot(*i)
    input('Exit?')


if __name__ == "__main__" : 
	main()

            
            
