from project.shapes import *
import pygame
import random
import sys
import time


pygame.init()



filePath = "project/highscore.txt"

fileTextValid = FileValidation(filePath)

WindowMaker(fileTextValid)

menu()


window_width = 800
window_height = 600
rows = 10
columns = 20
block = 30
radius = 5

x_side = (window_width - (columns * block)) / 2
y_side = 100

myshapes = [L, LINE, MINILINE, ORIBLINE, POINT, CROSS, Z, Z2 ]

def updateVars():
    global x, y, sh_type, random_color, Rotation, sheklman
    x = 1
    y = 3
    # sh_type = random.randint(0, len(myshapes) - 1)
    sh_type = 1
    random_color = random.randint(1, len(colors) - 1)
    Rotation = 0
    sheklman = myshapes[sh_type][Rotation]

def newGame():
    global score, Vaziatbazi, speed, fps, rows, columns, Data, dynamic_text, newrecordzad
    updateVars()
    Data = []
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(0)
        Data.append(temp)
    score = 0
    Vaziatbazi = "start"
    speed = 30
    fps = 50
    dynamic_text = ""
    newrecordzad = False

def khatshekan():
    global sheklman, score, x, y
    global rows, columns, Data, dynamic_text

    for i in range(4):
        for j in range(4):
            if sheklman[i][j] > 0:
                Data[i + y][j + x] = random_color
    i = 0
    j = 0
    khat_shomar = 0
    for j in range(columns):
        sefr_shomar = 0
        for i in range(rows):
            if Data[i][j] > 0:
                sefr_shomar += 1
        if sefr_shomar > 9:
            khat_shomar += 1
            for k in range(j, 1, -1):
                for h in range(rows):
                    Data[h][k] = Data[h][k - 1]
    if khat_shomar > 0:
        dynamic_text = "emtiaz gerefti !"
    score += khat_shomar ** 2

def Barkhord():
    global sheklman, x, y
    Barkhord_b = False
    for i in range(4):
        for j in range(4):
            if sheklman[i][j] > 0:
                if i + y > 9 or i + y < 0  or j + x > 19 or Data[i + y][j + x] > 0:
                    Barkhord_b = True
    # print("barkhord: ", Barkhord_b)
    return Barkhord_b

newGame()

window = pygame.display.set_mode((window_width, window_height))


shomarandeh = 0


isRuning = True
while isRuning:

    sefrdari = 0
    for i in range(rows):
        if Data[i][7] > 0:
            sefrdari += 1
    if sefrdari > 0:
        dynamic_text = "dari mibazi refigh !"

    if ((shomarandeh % speed) == 0) and (Vaziatbazi == "start"):
        x += 1
        if Barkhord() == True:
            x -= 1
            khatshekan()
            updateVars()

        if Barkhord() == True:
            Vaziatbazi = "gameover"
            shomarandeh = 0

    backgroundcolor = darkcyan
    window.fill(backgroundcolor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRuning = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_ESCAPE:
                newGame()

            if event.key == pygame.K_s:
                if Vaziatbazi == "start":
                    Vaziatbazi = "stop"
                elif Vaziatbazi == "stop":
                    Vaziatbazi = "start"
                print("Vaziatbazi is: " + Vaziatbazi)

            if (event.key == pygame.K_n) and (Vaziatbazi == "start"):
                updateVars()

            if (event.key == pygame.K_SPACE) and (Vaziatbazi == "start"):
                while not Barkhord():
                    x += 1
                x -= 1
                khatshekan()
                updateVars()

                if Barkhord() == True:
                    Vaziatbazi = "gameover"

            if (event.key == pygame.K_LEFT) and (Vaziatbazi == "start"):
                previous_Rot = Rotation
                if (Rotation >= 0) and (Rotation < len(myshapes[sh_type]) - 1):
                    Rotation += 1
                else:
                    Rotation = 0
                # Rotation = (Rotation + 1) % (len(myshapes[sh_type]))
                sheklman = myshapes[sh_type][Rotation]

                if Barkhord() == True:
                    Rotation = previous_Rot
                    # if (Rotation > 0) and (Rotation <= (len(myshapes[sh_type]) - 1)):
                    #     Rotation -= 1
                    # else:
                    #     Rotation = len(myshapes[sh_type]) - 1

                sheklman = myshapes[sh_type][Rotation]

            if (event.key == pygame.K_RIGHT) and (Vaziatbazi == "start"):
                fps = 120
                speed = 2

            if (event.key == pygame.K_UP) and (Vaziatbazi == "start"):
                y -= 1
                if Barkhord() == True:
                    y += 1

            if (event.key == pygame.K_DOWN) and (Vaziatbazi == "start"):
                y += 1
                if Barkhord() == True:
                    y -= 1

        if (event.type == pygame.KEYUP) and (Vaziatbazi == "start"):
            fps = 35
            speed = 30

    for i in range(rows):
        for j in range(columns):
            if i % 2 == 0:
                p = i * 4 + j
            else:
                p = i * 4 + j + 1

            if p % 2 == 0:
                chessColor = lightGreen
            else:
                chessColor = lightBlue
            
            pygame.draw.rect(window, chessColor, ( x_side + j * block ,y_side + i * block, block, block ), 0, radius)
            pygame.draw.rect(window, (255, 255, 255), ( x_side + j * block ,y_side + i * block, block, block ), 1, radius)
            if Data[i][j] > 0:
                pygame.draw.rect(window, colors[Data[i][j]], (x_side + (j) * block + 1,y_side + (i) * block + 1, block - 2, block - 2 ), 0, radius)

    i = 0
    j = 0
    for i in range(4):
        for j in range(4):
            if sheklman[i][j] > 0:
                pygame.draw.rect(window, colors[random_color], (x_side + (j + x) * block + 1,y_side + (i + y) * block + 1, block - 2, block - 2 ), 0, radius)
            # else:
            #     pygame.draw.rect(window, (255, 255, 255), ( (j + x) * block + 1, (i + y) * block + 1, block - 2, block - 2 ), 0, radius)
            
    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    myFont = pygame.font.SysFont('Calibri', 30, True, False)
    sookhti = font1.render("tamoom shod refigh !", True, (255, 125, 0))
    sookhti_2 = font1.render("ESC ro feshar bedeh !", True, (255, 215, 0))
    stopFont = pygame.font.SysFont("Calibri", 280, True, False)
    stoptext = stopFont.render("Stop !", True, violet)


    if Vaziatbazi == "stop":
        window.blit(stoptext, [x_side, 100])


    last_hsighscore = open(filePath, "rt")

    if open(filePath, "rt") == True:
        open(filePath, "rt")
    elif open(filePath, "rt") == False:
        open(filePath, "xt")
        open(filePath, "wt").write(0)

    last_hsighscore = open(filePath, "rt").read()

    newhighscore = last_hsighscore

    hidden_color = (255, 255, 255)
    if Vaziatbazi == "gameover":
        hidden_color = backgroundcolor
    playerscore = font.render("Score: " + str(score), True, (255, 255, 255))

    scoretext = font.render("Last highScore: " + str(last_hsighscore), True, hidden_color)
    window.blit(playerscore, [0, 10])
    window.blit(scoretext, [0, 50])
    
    newRecordtext = myFont.render("record jadid !", True, salmon)

    if score > int(last_hsighscore):
        newhighscore = score
        open(filePath, "wt").write(str(newhighscore))
        newrecordzad = True
    
    if newrecordzad:
        window.blit(newRecordtext, [int((5/12) * window_width), window_height - (30 + 30)])


    newhighscore_text = font.render("your highscore: " + str(newhighscore), True, (255, 255, 255))
    
    if Vaziatbazi == "gameover":
        window.blit(sookhti, [100, 400])
        window.blit(sookhti_2, [100, 460])
        window.blit(newhighscore_text, [280, 40])

    # dynamic_alert section
    dynamic_alert = myFont.render(dynamic_text, True, yellow)
    window.blit(dynamic_alert, [50, window_height - (30 + 30)])

    # end of dynamic alert section

    pygame.display.update()
    pygame.time.Clock().tick(fps)
    shomarandeh += 1