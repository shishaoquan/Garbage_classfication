"""
garbage_classfication -

@IDE:   PyCharm
@Author:石少全
@Date:2022/5/19 9:59 
@Description: 


"""
import random
import time

import pygame

pygame.init()

WEITH = 1000
HEIGH = 600
window = pygame.display.set_mode((WEITH, HEIGH))
pygame.display.set_caption('垃圾分类小游戏鸭')
window.fill((255, 255, 255))
pygame.display.flip()
# 加载背景图片
image1 = pygame.image.load('resource/bg.jpg')
# 更新一下


image2 = pygame.image.load('resource/gb.png')


def person_mouce():
    x, y = pygame.mouse.get_pos()
    width, height = image2.get_size()
    x -= width / 2
    y -= height / 2
    pygame.mouse.set_visible(False)  # 鼠标不可见
    window.blit(image2, (x, y))


grabage = [
    {'img': 'resource/img/1.png', 'key': 0},
    {'img': 'resource/img/2.png', 'key': 1},
    {'img': 'resource/img/3.png', 'key': 1},
    {'img': 'resource/img/4.png', 'key': 3},
    {'img': 'resource/img/5.png', 'key': 1},
    {'img': 'resource/img/6.png', 'key': 1},
    {'img': 'resource/img/7.png', 'key': 1},
    {'img': 'resource/img/8.png', 'key': 1},
    {'img': 'resource/img/9.png', 'key': 1},
    {'img': 'resource/img/10.png', 'key': 1},
    {'img': 'resource/img/11.png', 'key': 1},
    {'img': 'resource/img/12.png', 'key': 1},
    {'img': 'resource/img/13.png', 'key': 1},
    {'img': 'resource/img/14.png', 'key': 1},
    {'img': 'resource/img/15.png', 'key': 1},
    {'img': 'resource/img/16.png', 'key': 1},
    {'img': 'resource/img/17.png', 'key': 1},
    {'img': 'resource/img/18.png', 'key': 1},

]

position = (WEITH / 2, HEIGH / 2)
random_num = random.randint(0, len(grabage) - 1)
moving = False
score = 0  # 初始化分数
right_img = pygame.image.load('resource/right.png')
wrong_img = pygame.image.load('resource/wrong.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # 增加一些鼠标事件

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                moving = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                moving = False
        if moving == True:
            position = pygame.mouse.get_pos()

    # 下面开始判断
    if 200 <= position[0] <= 310 and 440 <= position[1] <= 600:
        if grabage[random_num]['key'] == 0:
            score += 1
            window.blit(right_img, (350, 150))
        else:
            window.blit(wrong_img, (350, 150))
        pygame.display.flip()  # 更新一下
        random_num = random.randint(0, len(grabage) - 1)
        position = (WEITH / 2, HEIGH / 2)
        moving = False
        time.sleep(1)
    elif 355 <= position[0] <= 470 and 440 <= position[1] <= 600:
        if grabage[random_num]['key'] == 1:
            score += 1
            window.blit(right_img, (350, 150))
        else:
            window.blit(wrong_img, (350, 150))
        pygame.display.flip()
        random_num = random.randint(0, len(grabage) - 1)
        position = (WEITH / 2, HEIGH / 2)
        moving = False
        time.sleep(1)
    elif 500 <= position[0] <= 620 and 440 <= position[1] <= 600:
        if grabage[random_num]['key'] == 2:
            score += 1
            window.blit(right_img, (350, 150))
        else:
            window.blit(wrong_img, (350, 150))
        pygame.display.flip()
        random_num = random.randint(0, len(grabage) - 1)
        position = (WEITH / 2, HEIGH / 2)
        moving = False
        time.sleep(1)

    # 最后一种情况
    elif 650 <= position[0] <= 770 and 440 <= position[1] <= 600:
        if grabage[random_num]['key'] == 2:
            score += 1
            window.blit(right_img, (350, 150))
        else:
            window.blit(wrong_img, (350, 150))
        pygame.display.flip()
        random_num = random.randint(0, len(grabage) - 1)
        position = (WEITH / 2, HEIGH / 2)
        moving = False
        time.sleep(1)

    window.blit(image1, (0, 0))  # 绑定背景

    # 显示分数

    # font = pygame.font.Font('resource/kaiti_GB2312.ttf',30)
    # font.render()









    img3 = pygame.image.load(grabage[random_num]['img']).convert_alpha()
    w1, h1 = img3.get_size()
    testw1 = position[0] - w1 / 2
    testh1 = position[1] - h1 / 2
    window.blit(img3, (testw1, testh1))

    person_mouce()
    pygame.display.update()
