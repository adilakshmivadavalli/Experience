import pygame
import sys
import traceback
import myplane
import enemy
import bullet
import supply
import time
import mysql

from pygame.locals import *
from random import *

#Initiate
pygame.init()
pygame.mixer.init()
start = 0
end = 0
upload = 0
download = 0
bestScore = 0
bestNum_se = 0
bestNum_me = 0
bestNum_be = 0
bestTotal_time = 0
bestNum_sb = 0
bestNum_db = 0
bestNum_normalbullet = 0
bestNum_doublebullet = 0
bestNum_super = 0

#Generate background screen
bg_size = width, height = 480, 700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("Aircraft War")

#Set background photo
background = pygame.image.load("images/background.png").convert()

#Set color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#Load music
pygame.mixer.music.load("sound/game_music.ogg")
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.2)

#Add enemy in group
def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)

def add_big_enemies(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)

#Modify enemy speed 
def inc_speed(target, inc):
    for each in target:
        each.speed += inc

def main():
    #Set start time point
    start = time.clock()
    
    #Play bgmusic
    pygame.mixer.music.play(-1)

    #Generate player's plane
    me = myplane.MyPlane(bg_size) 

    #Put enemy's planes in a group
    enemies = pygame.sprite.Group()

    #Generate small enemy in another group
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, 15)

    #Generate middle enemy in another group
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 4)

    #Generate big enemy in another group
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, 2)

    #Initiate normal bullet
    bullet1 = []
    bullet1_index = 0
    BULLET1_NUM = 4
    #Set position of bullet
    for i in range(BULLET1_NUM):
        bullet1.append(bullet.Bullet1(me.rect.midtop))

    #Initiate double bullet
    bullet2 = []
    bullet2_index = 0
    BULLET2_NUM = 8
    #Set position of bullet
    for i in range(BULLET2_NUM//2):
        bullet2.append(bullet.Bullet2((me.rect.centerx-33, me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx+30, me.rect.centery)))

    #Initiate clock
    clock = pygame.time.Clock()

    #Hit picture check
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0

    #Set enemy counter
    num_se = 0
    num_me = 0
    num_be = 0
    #Set supply bag number
    num_sb = 0
    num_db = 0
    #Set super bullet used
    num_super = 0
    #Set score, font and size
    score = 0
    score_font = pygame.font.Font("font/font.ttf", 24)

    #Check game pause or not
    paused = False
    pause_nor_image = pygame.image.load("images/pause_nor.png").convert_alpha()
    pause_pressed_image = pygame.image.load("images/pause_pressed.png").convert_alpha()
    resume_nor_image = pygame.image.load("images/resume_nor.png").convert_alpha()
    resume_pressed_image = pygame.image.load("images/resume_pressed.png").convert_alpha()
    #Put pause button
    paused_rect = pause_nor_image.get_rect()
    paused_rect.left, paused_rect.top = width - paused_rect.width - 10, 10
    paused_image = pause_nor_image

    #Set default difficulty
    level = 1

    #Set super bomb font, picture and number 
    bomb_image = pygame.image.load("images/bomb.png").convert_alpha()
    bomb_rect = bomb_image.get_rect()
    bomb_font = pygame.font.Font("font/font.ttf", 48)
    bomb_num = 3

    #Provide supply bags every 30 sec
    bullet_supply = supply.Bullet_Supply(bg_size)
    bomb_supply = supply.Bomb_Supply(bg_size)
    SUPPLY_TIME = USEREVENT
    pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)

    #Set double bullet timer
    DOUBLE_BULLET_TIME = USEREVENT + 1

    #Set signal of double bullet
    is_double_bullet = False

    #Invincible timer
    INVINCIBLE_TIME = USEREVENT + 2

    #Life number
    life_image = pygame.image.load("images/life.png").convert_alpha() 
    life_rect = life_image.get_rect()
    life_num = 3

    #Set Game Over screen
    gameover_font = pygame.font.Font("font/font.TTF", 48)
    again_image = pygame.image.load("images/again.png").convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load("images/gameover.png").convert_alpha()
    gameover_rect = gameover_image.get_rect()

    #Swith picture
    switch_image = True

    #Set delay
    delay = 100

#########################
    #Check running status
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            #Press pause
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    paused = not paused
                    #If game paused, pause the music and pully bag
                    if paused:
                        pygame.time.set_timer(SUPPLY_TIME, 0)
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()
            
            #Change pause button style
            elif event.type == MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        paused_image = resume_pressed_image
                    else:
                        paused_image = pause_pressed_image
                else:
                    if paused:
                        paused_image = resume_nor_image
                    else:
                       paused_image = pause_nor_image

            #Check if use super bomb or not
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if bomb_num:
                        bomb_num -= 1
                        num_super += 1
                        bomb_sound.play()
                        #Destroy all enemies
                        for each in enemies:
                            if each.rect.bottom > 0:
                                each.active = False

            #Check if the time is supply time or not
            elif event.type == SUPPLY_TIME:
                supply_sound.play()
                #Choice one random
                if choice([True, False]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()

            #Check if the time is double bullet time or not
            elif event.type == DOUBLE_BULLET_TIME:
                is_double_bullet = False
                pygame.time.set_timer(DOUBLE_BULLET_TIME, 0)

            #Cancel invincible
            elif event.type == INVINCIBLE_TIME:
                me.invincible = False
                pygame.time.set_timer(INVINCIBLE_TIME, 0)
                         
        #Modify difficulty depends on score
        if level == 1 and score > 200:
            level = 2
            upgrade_sound.play()
            #Add 3 small enemies, 2 middle enemies and 1 big enemies
            add_small_enemies(small_enemies, enemies, 3)
            add_mid_enemies(mid_enemies, enemies, 2)
            add_big_enemies(big_enemies, enemies, 1)
            #Modify small enemies' speed
            inc_speed(small_enemies, 1)
        elif level == 2 and score > 2000:
            level = 3
            upgrade_sound.play()
            #Add 5 small enemies, 3 middle enemies and 2 big enemies
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            #Modify small enemies' speed
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        elif level == 3 and score > 4000:
            level = 4
            upgrade_sound.play()
            #Add 5 small enemies, 3 middle enemies and 2 big enemies
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            #Modify small enemies' speed
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        elif level == 4 and score > 6000:
            level = 5
            upgrade_sound.play()
            #Add 5 small enemies, 3 middle enemies and 2 big enemies
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            #Modify small enemies' speed
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
            
        #Set screen
        screen.blit(background, (0, 0))
        
        #render used to change it as surface object
        score_text = score_font.render("Score : %s" % str(score), True, WHITE)
        screen.blit(score_text, (10, 5))

        score_text = score_font.render("Small enemy : %s" % str(num_se), True, WHITE)
        screen.blit(score_text, (10, 30))

        score_text = score_font.render("Middle enemy : %s" % str(num_me), True, WHITE)
        screen.blit(score_text, (10, 55))

        score_text = score_font.render("Big enemy : %s" % str(num_be), True, WHITE)
        screen.blit(score_text, (10, 80))

        
        if life_num and not paused:
            # Check user's operation
            key_pressed = pygame.key.get_pressed()

            if key_pressed[K_w] or key_pressed[K_UP]:
                me.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveRight()

            #Shoot normal bullet 6/sec
            if not(delay % 10):
                bullet_sound.play()
                #If double bullet, set bullets to double bullets
                if is_double_bullet:
                    bullets = bullet2
                    bullets[bullet2_index].reset((me.rect.centerx-33, me.rect.centery))
                    bullets[bullet2_index+1].reset((me.rect.centerx+30, me.rect.centery))
                    bullet2_index = (bullet2_index + 2) % BULLET2_NUM
                else:
                    bullets = bullet1
                    bullets[bullet1_index].reset(me.rect.midtop)
                    #Load next bullet in bullets[]
                    bullet1_index = (bullet1_index + 1) % BULLET1_NUM

                
            #Check if bullets hit enemy or not
            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image, b.rect)
                    enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        #One hit decrease one energy
                        for e in enemy_hit:
                            #Middle or big enemy
                            if e in mid_enemies or e in big_enemies:
                                e.hit = True
                                e.energy -= 1
                                if e.energy == 0:
                                    e.active = False
                            #Small enemy
                            else:
                                e.active = False

###################################
            #Draw supper bullet bag
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                #Check if player catch it or not 
                if pygame.sprite.collide_mask(bomb_supply, me):
                    get_bomb_sound.play()
                    num_sb += 1
                    if bomb_num < 3 :
                        bomb_num += 1
                    bomb_supply.active = False

            #Draw double bullet bag
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                #Check if player catch it or not 
                if pygame.sprite.collide_mask(bullet_supply, me):
                    get_bullet_sound.play()
                    num_db += 1
                    is_double_bullet = True
                    pygame.time.set_timer(DOUBLE_BULLET_TIME, 18 * 1000)
                    bullet_supply.active = False
           
            #Draw big enemy
            for each in big_enemies:
                #Check the enemy alive or destroy
                if each.active:
                    each.move()
                    #If hit, switch picture
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        if switch_image:
                            screen.blit(each.image1, each.rect)
                        else:
                            screen.blit(each.image2, each.rect)

                    #Draw enemy energy
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.right, each.rect.top - 5), \
                                     2)
                    #Change the color
                    energy_remain = each.energy / enemy.BigEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, \
                                      each.rect.top - 5), 2)
                        
                    #Play background music. -1 means continuous
                    if each.rect.bottom == -50:
                        enemy3_fly_sound.play(-1)
                else:
                    #Destroy
                    if not(delay % 3):
                        if e3_destroy_index == 0:
                            enemy3_down_sound.play()
                        #Show destroy in progress with 6 pictures 
                        screen.blit(each.destroy_images[e3_destroy_index], each.rect)
                        e3_destroy_index = (e3_destroy_index + 1) % 6
                        if e3_destroy_index == 0:
                            enemy3_fly_sound.stop()
                            score += 100
                            num_be += 1
                            each.reset()

            #Draw middle enemies
            for each in mid_enemies:
                #Check the enemy alive or destroy
                if each.active:
                    each.move()
                    #If hit, switch picture
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)

                    #Draw enemy energy
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.right, each.rect.top - 5), \
                                     2)
                    #Change the color
                    energy_remain = each.energy / enemy.MidEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, \
                                      each.rect.top - 5), 2)
                else:
                    #Destroy
                    if not(delay % 3):
                        if e2_destroy_index == 0:
                            enemy2_down_sound.play()
                        #Show destroy in progress with 4 pictures 
                        screen.blit(each.destroy_images[e2_destroy_index], each.rect)
                        e2_destroy_index = (e2_destroy_index + 1) % 4
                        if e2_destroy_index == 0:
                            score += 60
                            num_me += 1
                            each.reset()

            #Draw small enemy
            for each in small_enemies:
                #Check the enemy alive or destroy
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    #Destroy
                    if not(delay % 3):
                        if e1_destroy_index == 0:
                            enemy1_down_sound.play()
                        #Show destroy in progress with 4 pictures 
                        screen.blit(each.destroy_images[e1_destroy_index], each.rect)
                        e1_destroy_index = (e1_destroy_index + 1) % 4
                        if e1_destroy_index == 0:
                            score += 10
                            num_se += 1
                            each.reset()

            #Detect collision, check if player's plane touched any enemy plane in group of enemies
            enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
            if enemies_down and not me.invincible:
                #If player's plane down, all enemies down.
                me.active = False
                for e in enemies_down:
                    e.active = False
            
            #Draw player's plane with switching picture
            if me.active:
                if switch_image:
                    screen.blit(me.image1, me.rect)
                else:
                    screen.blit(me.image2, me.rect)
            else:
                #Destroy
                if not(delay % 3):
                    if me_destroy_index == 0:
                        me_down_sound.play()
                    #Show destroy in progress with 4 pictures 
                    screen.blit(me.destroy_images[me_destroy_index], me.rect)
                    me_destroy_index = (me_destroy_index + 1) % 4
                    #When player's plane down, life count -1 and player will have 3 second without any hurt
                    if me_destroy_index == 0:
                        life_num -= 1
                        me.reset()
                        #When player's plane down, won't get hurt in 3 sec
                        pygame.time.set_timer(INVINCIBLE_TIME, 3 * 1000)
                    else:
                        #Set end time point
                        end = time.clock()

            #Draw super bullet
            bomb_text = bomb_font.render("× %d" % bomb_num, True, WHITE)
            text_rect = bomb_text.get_rect()
            screen.blit(bomb_image, (10, height - 10 - bomb_rect.height))
            screen.blit(bomb_text, (20 + bomb_rect.width, height - 5 - text_rect.height))

            #Draw remain life
            if life_num:
                for i in range(life_num):
                    screen.blit(life_image, \
                                (width-10-(i+1)*life_rect.width, \
                                 height-10-life_rect.height))

######################
        #Set Game Over
        elif life_num == 0:
            #Stop background music
            pygame.mixer.music.stop()

            #Stop all music
            pygame.mixer.stop()

            #Stop provide supply bag
            pygame.time.set_timer(SUPPLY_TIME, 0)

            #Draw Game Over Screen
            #Show the game time
            total_time = "%d" % (end - start)
            num_normalbullet = (int)(total_time) * 6
            num_doublebullet = num_db * 12 * 18

            #Get data from database
            global download
            while download == 0:
                global bestScore,bestNum_se,bestNum_me,bestNum_be,bestTotal_time,bestNum_sb,bestNum_db,bestNum_normalbullet,bestNum_doublebullet,bestNum_super
                bestScore = mysql.get_bestScore()
                bestNum_se = mysql.get_bestNum_se()
                bestNum_me = mysql.get_bestNum_me()
                bestNum_be = mysql.get_bestNum_be()
                bestTotal_time = mysql.get_bestTotal_time()
                bestNum_sb = mysql.get_bestNum_sb()
                bestNum_db = mysql.get_bestNum_db()
                bestNum_normalbullet = mysql.get_bestNum_normalbullet()
                bestNum_doublebullet = mysql.get_bestNum_doublebullet()
                bestNum_super = mysql.get_bestNum_super()          
                download += 1

            #Upload data to database
            global upload
            while upload == 0:
                mysql.upload_score(score,num_se,num_me,num_be,\
                                   total_time,num_sb,num_db,num_normalbullet,\
                                   num_doublebullet,num_super)        
                upload += 1

            #Show message in Game Over screen
            new_record = 0
            if int(score) > int(bestScore):            
                score_text = score_font.render("Score : %s" % str(score), True, RED)
                score_text2 = score_font.render("Best: %s" % str(score), True, WHITE)
                new_record += 1
                screen.blit(score_text, (10, 5))
                screen.blit(score_text2, (280, 5))
            else:
                score_text2 = score_font.render("Best: %s" % str(bestScore), True, WHITE)
                screen.blit(score_text2, (280, 5))

            if int(num_se) > bestNum_se:
                se_text = score_font.render("Small enemy : %s" % str(num_se), True, RED)
                se_text2 = score_font.render("Best: %s" % str(num_se), True, WHITE)
                new_record += 1
                screen.blit(se_text, (10, 30))
                screen.blit(se_text2, (295, 30))
            else:
                se_text2 = score_font.render("Best: %s" % str(bestNum_se), True, WHITE)
                screen.blit(se_text2, (295, 30))

            if int(num_me) > bestNum_me:
                me_text = score_font.render("Middle enemy : %s" % str(num_me), True, RED)
                me_text2 = score_font.render("Best: %s" % str(num_me), True, WHITE)
                new_record += 1
                screen.blit(me_text, (10, 55))
                screen.blit(me_text2, (320, 55))
            else:
                me_text2 = score_font.render("Best: %s" % str(bestNum_me), True, WHITE)
                screen.blit(me_text2, (320, 55))

            if int(num_be) > bestNum_be:
                be_text = score_font.render("Big enemy : %s" % str(num_be), True, RED)
                be_text2 = score_font.render("Best: %s" % str(num_be), True, WHITE)
                new_record += 1
                screen.blit(be_text, (10, 80))
                screen.blit(be_text2, (320, 80))
            else:
                be_text2 = score_font.render("Best: %s" % str(bestNum_be), True, WHITE)
                screen.blit(be_text2, (320, 80))
            
            if int(total_time) > bestTotal_time:
                Time_text = score_font.render("Time : %s Seconds" % str(total_time), True, RED)
                Time_text2 = score_font.render("Best: %s" % str(total_time), True, WHITE)
                new_record += 1
                screen.blit(Time_text, (10, 105))
                screen.blit(Time_text2, (320, 105))
            else:
                Time_text = score_font.render("Time : %s Seconds" % str(total_time), True, WHITE)
                Time_text2 = score_font.render("Best: %s" % str(bestTotal_time), True, WHITE)
                screen.blit(Time_text, (10, 105))
                screen.blit(Time_text2, (320, 105))
            
            if int(num_sb) > bestNum_sb:
                sbb_text = score_font.render("Super bullet bag accept : %s" % str(num_sb), True, RED)
                sbb_text2 = score_font.render("Best: %s" % str(num_sb), True, WHITE)
                new_record += 1
                screen.blit(sbb_text, (10, 130))
                screen.blit(sbb_text2, (320, 130))
            else: 
                sbb_text = score_font.render("Super bullet bag accept : %s" % str(num_sb), True, WHITE)
                sbb_text2 = score_font.render("Best: %s" % str(bestNum_sb), True, WHITE)
                screen.blit(sbb_text, (10, 130))
                screen.blit(sbb_text2, (320, 130))

            if int(num_db) > bestNum_db:
                dbb_text = score_font.render("Double bullet bag accept : %s" % str(num_db), True, RED)
                dbb_text2 = score_font.render("Best: %s" % str(num_db), True, WHITE)
                new_record += 1
                screen.blit(dbb_text, (10, 155))
                screen.blit(dbb_text2, (320, 155))
            else:    
                dbb_text = score_font.render("Double bullet bag accept : %s" % str(num_db), True, WHITE)
                dbb_text2 = score_font.render("Best: %s" % str(bestNum_db), True, WHITE)
                screen.blit(dbb_text, (10, 155))
                screen.blit(dbb_text2, (320, 155))

            if int(num_normalbullet) > bestNum_normalbullet:
                nb_text = score_font.render("Normal bullet used : %s" % str(num_normalbullet), True, RED)
                nb_text2 = score_font.render("Best: %s" % str(num_normalbullet), True, WHITE)
                new_record += 1
                screen.blit(nb_text, (10, 180))
                screen.blit(nb_text2, (320, 180))
            else:
                nb_text = score_font.render("Normal bullet used : %s" % str(num_normalbullet), True, WHITE)
                nb_text2 = score_font.render("Best: %s" % str(bestNum_normalbullet), True, WHITE)
                screen.blit(nb_text, (10, 180))
                screen.blit(nb_text2, (320, 180))

            if int(num_doublebullet) > bestNum_doublebullet:
                db_text = score_font.render("Double bullet used : %s" % str(num_doublebullet), True, RED)
                db_text2 = score_font.render("Best: %s" % str(num_doublebullet), True, WHITE)
                new_record += 1
                screen.blit(db_text, (10, 205))
                screen.blit(db_text2, (320, 205))
            else:
                db_text = score_font.render("Double bullet used : %s" % str(num_doublebullet), True, WHITE)
                db_text2 = score_font.render("Best: %s" % str(bestNum_doublebullet), True, WHITE)
                screen.blit(db_text, (10, 205))
                screen.blit(db_text2, (320, 205))
            
            if int(num_super) > bestNum_super:
                sb_text = score_font.render("Super bullet used : %s" % str(num_super), True, RED)
                sb_text2 = score_font.render("Best: %s" % str(num_super), True, WHITE)
                new_record += 1
                screen.blit(sb_text, (10, 230))
                screen.blit(sb_text2, (320, 230))
            else:                
                sb_text = score_font.render("Super bullet used : %s" % str(num_super), True, WHITE)
                sb_text2 = score_font.render("Best: %s" % str(bestNum_super), True, WHITE)
                screen.blit(sb_text, (10, 230))
                screen.blit(sb_text2, (320, 230))

            gameover_text1 = gameover_font.render("Game Over", True, (255, 255, 255))
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left, gameover_text1_rect.top = 135,300
            screen.blit(gameover_text1, gameover_text1_rect)

            if new_record > 0:
                gameover_text2 = gameover_font.render("New Record!!", True, RED)
                gameover_text2_rect = gameover_text2.get_rect()
                gameover_text2_rect.left, gameover_text2_rect.top = 120,365
                screen.blit(gameover_text2, gameover_text2_rect)

            again_rect.left, again_rect.top = 90,465
            screen.blit(again_image, again_rect)

            gameover_rect.left, gameover_rect.top = 90,515
            screen.blit(gameover_image, gameover_rect)

            #Check keyboard
            #If press left key
            if pygame.mouse.get_pressed()[0]:
                #Get position of mouse
                pos = pygame.mouse.get_pos()
                #If player press restart
                if again_rect.left < pos[0] < again_rect.right and \
                   again_rect.top < pos[1] < again_rect.bottom:
                    #run main again
                    download -= 1
                    upload -= 1
                    main()
                    
                #If press Quit           
                elif gameover_rect.left < pos[0] < gameover_rect.right and \
                     gameover_rect.top < pos[1] < gameover_rect.bottom:
                    #Game exit
                    pygame.quit()
                    sys.exit()      

        #Draw pause button
        screen.blit(paused_image, paused_rect)

        #Switch in every 5 frame
        if not(delay % 5):
            switch_image = not switch_image

        delay -= 1
        if not delay:
            delay = 100

        #Flip the screen
        pygame.display.flip()

        #Set clock
        clock.tick(60)

#Check if main is correct or not. If not, I won't quit immediately.
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
