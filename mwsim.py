from random import choice
# from sys import argv
from glob import glob
import pygame

directory = 'C:/Program Files (x86)/Steam/steamapps/common/Morrowind'
directory_sfx = directory + '/Data Files/Sound/'

pygame.mixer.init()
pygame.mixer.Sound(directory + '/Data Files/Music/Battle/MW battle2.mp3').play(-1).set_volume(1/6)
pygame.mixer.Channel(1)

sfx = {
	'spell': 'Fx/magic/*',
	'voice': 'Vo/d/m/ATK_DM*',
}

def sfx_play(type: str) -> None:
	def p(filename: str) -> None:
		def queue(filename_: str) -> None:
			pygame.mixer.Channel(1).queue(pygame.mixer.Sound(filename_))
		def wait() -> None:
			while pygame.mixer.Channel(1).get_queue():
				pass
		wait()
		queue(filename)
	p(choice(glob(directory_sfx + sfx[type])))

# test
def test() -> None:
	for sfx_type in sfx:
		directory = directory_sfx + sfx[sfx_type]
		print(sfx_type, directory)
		for filename in glob(directory):
			print(sfx_type, filename)

test()
# main
print('main')

for _ in range(10):
	sfx_play('spell')
	sfx_play('voice')

print('done')
