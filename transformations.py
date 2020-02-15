from drawLine import ViewPort,drawLine
from drawPolygon import drawPoly
import math


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
    input("Rotate at"+str(x)+str(y)+" by"+str(angle)+"?")
    vert = translation(vert,x,y,win,False)
    
    angle = (math.pi*angle/180)
    vert = [i+[1] for i in vert]
    
    ###Rotation matrix
    trans = [[math.cos(angle),math.sin(angle),0],[-math.sin(angle),math.cos(angle),0],[0,0,1]]

    result = [[int(sum(a*b for a,b in zip(A_row,B_col))) for B_col in trans ] for A_row in vert]
    result = [i[:-1] for i in result]

    #drawPoly(result,win,'green2')
    result = translation(result,-x,-y,win,False)
    return result

def scale(vert,x,y,sx,sy,win):
    input("Scale at "+str(x)+str(y)+" by"+str(sx)+str(sy)+"?")
    vert = translation(vert,x,y,win,False)
    vert = [i+[1] for i in vert]
    
    ###Scale matrix
    trans = [[sx,0,0],[0,sy,0],[0,0,1]]

    result = [[int(sum(a*b for a,b in zip(A_row,B_col))) for B_col in trans ] for A_row in vert]
    result = [i[:-1] for i in result]

    #drawPoly(result,win,'red2')
    result = translation(result,-x,-y,win,False)
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
    w=list(map(int,input("1.Rotate<x,y,angle>\n2.Translate<x,y>\n3.Scale<x,y,sx,sy>\n>>").split()))
    functions  = [rotation,translation,scale]
    drawPoly(functions[w[0]-1](vert , *w[1:] , win),win,"red3")

if __name__ == "__main__":
    main()