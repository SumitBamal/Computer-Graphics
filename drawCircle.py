from drawLine import ViewPort,Window
import sys
def drawCircle(xc,yc,x,y):
	return [(xc+x,yc+y),(xc-x,yc+y),(xc+x,yc-y),(xc-x,yc-y),(xc+y,yc+x),(xc-y,yc+x),(xc+y,yc-x),(xc-y,yc-x)]

def bresenham(xc,yc,r):
    pixels = []
    x = 0
    y = r 
    d = 3 - 2 * r
    pixels+=drawCircle(xc, yc, x, y)
    while (y >= x): 
        x+=1;  
        if (d > 0): 
            y-=1
            d = d + 4 * (x - y) + 10; 
        else:
            d = d + 4 * x + 6; 
        pixels+=drawCircle(xc, yc, x, y)
    return pixels


def main():
    if len(sys.argv[1:])!=3:
        exit(print('Wrong Number of Arguments','\nUsage :python3 drawCircle.py <xc> <yc> <r>'))
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
    x1,y1,r = int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])   
    print('ViewPort :',new_view)
    print("Window :",new_win)
    x,y = new_win.map_to(x1,y1,new_view)
    _,y_r = new_win.map_to(x1,y1+r,new_view)
    r=y_r - y
    print("Given points after mapping to viewPort.. ",x,y,r)	
    win = new_view.init_view()	
    pixel=bresenham(x,y,r)
    for i in pixel:
        x,y= i
        win.plot(*i)
    input('Exit?')

if __name__ == "__main__" : 
	main()	    
