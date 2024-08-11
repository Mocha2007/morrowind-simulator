from random import choice
# from sys import argv
from glob import glob
import pygame

directory = 'C:/Program Files (x86)/Steam/steamapps/common/Morrowind'
directory_sfx = directory + '/Data Files/Sound/'

pygame.mixer.init()
pygame.mixer.Channel(0)
pygame.mixer.Sound(directory + '/Data Files/Music/Battle/MW battle2.mp3').play(-1).set_volume(1/6)
pygame.mixer.set_num_channels(4)
n_channels = pygame.mixer.get_num_channels() - 1

sfx = {
	'health': 'Fx/magic/restH.wav',
	'spell': 'Fx/magic/*',
	'voice': 'Vo/d/m/ATK_DM*',
}

sfx_n = 0
def sfx_play(type: str) -> None:
	global sfx_n
	channel = pygame.mixer.Channel(sfx_n % n_channels + 1) # or pygame.mixer.find_channel() or pygame.mixer.Channel(list(sfx).index(type) + 1)
	def p(filename: str) -> None:
		def queue(filename_: str) -> None:
			channel.queue(pygame.mixer.Sound(filename_))
			print(filename_)
		def wait() -> None:
			while channel.get_queue():
				pass
		wait()
		queue(filename)
	p(choice(glob(directory_sfx + sfx[type])))
	sfx_n += 1

# test
def test() -> None:
	for sfx_type in sfx:
		directory = directory_sfx + sfx[sfx_type]
		print(sfx_type, directory)
		for filename in glob(directory):
			print(sfx_type, filename)

# test()
# main
print('*enters combat*')

for _ in range(100):
	try:
		sfx_play('health')
		# sfx_play('spell')
		sfx_play('voice')
	except FileNotFoundError:
		pass

print('done')
