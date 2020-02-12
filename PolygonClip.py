from drawLine import main,ViewPort,bresenham,drawLine
from drawPolygon import drawPoly
'''
---poly V
100 150
200 250
300 200
---cliper V
100 300
300 300
200 100
'''
def x_intersect(x1,y1,x2,y2, x3,y3,x4,y4) :

    num = (x1*y2 - y1*x2) * (x3-x4) - (x1-x2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    return num//den

def y_intersect(x1,y1,x2,y2, x3,y3,x4,y4):  
    num = (x1*y2 - y1*x2) * (y3-y4) - (y1-y2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    return num//den

  
def clip(poly_points, x1,y1,x2,y2): 

    new_points =[]
    for i in range(len(poly_points)):
        k = (i+1) % len(poly_points)
        ix = poly_points[i][0]
        iy = poly_points[i][1]
        kx = poly_points[k][0]
        ky = poly_points[k][1] 

        i_pos = (x2-x1) * (iy-y1) - (y2-y1) * (ix-x1); 
        k_pos = (x2-x1) * (ky-y1) - (y2-y1) * (kx-x1); 
  
        if i_pos < 0  and k_pos < 0 :
            new_points.append((kx,ky))
        elif i_pos >= 0 and k_pos < 0 :
            new_points.append((x_intersect(x1, y1, x2, y2, ix, iy, kx, ky),y_intersect(x1, y1, x2, y2, ix, iy, kx, ky)))
            new_points.append((kx,ky))
        elif i_pos < 0 and k_pos >= 0: 
            new_points.append((x_intersect(x1,y1, x2, y2, ix, iy, kx, ky),y_intersect(x1,y1, x2, y2, ix, iy, kx, ky)))
    return new_points
  
def PolyClip(poly_points, clipper_points):  
    for i in range(len(clipper_points)):
        k = (i+1) % len(clipper_points) 

        poly_points= clip(poly_points, clipper_points[i][0],clipper_points[i][1], clipper_points[k][0], clipper_points[k][1]); 
    return poly_points
    

def main():
    if(input('Defualt viewPort is (-400 -400, 400 400). Change?(y/Y)')in ('y','Y')):
        x,y=map(int,input('viewPort\'s xMax yMax : ').split())
        new_view = ViewPort(-x,-y,x,y)
    else:
        new_view =ViewPort(-400,-400,400,400)	
        print('ViewPort :',new_view)
        
    win = new_view.init_view()
    print('Enter vertices of Clipping Window')
    clipw=[]
    while(1):
        try:
            x,y=map(int,input('Next vert(N)?').split())
            clipw.append((x,y))
        except:
            print(clipw)
            break
    
    vert = []
    print('Enter Polygon to be clipped-')
    while(1):
        try:
            x,y=map(int,input('Next vert(N)?').split())
            vert.append((x,y))
        except:
            print(vert)
            break
    temp = PolyClip(vert,clipw)
    print('clipped vert:',temp)
    drawPoly(vert,win,'yellow')
    drawPoly(clipw,win,'red3')
    drawPoly(temp,win,'green')

    input('Exit?')	
if __name__=='__main__':
	main()