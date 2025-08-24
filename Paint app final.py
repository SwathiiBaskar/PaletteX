import cv2
import numpy as np
from spectrasketch import ShapeLab
from screeninfo import get_monitors
import sys
monitor=get_monitors()[0]
screen_width=monitor.width
screen_height=monitor.height
lab=ShapeLab(width=screen_width,height=screen_height,background_color=(255,255,255))
toolbar_height=170
lab.rectangle((0,0),(1918,toolbar_height),0,(220,220,220),-1)

sections = [
    ("Selection",   0,    180),
    ("Image",      180,   410),
    ("Tools",      410,   620),
    ("Brushes",    620,   760),
    ("Shapes",     760,  1060),
    ("Colours",   1060,  1720),
    ("Copilot",   1720,  1818),
    ("Layers",    1818,  1918),
]
colors = [
                (0, 0, 0),            #1 Black
                (32, 0, 64),          #2 Very Dark Purple
                (64, 0, 128),         #3 Dark Indigo
                (0, 0, 128),          #4 Navy
                (0, 64, 128),         #5 Teal
                (0, 128, 128),        #6 Dark Cyan
                (0, 128, 0),          #7 Dark Green
                (0, 128, 64),         #8 Pine Green
                (0, 128, 128),        #9 Teal
                (0, 191, 255),        #10 Deep Sky Blue
                (0, 255, 255),        #11 Cyan
                (0, 255, 128),        #12 Spring Green
                (0, 255, 0),          #13 Bright Green
                (128, 255, 0),        #14 Yellow-Green
                (192, 255, 0),        #15 Lime
                (255, 255, 0),        #16 Yellow
                (255, 192, 0),        #17 Gold
                (255, 128, 0),        #18 Orange
                (255, 64, 0),         #19 Deep Orange
                (255, 0, 0),          #20 Red
                (255, 0, 128),        #21 Hot Pink
                (255, 0, 255),        #22 Magenta
                (192, 0, 255),        #23 Purple
                (128, 0, 255),        #24 Violet
                (64, 0, 255),         #25 Indigo
                (128, 128, 255),      #26 Light Indigo
                (173, 216, 230),      #27 Light Blue
                (211, 211, 211),      #28 Light Gray
                (245, 245, 220),      #29 Beige
                (255, 255, 255),      #30 White
]
shape_modes = [
    "f",     
    "l",      
    "r",      
    "c",      
    "t",   
    "rt", 
    "lt",  
    "d",   
    "s",   
    "p",  
    "h",   
    "hp",    
    "o",  
    "ng",   
    "st1",   
    "st2",     
    "st3",  
    "he"
]

for name,x1,x2 in sections:
    cv2.rectangle(lab.canvas,(x1,0),(x2,toolbar_height),(180,180,180),-1)

def draw_icon_grid(canvas,x_start,x_end,y_top,y_bottom,num_rows,num_columns,spacing_x=10,spacing_y=10,padding=10):
    section_width=abs(x_end-x_start)
    section_height=abs(y_bottom-y_top)
    usable_width=section_width-(2*padding)-(num_columns-1)*spacing_x
    usable_height=section_height-(2*padding)- (num_rows-1)*spacing_y
    icon_width=(usable_width)/num_columns
    icon_height=(usable_height)/num_rows
    color_counter=0
    shape_counter=0
    pencil=0
    thickness_box=0
    for row in range(num_rows):
        for column in range(num_columns):
            x1=int((x_start+padding)+column*(icon_width+spacing_x))
            x2=int(x1+icon_width)
            y1=int((y_top+padding)+row*(icon_height+spacing_y))
            y2=int(y1+icon_height)
            colors = [
                (0, 0, 0),            #1 Black
                (32, 0, 64),          #2 Very Dark Purple
                (64, 0, 128),         #3 Dark Indigo
                (0, 0, 128),          #4 Navy
                (0, 64, 128),         #5 Teal
                (0, 128, 128),        #6 Dark Cyan
                (0, 128, 0),          #7 Dark Green
                (0, 128, 64),         #8 Pine Green
                (0, 128, 128),        #9 Teal
                (0, 191, 255),        #10 Deep Sky Blue
                (0, 255, 255),        #11 Cyan
                (0, 255, 128),        #12 Spring Green
                (0, 255, 0),          #13 Bright Green
                (128, 255, 0),        #14 Yellow-Green
                (192, 255, 0),        #15 Lime
                (255, 255, 0),        #16 Yellow
                (255, 192, 0),        #17 Gold
                (255, 128, 0),        #18 Orange
                (255, 64, 0),         #19 Deep Orange
                (255, 0, 0),          #20 Red
                (255, 0, 128),        #21 Hot Pink
                (255, 0, 255),        #22 Magenta
                (192, 0, 255),        #23 Purple
                (128, 0, 255),        #24 Violet
                (64, 0, 255),         #25 Indigo
                (128, 128, 255),      #26 Light Indigo
                (173, 216, 230),      #27 Light Blue
                (211, 211, 211),      #28 Light Gray
                (245, 245, 220),      #29 Beige
                (255, 255, 255),      #30 White
            ]
            shapes=[
                "free_hand",
                "line",
                "rectangle",
                "circle",
                "triangle",
                "rtrh",
                "rtlh",
                "diamond",
                "square",
                "pentagon",
                "hexagon",
                "heptagon",
                "octagon",
                "n_gon",
                "4star",
                "5star",
                "6star",
                "heart"
                ]
            if(x_start==1060 and x_end==1620):
                center=((x1+x2)//2,(y1+y2)//2)
                radius=max(1,int(((x2-x1)**2+(y2-y1)**2)**0.5/2))
                if color_counter < len(colors):
                    color = colors[color_counter]
                    lab.circle(center,radius-10,color,thickness=-1)
                    lab.circle(center,radius-10,color=(0,0,0),thickness=1)
                color_counter+=1
            elif(x_start==760 and x_end==1060):
                if shape_counter==0:
                    cv2.rectangle(lab.canvas, (x1, y1), (x2, y2), color=(0,0,0), thickness=1)
                    mid_y = (y1 + y2) // 2
                    p1_x = x1 + 3
                    p2_x = x1 + (x2 - x1) * 1 // 4
                    p3_x = x1 + (x2 - x1) // 2
                    p4_x = x1 + (x2 - x1) * 3 // 4
                    p5_x = x2 - 3
                    pt1 = (p1_x, mid_y)
                    pt2 = (p2_x, y1 + 3)
                    pt3 = (p3_x, mid_y)
                    pt4 = (p4_x, y2 - 3)
                    pt5 = (p5_x, mid_y)
                    cv2.line(lab.canvas, pt1, pt2, color=(0,0,0), thickness=2)
                    cv2.line(lab.canvas, pt2, pt3, color=(0,0,0), thickness=2)
                    cv2.line(lab.canvas, pt3, pt4, color=(0,0,0), thickness=2)
                    cv2.line(lab.canvas, pt4, pt5, color=(0,0,0), thickness=2)
                    shape_counter+=1
                elif shape_counter==1:
                    lab.line((x1+3,y1+3),(x2-3,y2-3),color=(0,0,0),thickness=2)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    shape_counter+=1
                elif shape_counter==2:
                    lab.rectangle((x1+5,y1+10),(x2-5,y2-10),0,color=(0,0,0),thickness=2)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    shape_counter+=1
                elif shape_counter==3:
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    center=((x1+x2)//2,(y1+y2)//2)
                    radius=max(1,int(((x2-x1)**2+(y2-y1)**2)**0.5/2))
                    lab.circle(center,radius-13,color=(0,0,0),thickness=2)
                    shape_counter+=1
                elif shape_counter==4:
                    lab.triangle((x1+5,y1+5),(x2-5,y2-5),0,color=(0,0,0),thickness=2)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    shape_counter+=1
                elif shape_counter==5:
                    lab.right_triangle_rh((x1+5,y1+5),(x2-5,y2-5),0,color=(0,0,0),thickness=2)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    shape_counter+=1
                elif shape_counter==6:
                    lab.right_triangle_lh((x1+5,y1+5),(x2-5,y2-5),0,color=(0,0,0),thickness=2)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    shape_counter+=1
                elif shape_counter==7:
                    lab.diamond((x1+5,y1+5),(x2-5,y2-5),0,color=(0,0,0),thickness=2)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    shape_counter+=1
                elif shape_counter==8:
                    lab.square((x1+5,y1+5),(x2-5,y2-5),0,color=(0,0,0),thickness=2)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    shape_counter+=1
                elif shape_counter==9:
                    lab.pentagon((x1+5,y1+5),(x2-5,y2-5),0,color=(0,0,0),thickness=2)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    shape_counter+=1
                elif shape_counter==10:
                    lab.hexagon((x1+5,y1+5),(x2-5,y2-5),0,color=(0,0,0),thickness=2)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    shape_counter+=1
                elif shape_counter==11:
                    lab.heptagon((x1+5,y1+5),(x2-5,y2-5),0,color=(0,0,0),thickness=2)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    shape_counter+=1
                elif shape_counter==12:
                    lab.octagon((x1+5,y1+5),(x2-5,y2-5),0,color=(0,0,0),thickness=2)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    shape_counter+=1
                elif shape_counter==13:
                    lab.n_gon((x1+5,y1+5),(x2-5,y2-5),10,0,color=(0,0,0),thickness=2)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    shape_counter+=1
                elif shape_counter==14:
                    lab.star((x1+5,y1+5),(x2-5,y2-5),4,0.3,0,color=(0,0,0),thickness=2)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    shape_counter+=1
                elif shape_counter==15:
                    lab.star((x1+5,y1+5),(x2-5,y2-5),5,0.5,0,color=(0,0,0),thickness=2)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    shape_counter+=1
                elif shape_counter==16:
                    lab.star((x1+5,y1+5),(x2-5,y2-5),6,0.5,0,color=(0,0,0),thickness=2)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    shape_counter+=1
                elif shape_counter==17:
                    lab.heart((x1+5,y1+5),(x2-5,y2-5),0,color=(0,0,0),thickness=2)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
            elif(x_start==1620 and x_end==1720):
                center_x=((x1+x2)//2)
                center_y=((y1+y2)//2)+10
                text="Sketchy"
                font=cv2.FONT_HERSHEY_SIMPLEX
                font_scale=0.6
                thickness=2
                color=(0,0,0)
                text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
                text_x = center_x - text_size[0] // 2
                text_y = center_y + text_size[1] // 2
                cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(192, 0, 255),thickness=-1)
                cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(230,20,255),thickness=2)
                cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                cv2.putText(lab.canvas,text,(text_x,text_y-10),font,font_scale,color,thickness,cv2.LINE_AA)
            elif(x_start==0 and x_end==180):
                cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                cv2.rectangle(lab.canvas,(x1+10,y1+15),(x2-10,y2-15),color=(220,220,220),thickness=-1)
                cv2.rectangle(lab.canvas,(x1+10,y1+15),(x2-10,y2-15),color=(0,0,0),thickness=1)
            elif(x_start==180 and x_end==410):
                if pencil==0:
                    lab.rectangle((x1+30,y1+30),(x2-30,y2-30),45,color=(0,255,255),thickness=-1)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    pencil+=1
                elif pencil==1:
                    lab.rectangle((x1+30,y1+30),(x2-30,y2-30),45,color=(255,0,128),thickness=-1)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    pencil+=1
                elif pencil==2:
                    lab.square((x1+40,y1+40),(x2-40,y2-40),45,color=(255,0,0),thickness=-1)
                    lab.circle((x1+5,y1+5),5,color=(0,0,255),thickness=-1)
                    lab.circle((x2-15,y2-15),15,color=(0,255,0),thickness=-1)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    pencil+=1
                elif pencil==3:
                    cv2.line(lab.canvas,(x1+10,y1+10),(x2-10,y2-10),(0,0,0),thickness=2)
                    cv2.line(lab.canvas,(x2-10,y1+10),(x1+10,y2-10),(0,0,0),thickness=2)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    cv2.rectangle(lab.canvas,(x1+10,y1+10),(x2-10,y2-10),color=(0,0,0),thickness=1)
            elif (x_start==410 and x_end==620):
                if thickness_box==0:
                    cv2.line(lab.canvas,(x1+5,(y1+y2)//2),(x2-5,(y1+y2)//2),color=(0,0,0),thickness=2)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    thickness_box+=1
                elif thickness_box==1:
                    cv2.line(lab.canvas,(x1+5,(y1+y2)//2),(x2-5,(y1+y2)//2),color=(0,0,0),thickness=4)
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    thickness_box+=1
                elif thickness_box==2:
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    cv2.line(lab.canvas,(x1+5,(y1+y2)//2),(x2-5,(y1+y2)//2),color=(0,0,0),thickness=6)
                    thickness_box+=1
                elif thickness_box==3:
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    cv2.line(lab.canvas,(x1+5,(y1+y2)//2),(x2-5,(y1+y2)//2),color=(0,0,0),thickness=8)
                    thickness_box+=1
                elif thickness_box==4:
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    cv2.line(lab.canvas,(x1+5,(y1+y2)//2),(x2-5,(y1+y2)//2),color=(0,0,0),thickness=10)
                    thickness_box+=1
                elif thickness_box==5:
                    cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
                    cv2.line(lab.canvas,(x1+5,(y1+y2)//2),(x2-5,(y1+y2)//2),color=(0,0,0),thickness=12)
                    thickness_box+=1
            else:
                cv2.rectangle(lab.canvas,(x1,y1),(x2,y2),color=(0,0,0),thickness=1)
            
draw_icon_grid(lab.canvas,0,180,0,toolbar_height,1,1)
draw_icon_grid(lab.canvas,180,410,0,toolbar_height,2,2)
draw_icon_grid(lab.canvas,410,620,0,toolbar_height,2,3)
draw_icon_grid(lab.canvas,620,760,0,toolbar_height,2,1)
draw_icon_grid(lab.canvas,760,1060,0,toolbar_height,3,6)
draw_icon_grid(lab.canvas,1060,1720-100,0,toolbar_height,3,10)
draw_icon_grid(lab.canvas,1720-100,1720,0,toolbar_height,1,1)

def handle_mouse_click(x,y):
    global color,thickness,mode
    if 760<=x<=1060 and 0<=y<=toolbar_height:
        col=(x-760)//((1060-760)//6)
        row=y//(toolbar_height//3)
        idx=row*6+col
        if idx<len(shape_modes):
            mode=shape_modes[idx]
            print("Mode Selected: ",mode)
    elif 1060<=x<=1620 and 0<=y<=toolbar_height:
        col=(x-1060)//((1620-1060)//10)
        row=y//(toolbar_height//3)
        idx=row*10+col
        if idx<len(colors):
            color=colors[idx]
            print("Color selected: ",color)
    elif 410<=x<=620 and 0<=y<=toolbar_height:
        col=(x-410)//((620-410)//3)
        row=y//(toolbar_height//2)
        idx=row*3+col
        thickness_levels=[2,4,6,8,10,12]
        if idx<len(thickness_levels):
            thickness=thickness_levels[idx]
            print("Thickness selected: ",thickness)
    elif 180<=x<=410 and 0<=y<=toolbar_height:
        col=(x-180)//((410-180)//2)
        row=y//(toolbar_height//2)
        idx=row*2+col
        if idx==0:
            mode='f'
            color=(0,0,0)
            thickness=1
        elif idx==2:
            mode="fill"
        elif idx==1:
            mode="erase"
        elif idx==3:
            sys.exit()
drawing =False
prev_x,prev_y,x,y=-1,-1,-1,-1
mode='f'
color=(0,0,0)
thickness=3
has_moved=False
def movement(event,mx,my,flags,param):
    global prev_x,prev_y,x,y,drawing,has_moved
    x,y=mx,my
    if event==cv2.EVENT_LBUTTONDOWN:
        if y<=toolbar_height:
            handle_mouse_click(x,y)
            return
        else:
            drawing=True
            has_moved=False
            prev_x,prev_y=x,y
    elif event==cv2.EVENT_MOUSEMOVE and drawing:
        has_moved=True
        if mode=='f':
            lab.line((prev_x,prev_y),(x,y),color,thickness)
            prev_x,prev_y=x,y
        elif mode == 'erase':
            lab.line((prev_x, prev_y), (x, y), (255,255,255), thickness)
            prev_x, prev_y = x, y
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if y <= toolbar_height:
            handle_mouse_click(x, y)
            return
        if mode == 'erase':
            lab.line((prev_x, prev_y), (x, y), (255,255,255), thickness)
            return
        if mode=="fill":
            if y>toolbar_height:
                mask=np.zeros((lab.canvas.shape[0]+2,lab.canvas.shape[1]+2),np.uint8)
                cv2.floodFill(lab.canvas,mask,(x,y),color,loDiff=(10,10,10),upDiff=(10,10,10))
            else:
                print("Fill ignored! Click on the toolbar area")
        elif mode=='r':
            lab.rectangle((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='c':
            center=((prev_x+x)//2,(prev_y+y)//2)
            radius=max(1,int(((x-prev_x)**2+(y-prev_y)**2)**0.5/2))
            lab.circle(center,radius,color,thickness)
        elif mode=='l':
            lab.line((prev_x,prev_y),(x,y),color,thickness)
        elif mode=='t':
            lab.triangle((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='rt':
            lab.right_triangle_rh((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='lt':
            lab.right_triangle_lh((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='d':
            lab.diamond((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='p':
            lab.pentagon((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='h':
            lab.hexagon((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='hp':
            lab.heptagon((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='o':
            lab.octagon((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='s':
            lab.square((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='ng':
            lab.n_gon((prev_x,prev_y),(x,y),13,0,color,thickness)
        elif mode=='he':
            lab.heart((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='st1':
            lab.star((prev_x,prev_y),(x,y),4,0.3,0,color,thickness)
        elif mode=='st2':
            lab.star((prev_x,prev_y),(x,y),5,0.5,0,color,thickness)
        elif mode=='st3':
            lab.star((prev_x,prev_y),(x,y),6,0.5,0,color,thickness)
cv2.namedWindow("Paint app",cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Paint app",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.setMouseCallback("Paint app",movement)

while True:
    temp=ShapeLab(width=screen_width,height=screen_height,background_color=(255,255,255))
    temp.canvas[:]=lab.canvas.copy()
    if drawing and has_moved and mode in ['r','c','l','t','rt','lt','d','p','h','hp','o','s','ng','he','st1','st2','st3',"fill"]:
        if mode == 'erase':
            temp.line((prev_x, prev_y), (x, y), (255,255,255), thickness)
        elif mode=="fill":
            mask=np.zeros((temp.canvas.shape[0]+2,temp.canvas.shape[1]+2),np.uint8)
            cv2.floodFill(temp.canvas,mask,(x,y),color,loDiff=(10,10,10),upDiff=(10,10,10))
        elif mode=='r':
            temp.rectangle((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='c':
            center=((prev_x+x)//2,(prev_y+y)//2)
            radius=max(1,int(((x-prev_x)**2+(y-prev_y)**2)**0.5/2))
            temp.circle(center,radius,color,thickness)
        elif mode=='l':
            temp.line((prev_x,prev_y),(x,y),color,thickness)
        elif mode=='t':
            temp.triangle((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='rt':
            temp.right_triangle_rh((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='lt':
            temp.right_triangle_lh((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='d':
            temp.diamond((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='p':
            temp.pentagon((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='h':
            temp.hexagon((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='hp':
            temp.heptagon((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='o':
            temp.octagon((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='s':
            temp.square((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='ng':
            temp.n_gon((prev_x,prev_y),(x,y),13,0,color,thickness)
        elif mode=='he':
            temp.heart((prev_x,prev_y),(x,y),0,color,thickness)
        elif mode=='st1':
            temp.star((prev_x,prev_y),(x,y),4,0.3,0,color,thickness)
        elif mode=='st2':
            temp.star((prev_x,prev_y),(x,y),5,0.5,0,color,thickness)
        elif mode=='st3':
            temp.star((prev_x,prev_y),(x,y),6,0.5,0,color,thickness)
    cv2.imshow("Paint app", temp.canvas)
    key = cv2.waitKey(1)
    if key == 27:  # ESC to exit
        break
    
cv2.destroyAllWindows()

#clear canvas
#undo/redo
#save
#rotation

