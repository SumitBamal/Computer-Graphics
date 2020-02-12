from drawLine import main,ViewPort,bresenham,drawLine
from drawPolygon import drawPoly
global t1,t2
t1=0
t2=1
def isClip(p,q):
    global t1,t2
    flag = 1
    if p<0:
        r = q / p
        if r>t2:
            flag = 0
        elif r>t1:
            t1 = r
    elif p>0:
        r=q/p
        if r<t1:
            flag = 0
        else:
            t2 = r
    elif q < 0:
        flag = 0
    return flag
def clip(x1,y1,x2,y2, bxmin , bymin , bxmax , bymax):
    global  t1 , t2
    dx = x2 - x1
    if(isClip(-dx,y1-bymin)):
        if isClip(dx,bxmax-x1):
            dy=y2-y1
            if(isClip(-dy,y1-bymin)):
                if(isClip(dy,bymax-y1)):
                    if t2<1:
                        x2 = x1 + t2 * dx
                        y2 = y1 + t2 * dy
                    if t1>0:
                        x1 += t1 * dx 
                        y1 += t1 * dy
    
    return list(map(int,[x1,y1,x2,y2]))

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
    temp = clip(x,y,x1,y1,xmin,ymin,xmax,ymax)
    print(temp,x,y,x1,y1,xmin,ymin,xmax,ymax)
    if not temp:return
    pixel = bresenham(*temp)	
    for i in pixel:
        x,y= i
        win.plot(*i,'green')
    input('Exit?')	
if __name__=='__main__':
    main()
