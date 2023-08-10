import pygame
pygame.font.init()
running = True
background_colour = (225,225,225)
black = (0,0,0)
screen = pygame.display.set_mode((750, 750))
pygame.display.set_caption('Calculator')
screen.fill(background_colour)
num1 = ""
num2 = ""
operator = ""
current_value = 1
start = True
equation = ""
flip = False
third = False
ansnum = False
colour = (195,195,195)
colour2 = (176,176,176)
my_font = pygame.font.SysFont('Times New Roman', 45)
my_font2 = pygame.font.SysFont('Times New Roman', 60)
my_font3 = pygame.font.SysFont('Times New Roman', 40)
decimal = True
nonbinary = False
#FUNCTIONS
def addition(val):
    global equation,num1,num2
    if ansnum == False:         
        #equation += val                   
        if current_value == 1:
            num1 += val
        else:
            num2 += val
        decimal = True     
  
def calculation(val):
    global operator,current_value,third,ansnum,equation,num1,num2, decimal
    if third == False:
        #equation += val
        ansnum = False
           
        current_value = 2  
        operator = val
        third = True
        decimal = True
    else:
        if operator == "+":
            
            equation = str(float(num1)+float(num2))
        if operator == "-":
            
            equation = str(float(num1)-float(num2))
        if operator == "*":
            
            equation = str(float(num1)*float(num2))  
        if operator == "/":
            try:
                equation = str(float(num1)/float(num2))
            except:
                equation = ""    

        num1 = equation
        #equation += val
        num2 = ""
        operator = val
        current_value = 2                       
        ansnum = False
        decimal = True


while running:
#DRAWINGS  0-9   
    screen.fill(pygame.Color(background_colour)) 

    pygame.draw.line(screen,black, (1,1), (749,1))
    pygame.draw.line(screen,black, (1,748), (749,748))
    
    pygame.draw.rect(screen, colour, pygame.Rect(125, 200, 100, 100))
    text_surface = my_font.render('7', False, (0, 0, 0))   
    screen.blit(text_surface, (165,225))

    pygame.draw.rect(screen, colour, pygame.Rect(325, 200, 100, 100))
    text_surface = my_font.render('8', False, (0, 0, 0))   
    screen.blit(text_surface, (365,225))

    pygame.draw.rect(screen, colour, pygame.Rect(525, 200, 100, 100))
    text_surface = my_font.render('9', False, (0, 0, 0))   
    screen.blit(text_surface, (565,225))

    pygame.draw.rect(screen, colour, pygame.Rect(125, 325, 100, 100))
    text_surface = my_font.render('4', False, (0, 0, 0))   
    screen.blit(text_surface, (165,350))

    pygame.draw.rect(screen, colour, pygame.Rect(325, 325, 100, 100))
    text_surface = my_font.render('5', False, (0, 0, 0))   
    screen.blit(text_surface, (365,350))

    pygame.draw.rect(screen, colour, pygame.Rect(525, 325, 100, 100))
    text_surface = my_font.render('6', False, (0, 0, 0))   
    screen.blit(text_surface, (565,350)) 

    pygame.draw.rect(screen, colour, pygame.Rect(125, 450, 100, 100))
    text_surface = my_font.render('1', False, (0, 0, 0))   
    screen.blit(text_surface, (165,475))

    pygame.draw.rect(screen, colour, pygame.Rect(325, 450, 100, 100))
    text_surface = my_font.render('2', False, (0, 0, 0))   
    screen.blit(text_surface, (365,475))

    pygame.draw.rect(screen, colour, pygame.Rect(525, 450, 100, 100))
    text_surface = my_font.render('3', False, (0, 0, 0))   
    screen.blit(text_surface, (565,475))

    pygame.draw.rect(screen, colour2, pygame.Rect(25, 585, 100, 100))
    text_surface = my_font.render('+', False, (255, 200, 0))   
    screen.blit(text_surface, (65,610))

    pygame.draw.rect(screen, colour2, pygame.Rect(140, 585, 100, 100))
    text_surface = my_font.render('-', False, (255, 200, 0))   
    screen.blit(text_surface, (182,609))  

    pygame.draw.rect(screen, colour2, pygame.Rect(255, 585, 100, 100))
    text_surface = my_font.render('*', False, (255, 200, 0))   
    screen.blit(text_surface, (294,618))    

    pygame.draw.rect(screen, colour2, pygame.Rect(370, 585, 100, 100))
    text_surface = my_font.render('/', False, (255, 200, 0))   
    screen.blit(text_surface, (411,612))

    pygame.draw.rect(screen, colour2, pygame.Rect(518, 580, 120, 120))
    text_surface = my_font2.render('=', False, (255, 200, 0))   
    screen.blit(text_surface, (564,608))  

    pygame.draw.rect(screen, colour, pygame.Rect(5, 450, 100, 100))
    text_surface = my_font.render('0', False, (0, 0, 0))   
    screen.blit(text_surface, (42,476))  
    
    pygame.draw.rect(screen, colour, pygame.Rect(5, 326, 100, 100))
    text_surface = my_font2.render('.', False, (0, 0, 0))   
    screen.blit(text_surface, (47,336))     
#CLEAR
    pygame.draw.rect(screen, colour2, pygame.Rect(5, 200, 100, 100))
    text_surface = my_font3.render('Clear', False, (255, 200, 0))   
    screen.blit(text_surface, (9,227))    
    equation = num1 + operator + num2 
    text_surface = my_font2.render(equation, False, (0, 0, 0))  
    screen.blit(text_surface, (165,60))
#NEGATIVE
    pygame.draw.rect(screen, colour, pygame.Rect(5, 80, 100, 100))
    text_surface = my_font2.render('+/-', False, (0, 0, 0))   
    screen.blit(text_surface, (18,97)) 

    pygame.draw.rect(screen, colour, pygame.Rect(643, 590, 100, 100))
    text_surface = my_font.render('B', False, (255, 0, 0))   
    screen.blit(text_surface, (679,615))    
#FUNCTIONS
    pygame.display.update()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:         
            running = False   
        #Clicking
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0]>125 and pos[0]<225 and pos[1]>450 and pos[1]<550:
                addition("1")
                start = False
                flip = True
            elif pos[0]>325 and pos[0]<425 and pos[1]>450 and pos[1]<550:
                addition("2")
                start = False
                flip = True
            if pos[0]>525 and pos[0]<625 and pos[1]>450 and pos[1]<550:
                addition("3")
                start = False  
                flip = True                      
            if pos[0]>125 and pos[0]<225 and pos[1]>325 and pos[1]<425:
                addition("4")
                start = False    
                flip = True                 
            if pos[0]>325 and pos[0]<425 and pos[1]>325 and pos[1]<425:
                addition("5")
                start = False
                flip = True 
            if pos[0]>525 and pos[0]<625 and pos[1]>325 and pos[1]<425:
                addition("6")
                flip = True
                start = False 
            if pos[0]>125 and pos[0]<225 and pos[1]>200 and pos[1]<300:
                addition("7")
                start = False
                flip = True 
            if pos[0]>325 and pos[0]<425 and pos[1]>200 and pos[1]<300:
                addition("8")
                start = False
                flip = True
            if pos[0]>525 and pos[0]<625 and pos[1]>200 and pos[1]<300:
                addition("9")
                start = False
                flip = True
            if pos[0]>5 and pos[0]<105 and pos[1]>450 and pos[1]<550:
                addition("0")
                start = False
            if pos[0]>5 and pos[0]<105 and pos[1]>326 and pos[1]<426:
                if decimal == True:
                    addition(".")  
                    decimal = False 
                    flip = False
            if pos[0]>5 and pos[0]<105 and pos[1]>80 and pos[1]<180:
                if flip == True:
                    if current_value == 1 and len(num1) > 0:
                        num1 = str(float(num1) * -1)
                    if current_value == 2 and len(num2) > 0:
                        num2 = str(float(num2) * -1)                                
                #OPERATIONS OR SYMBOLS
            #PLUS                     
            if pos[0]>25 and pos[0]<125 and pos[1]>585 and pos[1]<685:
                if start == False:
                    calculation("+")
                    start = True
                    decimal = True
                 
            #MINUS                                               
            if pos[0]>140 and pos[0]<240 and pos[1]>585 and pos[1]<685:
                if start == False:
                    calculation("-")
                    start = True     
                    decimal = True               
            #MULTIPLICATION                        
            if pos[0]>255 and pos[0]<355 and pos[1]>585 and pos[1]<685:
                if start == False:
                    calculation("*")
                    start = True
                    decimal = True
            #DIVISION                            
            if pos[0]>370 and pos[0]<470 and pos[1]>585 and pos[1]<685:
                if start == False:
                    calculation("/") 
                    start = True 
                    decimal = True                        
            #CLEAR BUTTON                        
            if pos[0]>5 and pos[0]<105 and pos[1]>200 and pos[1]<300:
                num1 = ""
                num2 = ""
                equation = ""
                operator = ""
                current_value = 1   
                ansnum = False
                start = True  
                decimal = True                 

            #EQUALS OPERATION    
            if pos[0]>520 and pos[0]<640 and pos[1]>580 and pos[1]<700:
                if start == False:
                    #equation += "="
                    if operator == "+":
                        
                        num1 =  str(float(num1)+float(num2))
                    if operator == "-":
                        
                        num1 =  str(float(num1)-float(num2))
                    if operator == "*":
                        
                        num1 =  str(float(num1)*float(num2))  
                    if operator == "/":
                        
                        try:
                            num1 =  str(float(num1)/float(num2))
                        except:
                            num1 =  "" 
                    #if operator == "":
                        #equation = num1     
                    #num1 = equation
                    num2 = ""
                    operator = ""
                    current_value = 1
                    ansnum = True
                    decimal = True
            #Binary Answer
            if pos[0]>643 and pos[0]<743 and pos[1]>590 and pos[1]<690:    
                if current_value == 1 and nonbinary == False:
                        num1 = bin(int(float(num1)))[2:]
                if current_value == 2 and nonbinary == False:
                        num1 = bin(int(float(num2)))[2:]