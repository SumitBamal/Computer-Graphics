from drawLine import ViewPort,drawLine
from drawPolygon import drawPoly
#from scanLine import scanLineUtil
import math,sys
from graphics import color_rgb,Line,Point
'''
l=[
    [40,0,0],[80,0,40],[40,0,80],[0,0,40],
    [40,40,0],[80,40,40],[40,40,80],[0,40,40]
]
'''
def drawAxis(win,new_view):
    L1 = Line(Point(0,0),Point(new_view.xVmax,0))
    L2 = Line(Point(0,0),Point(0,new_view.yVmax))
    L3 = Line(Point(0,0) ,      Point(new_view.xVmin,new_view.yVmin))
    L1.setFill('blue')
    L2.setFill('blue')
    L3.setFill('blue')
    L1.setArrow("last")
    L2.setArrow("last")
    L3.setArrow("last")
    L1.draw(win)
    L2.draw(win)
    L3.draw(win)
    return win


class _3D_helper:
    def __init__(self,vport,win):
        port  = vport
        win = win

    def add_padding(self,l):
        for i in l:
            i.append(1)
        return l

    def remove_padding(self,l):
        for i in range(len(l)):
            for j in range(len(l[0])):
                l[i][j] = l[i][j]//l[i][3]
        for i in range(len(l)):
            l[i] = l[i][:-1]
        return l

    def matrix_multiply(self,m1,m2):
        return [[int(sum(a*b for a,b in zip(A_row,B_col))) for B_col in zip(*m2) ] for A_row in m1]
    
    def draw_2d_polygon(self,l2d,color,undraw=False):
        n = len(l2d)

        drawPoly(l2d[:n//2], win ,color)
        drawPoly(l2d[n//2:], win ,color)
        #scanLineUtil(l2d[:n//2], win ,"green")
        #scanLineUtil(l2d[n//2:], win, "purple")
        for i in range(n//2):
            x1,y1,x2,y2 = l2d[i][0],l2d[i][1],l2d[(n//2)+i][0],l2d[(n//2)+i][1]
            drawLine(win,color,x1,y1,x2,y2)
        if undraw:    drawAxis(win,port)

    def parallel(self,l,x0,y0,z0,n1,n2,n3,a,b,c):
        d0 = n1*x0 + n2*y0 + n3*z0
        d1 = n1*a + n2*b + n3*c
        l = self.add_padding(l)
        trans_matrix = [
            [d1-a*n1,-b*n1,-c*n1,0],
            [-a*n2,d1-b*n2,c*n2,0],
            [-a*n3,-b*n3,d1-c*n3,0],
            [a*d0,b*d0,c*d0,d1]
        ]
        result = self.matrix_multiply(l,trans_matrix)
        result = self.remove_padding(result)
        return convert_to_2d(result)

    def perspective(self,l,x0,y0,z0,n1,n2,n3,a,b,c):
        d0 = x0*n1 + y0*n2 + z0*n3
        d1 = a*n1 + b*n2 + c*n3
        d = d0-d1
        l = self.add_padding(l)
        trans_matrix = [
            [n1*a+d,b*n1,c*n1,n1],
            [a*n2,b*n2+d,c*n2,n2],
            [a*n3,b*n3,c*n3+d,n3],
            [-a*d0,-b*d0,-c*d0,-d1]
        ]
        result = self.matrix_multiply(l,trans_matrix)
        result = self.remove_padding(result)
        return convert_to_2d(result)

    def orthographic_projection(self,l):
        x0,y0,z0 = 0,0,0
        n1,n2,n3 = 0,0,1
        a,b,c = 0,0,1
        return self.parallel(l,x0,y0,z0,n1,n2,n3,a,b,c)

    def isometric_projection(self,l):
        x0,y0,z0 = 50,50,50
        n1,n2,n3 = 1,1,1
        a,b,c = 1,1,1
        return self.parallel(l,x0,y0,z0,n1,n2,n3,a,b,c)

    def diametric_projection(self,l):
        x0,y0,z0 = 50,0,0
        n1,n2,n3 = 1,1,2
        a,b,c = 1,1,2
        return self.parallel(l,x0,y0,z0,n1,n2,n3,a,b,c)

    def trimetric_projection(self,l):
        x0,y0,z0 = 50,0,0
        n1,n2,n3 = 6,4,3
        a,b,c = 6,4,3
        return self.parallel(l,x0,y0,z0,n1,n2,n3,a,b,c)

    def cavalier_projection(self,l):
        x0,y0,z0 = 0,0,0
        n1,n2,n3 = 0,0,1
        a,b,c = 3,4,5
        return self.parallel(l,x0,y0,z0,n1,n2,n3,a,b,c)

    def cabinet_projection(self,l):
        x0,y0,z0 = 0,0,0
        n1,n2,n3 = 0,0,1
        a,b,c = 3,4,10
        return self.parallel(l,x0,y0,z0,n1,n2,n3,a,b,c)

    def one_point_perspective(self,l):
        x0,y0,z0 = 0,0,0
        n1,n2,n3 = 0,0,1
        a,b,c = 50,50,150
        return self.perspective(l,x0,y0,z0,n1,n2,n3,a,b,c)

    def two_point_perspective(self,l):
        x0,y0,z0 = 200,0,0
        n1,n2,n3 = 1,1,0
        a,b,c = -100,-75,-50
        return self.perspective(l,x0,y0,z0,n1,n2,n3,a,b,c)

    def three_point_perspective(self,l):
        x0,y0,z0 = 0,0,0
        n1,n2,n3 = 1,1,1
        a,b,c = 150,150,150
        return self.perspective(l,x0,y0,z0,n1,n2,n3,a,b,c)



def convert_to_2d(l):
    l2d = []
    for i in l:
        l2d.append((i[0] - int(i[2]*(math.cos(math.pi/4))), i[1] - int(i[2]*(math.sin(math.pi/4)))))
    return l2d


if __name__=="__main__":
    port  = ViewPort(-400,-400,400,400)
    win = port.init_view()
    win = drawAxis(win,port)
    __3d = _3D_helper(port,win)

    cube_size = 80
    l=[
        [40,0,0],[80,0,40],[40,0,80],[0,0,40],
        [40,40,0],[80,40,40],[40,40,80],[0,40,40]
    ]
    '''l = [[0,0,0],
            [cube_size,0,0],
            [cube_size,cube_size,0],
            [0,cube_size,0],
            [0,0,cube_size],
            [cube_size,0,cube_size],
            [cube_size,cube_size,cube_size],
            [0,cube_size,cube_size]]'''
    l2d = convert_to_2d(l)
    print(l2d)
    __3d.draw_2d_polygon(l2d,"red")
    print('''Enter any operation (on the viewport):
    o -> orthographic
    i -> isometric
    d -> diametric
    t -> trimetric
    c -> cavalier
    a -> cabinet
    l -> original polygon
    1 -> one point perspective
    2 -> two point perspective
    3 -> three point perspective    
    q -> quit
Press e after each operation to undraw the projected polygon''')
    i=0
    while(True):
        key = win.getKey()
        if(i==0):
            __3d.draw_2d_polygon(l2d,color_rgb(44,44,44),undraw=True)
            i=1
        if(key == 'o'):
            mat = __3d.orthographic_projection(l)
        elif(key == 'i'):
            mat = __3d.isometric_projection(l)
        elif(key == 'd'):
            mat = __3d.diametric_projection(l)
        elif(key == 't'):
            mat = __3d.trimetric_projection(l)
        elif(key == 'c'):
            mat = __3d.cavalier_projection(l)
        elif(key == 'a'):
            mat = __3d.cabinet_projection(l)
        elif(key == 'l'):
            mat = l2d
        elif(key == '1'):
            mat = __3d.one_point_perspective(l)
        elif(key == '2'):
            mat = __3d.two_point_perspective(l)
        elif(key == '3'):
            mat = __3d.three_point_perspective(l)            
        elif(key == 'q'):
            break
        else:
            print("Invalid key pressed...")
            continue
        __3d.draw_2d_polygon(mat,"yellow")
        print(f'Operation {key} is completed...Press e to erase')
        if(win.getKey() == 'e'):
            __3d.draw_2d_polygon(mat,color_rgb(44,44,44),undraw=True)

    win.getMouse() 
    win.close()