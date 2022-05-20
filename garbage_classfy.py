"""
garbage_classfy -

@IDE:   PyCharm
@Author:石少全
@Date:2022/5/20 14:19 
@Description: 


"""


# 素材已经有了, 现在需要进行再测试
# 从头开始写，这样才能够讲出来


# 一、 最小游戏系统 --- (已完成)
# 二、 加载背景图片 --- (已完成)
# 三、 绑定鼠标图标 --- (暂时完成)
import random

import pygame


pygame.init()
WIDTH = 1000
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('临沂科技职业学院垃圾分类')


def person_mouse():
    """
    绑定鼠标的函数
    :return: 应该是需要返回值的
    """
    m_x, m_y = pygame.mouse.get_pos()
    mouse_image = pygame.image.load('resource/gb.png')
    width = mouse_image.get_width()
    height = mouse_image.get_height()
    m_x = m_x - width / 2
    m_y = m_y - height / 2
    # 进行渲染
    # 鼠标消失
    pygame.mouse.set_visible(False)
    window.blit(mouse_image, (m_x, m_y))


garbage_list =[
    {'location': 'resource/img/1.png', 'key': 0},
    {'location': 'resource/img/2.png', 'key': 1},
    {'location': 'resource/img/3.png', 'key': 2},
    {'location': 'resource/img/4.png', 'key': 3},
    {'location': 'resource/img/5.png', 'key': 0},
    {'location': 'resource/img/6.png', 'key': 0},
    {'location': 'resource/img/7.png', 'key': 0},
    {'location': 'resource/img/8.png', 'key': 0},
    {'location': 'resource/img/9.png', 'key': 0},
    {'location': 'resource/img/10.png', 'key': 0},
    {'location': 'resource/img/11.png', 'key': 0},
    {'location': 'resource/img/12.png', 'key': 0},
    {'location': 'resource/img/13.png', 'key': 0},
    {'location': 'resource/img/14.png', 'key': 0},
    {'location': 'resource/img/15.png', 'key': 0},
    {'location': 'resource/img/16.png', 'key': 0},
    {'location': 'resource/img/17.png', 'key': 0},
    {'location': 'resource/img/18.png', 'key': 0},
]







# 中心点
position = [WIDTH/2, HEIGHT/2]

num_r = random.randint(0, len(garbage_list) - 1)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # 加载一下

    background = pygame.image.load('resource/bg.jpg')
    window.fill((255, 255, 255))
    # 渲染
    window.blit(background, (0, 0))
    pygame.display.flip()

    # 鼠标事件
    person_mouse()
    # 更新

    # 问题？ 为什么一直出现频闪的问题, 还是一直会一直闪啊闪
    # pygame.display.update()


    # 开始判断
    if_img = pygame.image.load(garbage_list[num_r]['location'])
    # 渲染
    w_x = if_img.get_width()
    w_y = if_img.get_height()
    window.blit(if_img, (position[0] - w_x / 2, position[1] - w_y / 2))
    pygame.display.update()


























































































