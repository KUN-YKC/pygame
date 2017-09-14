import sys

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf
#from game_functions import update_screen
from pygame.sprite import Group
from alien import Alien
from scoreboard import Scoreboard

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_with, ai_settings.screen_height))
	pygame.display.set_caption('外星人游戏')
	
	#创建Play按钮
	play_button = Button(ai_settings, screen, 'Play')
	
	#创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)
	#创建存储游戏统计信息的实例，并创建得分牌
	sb = Scoreboard(ai_settings, screen, stats)
	#创建一艘飞船
	ship = Ship(ai_settings, screen)

	#创建一个用于存储子弹的编组
	bullets = Group()
	#外星人编组
	aliens = Group()
	#外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)
			
	#设置背景色
	#bg_color = (230, 230, 230)
	
	#创建一个外星人
	alien = Alien(ai_settings, screen)
		
	#开始游戏的主循环
	while True:		
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)	
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
				
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
		#gf.update_screen(ai_settings, screen, ship)

run_game()
