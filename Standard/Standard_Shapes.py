import pygame
import sys


# شکل های تتریس
T = [
    [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ],
    [
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        
    ],
    [
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        
    ],
    [
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
    ],
]

L = [
    
    [
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
    ],
    [
        [0, 0, 1, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ],
    [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0],
    ],
]

LP = [
    [
        [0, 1, 1, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
    ],
    [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 0],
    ],
    [
        [1, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ],
]

Z = [
    [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ],
    [
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0],
    ],
]

ZP = [
    
    [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 0],
    ],
    [
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
    ],
]

LINE = [
    
    [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
    ],
    [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ],
]

O = [
    [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ],
]

    # [
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0],
    # ],



    # رنگ ها برای شکل
bc_color_1 = (70, 130, 180)
bc_color_2 = (95, 167, 226)

black = (0, 0, 0)
lightGreen = (0, 255, 149)
Green = (0, 128, 0)
lightBlue = (0, 255, 242)
salmon = (250, 128, 114)
yellow = (255, 255, 0)
violet = (238, 130, 238)
strongviolet = (204, 0, 255)
orange = (255, 165, 0)
strongorange = (255, 81, 0)
blue = (0, 0, 255)
bluered = (220, 20, 60)
darkcyan = (0, 139, 139)

colors = [black, lightGreen, lightBlue, salmon, yellow, violet, orange, blue, 
    strongviolet, strongorange, Green, bluered,
]




def FileValidation(user_input):
    import os
    if not os.path.exists(user_input):
        print("file not found !")
        newzero = open(user_input, "wt")
        newzero.write("0")
        print("file is maded succeccfully !\nwith 0 value !")
        result = ["Data file not found !", "file is maded succeccfully with value 0 !"]
    else:
        print("file founded successfully !")
        result = ["Data file founded successfully !"]
        if os.stat(user_input).st_size == 0:
            open(user_input, "wt").write("0")
            print("file was empty ! it has 0 value now")
            result = ["Data file founded successfully !", "file was empty ! it has 0 value now"]
            
    return result


def menu():
    pygame.display.set_caption("Guide")
    menuWindow = pygame.display.set_mode((800, 600))
    pygame.init()
    
    menu_color = lightBlue

    font_size = 50
    myFont = pygame.font.SysFont('Calibri', font_size, True, False)
    myFont_2 = pygame.font.SysFont('Calibri', 65, True, False)
    arrowRi = myFont.render("fast move --> arrow down v", True, menu_color)
    arrowUp = myFont.render("Rotate --> arrow up ^", True, menu_color)
    arrowDown = myFont.render("move left --> arrow left <", True, menu_color)
    Rotate = myFont.render("move right --> arrow right >", True, menu_color)
    space = myFont.render("super space --> space", True, menu_color)
    StopText = myFont.render("puase game --> key S", True, menu_color)
    reseting = myFont.render("reset game --> ESC", True, menu_color)

    presstext = myFont_2.render("press any key to start", True, orange)
    texts = [arrowRi, arrowUp, arrowDown, Rotate, space, StopText, reseting]
    
    backgroundColor = darkcyan
    
    menuRun = True
    while menuRun:
        menuWindow.fill(backgroundColor)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menuRun = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                menuRun = False
        upf = 30
        rif = 30
        for i in range(len(texts)):
            menuWindow.blit(texts[i], [rif, upf + i * font_size])
        
        menuWindow.blit(presstext, [2 * rif, upf + (len(texts) + 0.5)* font_size])
        pygame.display.update()

def WindowMaker(user_Array):
    win_width = 800
    win_height = 600
    pygame.display.set_caption("Wellcome")
    thisFuncWindow = pygame.display.set_mode((win_width, win_height))
    pygame.init()

    font_size = 30
    myFont = pygame.font.SysFont('Calibri', font_size, True, False)
    myFont_2 = pygame.font.SysFont('Calibri', 65, True, False)
    myFont_3 = pygame.font.SysFont('Calibri', 280, True, False)
    presstext = myFont_2.render("press any key to start", True, orange)
    tetrisText = myFont_3.render("Tetris", True, violet)

    backgroundColor = darkcyan

    menuRun = True
    while menuRun:
        thisFuncWindow.fill(backgroundColor)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menuRun = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                menuRun = False
        
        thisFuncWindow.blit(tetrisText, [70, 20])
        upf = 280
        rif = 30
        for i in range(len(user_Array)):
            thisFuncWindow.blit(myFont.render(user_Array[i], True, yellow), [rif, upf + i * font_size])
            
        thisFuncWindow.blit(presstext, [rif, win_height - (65 + 30)])
        pygame.display.update()

