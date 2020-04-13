from drawLine import ViewPort,drawLine,drawAxis
from drawPolygon import drawPoly
import math,random
from graphics import *
'''
-50 0
100 0
125 50
25 100
-75 50

0 0
100 0
150 20
30 90
-100 -40

'''
def translation(vert,x,y,win):
    #if f:input("translate by"+str(x)+str(y))
    vert = [i+[1] for i in vert]
    
    ###Translation matrix
    trans = [[1,0,0],[0,1,0],[-x,-y,1]]

    result = [[int(sum(a*b for a,b in zip(A_row,B_col))) for B_col in zip(*trans) ] for A_row in vert]
    result = [i[:-1] for i in result]

    #drawPoly(result,win,'blue')

    return result
def rotation(vert,x,y,angle,win):
    vert = translation(vert,x,y,win)
    vert =only_rotation(vert,x,y,angle,win)
    result = translation(vert,-x,-y,win)
    return result

def only_rotation(vert,x,y,angle,win):
    #input("Rotate at"+str(x)+str(y)+" by"+str(angle)+"?")
        
    angle = (math.pi*angle/180)
    vert = [i+[1] for i in vert]
    
    ###Rotation matrix
    trans = [[math.cos(angle),math.sin(angle),0],[-math.sin(angle),math.cos(angle),0],[0,0,1]]

    result = [[int(sum(a*b for a,b in zip(A_row,B_col))) for B_col in zip(*trans) ] for A_row in vert]
    result = [i[:-1] for i in result]

    #drawPoly(result,win,'green2')
    return result

def scale(vert,x,y,sx,sy,win):
    vert = translation(vert,x,y,win)
    result = only_scale(vert,x,y,sx,sy,win)
    result = translation(result,-x,-y,win)
    return result

def only_scale(vert,x,y,sx,sy,win):
    #input("Scale at "+str(x)+str(y)+" by"+str(sx)+str(sy)+"?")
    
    vert = [i+[1] for i in vert]
    
    ###Scale matrix
    trans = [[sx,0,0],[0,sy,0],[0,0,1]]

    result = [[int(sum(a*b for a,b in zip(A_row,B_col))) for B_col in zip(*trans) ] for A_row in vert]
    result = [i[:-1] for i in result]

    #drawPoly(result,win,'red2')
    
    return result
def reflection(vert,x,y,angle,win):
    vert = translation(vert,x,y,win)
    vert = only_rotation(vert,x,y,angle,win)
    
    vert = [i+[1] for i in vert]
    
    ###Reflection matrix
    trans = [[-1,0,0],[0,1,0],[0,0,1]]

    result = [[int(sum(a*b for a,b in zip(A_row,B_col))) for B_col in zip(*trans) ] for A_row in vert]
    result = [i[:-1] for i in result]

    #drawPoly(result,win,'green2')
    result = only_rotation(result,x,y,-angle,win)
    result = translation(result,-x,-y,win)
    return result

def shear_x(vert,shx,win ):
    vert = [i+[1] for i in vert]
    
    ###Shear matrix
    trans = [[1,0,0],[shx,1,0],[0,0,1]]
    result = [[int(sum(a*b for a,b in zip(A_row,B_col))) for B_col in zip(*trans) ] for A_row in vert]
    result = [i[:-1] for i in result]
    return result

def shear_y(vert,shy,win ):
    vert = [i+[1] for i in vert]

    ###Shear matrix
    trans = [[1,shy,0],[0,1,0],[0,0,1]]
    result = [[int(sum(a*b for a,b in zip(A_row,B_col))) for B_col in zip(*trans) ] for A_row in vert]
    result = [i[:-1] for i in result]
    return result

def main(): 
    vert=[]
    while(1):
        try:
            x,y=map(int,input('Next vert?').split())
            vert.append([x,y])
        except:
            print(vert)
            break
    if(input('Defualt viewPort is (-400 -400, 400 400). Change?(y/Y)')in ('y','Y')):
        x,y=map(int,input('viewPort\'s xMax yMax : ').split())
        new_view = ViewPort(-x,-y,x,y)
    else:
        new_view =ViewPort(-400,-400,400,400)	
    print('ViewPort :',new_view)
    win = new_view.init_view()
    drawPoly(vert,win)
    
    while 1:
        k=win.getKey()
        #print(k,vert)
        if k=="Left":
            drawPoly(vert,win,color_rgb(44,44,44))
            drawAxis(win,new_view)
            vert = translation(vert,10,0,win) 
            drawPoly(vert,win,"red")
        elif k=="Right":
            drawPoly(vert,win,color_rgb(44,44,44))
            drawAxis(win,new_view)
            vert = translation(vert,-10,0,win) 
            drawPoly(vert,win,"red")
        elif k=="Up":
            drawPoly(vert,win,color_rgb(44,44,44))
            drawAxis(win,new_view)
            vert = translation(vert,0,-10,win) 
            drawPoly(vert,win,"red")
        elif k=="Down":
            drawPoly(vert,win,color_rgb(44,44,44))
            drawAxis(win,new_view)
            vert = translation(vert,0,10,win) 
            drawPoly(vert,win,"red")
        elif k=="s":
            drawPoly(vert,win,color_rgb(44,44,44))
            drawAxis(win,new_view)
            vert = only_scale(vert,0,0,2,2,win) 
            drawPoly(vert,win,"red")
        elif k=="S":
            drawPoly(vert,win,color_rgb(44,44,44))
            drawAxis(win,new_view)
            vert = only_scale(vert,0,0,0.5,0.5,win) 
            drawPoly(vert,win,"red")
        elif k=="r":
            drawPoly(vert,win,color_rgb(44,44,44))
            drawAxis(win,new_view)
            vert = only_rotation(vert,0,0,15,win) 
            drawPoly(vert,win,"red")
        elif k=="R":
            drawPoly(vert,win,color_rgb(44,44,44))
            drawAxis(win,new_view)
            vert = only_rotation(vert,0,0,-15,win) 
            drawPoly(vert,win,"red")
        elif k=="f":
            drawPoly(vert,win,color_rgb(44,44,44))
            drawAxis(win,new_view)
            vert = reflection(vert,0,0,45,win) 
            drawPoly(vert,win,"red")
        elif k=="F":
            drawPoly(vert,win,color_rgb(44,44,44))
            drawAxis(win,new_view)
            vert = reflection(vert,0,0,-45,win) 
            drawPoly(vert,win,"red")        
        elif k=="x":
            drawPoly(vert,win,color_rgb(44,44,44))
            drawAxis(win,new_view)
            vert = shear_x(vert,1,win) 
            drawPoly(vert,win,"red")        
        elif k=="X":
            drawPoly(vert,win,color_rgb(44,44,44))
            drawAxis(win,new_view)
            vert = shear_x(vert,-1,win) 
            drawPoly(vert,win,"red")        
        elif k=="y":
            drawPoly(vert,win,color_rgb(44,44,44))
            drawAxis(win,new_view)
            vert = shear_y(vert,1,win) 
            drawPoly(vert,win,"red")        
        elif k=="Y":
            drawPoly(vert,win,color_rgb(44,44,44))
            drawAxis(win,new_view)
            vert = shear_y(vert,-1,win) 
            drawPoly(vert,win,"red")
        #else:
        #    break
if __name__ == "__main__":
    main()
