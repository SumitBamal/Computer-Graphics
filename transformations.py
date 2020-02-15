from drawLine import ViewPort,drawLine
from drawPolygon import drawPoly
import math,random
from graphics import *
'''
-50 0
100 0
125 50
25 100
-75 50
'''
def translation(vert,x,y,win,f=True):
    if f:input("translate by"+str(x)+str(y))
    vert = [i+[1] for i in vert]
    
    ###Translation matrix
    trans = [[1,0,0],[0,1,0],[-x,-y,1]]

    result = [[int(sum(a*b for a,b in zip(A_row,B_col))) for B_col in trans ] for A_row in vert]
    result = [i[:-1] for i in result]

    #drawPoly(result,win,'blue')

    return result
def rotation(vert,x,y,angle,win):
    vert = translation(vert,x,y,win,False)
    vert =only_rotation(vert,x,y,angle,win)
    result = translation(vert,-x,-y,win,False)
    return result

def only_rotation(vert,x,y,angle,win):
    input("Rotate at"+str(x)+str(y)+" by"+str(angle)+"?")
        
    angle = (math.pi*angle/180)
    vert = [i+[1] for i in vert]
    
    ###Rotation matrix
    trans = [[math.cos(angle),math.sin(angle),0],[-math.sin(angle),math.cos(angle),0],[0,0,1]]

    result = [[int(sum(a*b for a,b in zip(A_row,B_col))) for B_col in zip(*trans) ] for A_row in vert]
    result = [i[:-1] for i in result]

    #drawPoly(result,win,'green2')
    return result

def scale(vert,x,y,sx,sy,win):
    vert = translation(vert,x,y,win,False)
    only_scale(vert,x,y,sx,sy,win)
    result = translation(result,-x,-y,win,False)
    return result

def only_scale(vert,x,y,sx,sy,win):
    input("Scale at "+str(x)+str(y)+" by"+str(sx)+str(sy)+"?")
    
    vert = [i+[1] for i in vert]
    
    ###Scale matrix
    trans = [[sx,0,0],[0,sy,0],[0,0,1]]

    result = [[int(sum(a*b for a,b in zip(A_row,B_col))) for B_col in zip(*trans) ] for A_row in vert]
    result = [i[:-1] for i in result]

    #drawPoly(result,win,'red2')
    
    return result

def reflection(vert,x,y,angle,win):
    input("Reflect by line passing through"+str(x)+str(y)+" at angle "+str(angle)+"?")
    vert = translation(vert,x,y,win,False)
    vert = only_rotation(vert,x,y,angle,win)
    
    vert = [i+[1] for i in vert]
    
    ###Reflection matrix
    trans = [[-1,0,0],[0,1,0],[0,0,1]]

    result = [[int(sum(a*b for a,b in zip(A_row,B_col))) for B_col in zip(*trans) ] for A_row in vert]
    result = [i[:-1] for i in result]

    #drawPoly(result,win,'green2')
    result = only_rotation(result,x,y,-angle,win)
    result = translation(result,-x,-y,win,False)
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
    functions  = [rotation,translation,scale,reflection,shear_x,shear_y]
    drawPoly(vert,win)
    while 1:
        w=list(map(int,input('''1.Rotate<x,y,angle>
2.Translate<x,y>
3.Scale<x,y,sx,sy> 
4.Reflect<x,y,angle>
5.Shear_x<shx>
6.Shear_y<shy>
>>''').split()))
        vert = functions[w[0]-1](vert , *w[1:] , win)
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        drawPoly(vert,win,color_rgb(r,g,b))
        input()
if __name__ == "__main__":
    main()