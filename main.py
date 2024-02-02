from pygame import * 
from random import randint 
 
class GameSprite(sprite.Sprite): 
 
    def __init__(self, player_image , player_x , player_y, size_x, size_y, player_speed): 
        sprite.Sprite.__init__(self) 
        self.image = transform.scale(image.load(player_image),(50 , 50))  
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
    def reset (self): 
        window.blit(self.image,(self.rect.x , self.rect.y)) 
 
class Player(GameSprite): 
    def update(self): 
        keys_pressed = key.get_pressed() 
        if keys_pressed [K_UP] and self.rect.y > 5 : 
            self.rect.y -= self.speed 
        if keys_pressed [K_DOWN] and self.rect.y < win_height - 80 : 
            self.rect.y += self.speed 
         
tennnisball = sprite.Group()

#game scene
win_width = 700 
win_height = 500 
window = display.set_mode((win_width, win_height)) 
display.set_caption("Ping-Pong") 
#background = transform.scale(("background.jpg")(win_width, win_height)) 
#fonts and names 
font.init() 
font1 = font.Font(None, 80)
font2 = font.Font(None, 36)

txt_lose_game = font1.render('YOU LOSE', True, [255, 0, 0])
txt_win_game = font1.render('YOU WIN', True, [0, 255, 0])

#picture 
racket_img = "racket.png"
tennisball_img = "tennis_ball"
background = "background.jpg"
window.fill(background)

#descend
racket = Player(rocket_img, 5, win_height - 100, 80, 100, 20) 
tennisball = sprite.Group() 
for i in range(1, 6): 
    monster = Enemy(ufo_img, randint(80, win_width - 80), -40, 80, 50, randint(1, 5)) 
    monsters.add(monster)  

while run: 
 
    #the event of clicking on the close button 
     
    for e in event.get(): 
        if e.type == QUIT: 
            run = False 
            #the event of clicking to space - sprite is shooting



    if not finish: 
 
        window.blit(background, (0, 0)) 
         
        #writing text on screen 
 
        text = font2.render("Рахунок:" + str(score), 1, (255, 255, 255)) 
        window.blit(text, (10, 20)) 
 
        #sprites moves
 
        racket.update() 
        tennisball_update()


        if sprite.spritecollide(rocket, monsters, False):
            finish = True
            window.blit(txt_lose_game, [200, 200])
 
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            monster = Enemy(ufo_img, randint(0, win_width - 80), 0, 80, 50, randint(1, 5)) 
            monsters.add(monster)
            score += 1

        if score >= 100:
            finish = True
            window.blit(txt_win_game, [200, 200])

        if lost == 3:
            finish = True
            window.blit(txt_lose_game, [200, 200])

        display.update() 
    
    else:
        score = 0
        lost = 0
        finish = False

        for m in monsters:
            m.kill()
        
        for m in bullets:
            m.kill()
        
        time.delay(3000)
        for i in range(1, 6): 
            monster = Enemy(ufo_img, randint(80, win_width - 80), -40, 80, 50, randint(1, 5)) 
            monsters.add(monster)

    time.delay(50)