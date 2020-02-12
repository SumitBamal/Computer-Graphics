from drawLine import main,ViewPort,bresenham,drawLine
from drawPolygon import drawPoly
INSIDE = 0  #0000 
LEFT = 1    #0001 
RIGHT = 2   #0010 
BOTTOM = 4  #0100 
TOP = 8     #1000 

def code_for(x,y,x_min,y_min,x_max,y_max):
	code = INSIDE 
	if x < x_min:      # to the left of rectangle 
		code |= LEFT 
	elif x > x_max:    # to the right of rectangle 
		code |= RIGHT 
	if y < y_min:      # below the rectangle 
		code |= BOTTOM 
	elif y > y_max:    # above the rectangle 
		code |= TOP 
	return code 

def cohenSutherlandClip(x1, y1, x2, y2,x_min,y_min,x_max,y_max): 
    code1 = code_for(x1, y1,x_min,y_min,x_max,y_max) 
    code2 = code_for(x2, y2,x_min,y_min,x_max,y_max) 
    accept = False
    while True: 
        if code1 == 0 and code2 == 0: 
            accept = True
            break
        elif (code1 & code2) != 0: 
            break
        else: 
            x = 1.0
            y = 1.0
            if code1 != 0: 
                code_out = code1 
            else: 
                code_out = code2 
            if code_out & TOP: 
                x = x1 + (x2 - x1) *(y_max - y1) / (y2 - y1) 
                y = y_max 
  
            elif code_out & BOTTOM: 
                x = x1 + (x2 - x1) *(y_min - y1) / (y2 - y1) 
                y = y_min 
  
            elif code_out & RIGHT: 
                y = y1 + (y2 - y1) *(x_max - x1) / (x2 - x1) 
                x = x_max 
  
            elif code_out & LEFT: 
                y = y1 + (y2 - y1) *(x_min - x1) / (x2 - x1) 
                x = x_min 
            if code_out == code1: 
                x1 = x 
                y1 = y 
                code1 = code_for(x1,y1,x_min,y_min,x_max,y_max) 
  
            else: 
                x2 = x 
                y2 = y 
                code2 = code_for(x2, y2,x_min,y_min,x_max,y_max) 
  
    if accept:
    	return  int(x1),int(y1),int(x2),int(y2)
    else: 
        print("Line rejected") 
        
        
def main():
    if(input('Defualt viewPort is (-400 -400, 400 400). Change?(y/Y)')in ('y','Y')):
        x,y=map(int,input('viewPort\'s xMax yMax : ').split())
        new_view = ViewPort(-x,-y,x,y)
    else:
        new_view =ViewPort(-400,-400,400,400)	
    print('ViewPort :',new_view)

    win = new_view.init_view()
    x,y,x1,y1 =drawLine(win)
    xmin,ymin,xmax,ymax = map(int,input('Enter Cliping Window\'s Endpoints <xmin> <ymin> <xmax> <ymax>  :').split())
    drawPoly([(xmin,ymin),(xmax,ymin),(xmax,ymax),(xmin,ymax)],win)

    temp = cohenSutherlandClip(x,y,x1,y1,xmin,ymin,xmax,ymax)   
    if not temp:return
    pixel = bresenham(*temp)	
    for i in pixel:
        x,y= i
        win.plot(*i,'green')
    input('Exit?')	
if __name__=='__main__':
	main()

