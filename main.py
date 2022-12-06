import pygame, sys, random, time
from pygame import display, event, font
 
pygame.init()
screen = display.set_mode((800, 550))
display.set_caption("Hangman!")

def display_message(message):
  screen.fill(yellow)

  text = word_font.render(message, True, blue)
  screen.blit(text, (280, 250))
  display.flip()
  time.sleep(3000)


yellow = (244,180,26)
blue = (20,61,89)
title_font = font.Font("font1.ttf", 70)
inst_font = font.Font("font2.ttf", 40)
word_font = font.Font("font2.ttf",  60)

words = ["biscuit", "brownie", "almonds"]
word = random.choice(words)
guessed = []
char = ""
hangman_tries = 5
 
while True:
  allevents = event.get()
  for myevent in allevents:
    if myevent.type == pygame.QUIT:
      sys.exit()
    if myevent.type == pygame.KEYDOWN:
      char = myevent.unicode
      if char in word:
        guessed.append(char)
      if char not in word:
        hangman_tries=hangman_tries-1

  screen.fill(yellow)
  text = title_font.render("HANGMAN", True,blue)
  screen.blit(text, (200, 150))
  instruction = inst_font.render("GUESS THE WORD", True, blue)
  screen.blit(instruction, (400, 50))

  won=True
  for ch in word:
    if ch not in guessed:
      won = False
      break

  if won == True:
    display_message("You won")
    break

  if hangman_tries == 0:
    display_message("Try again")
    break

  display_word = ""
  for ch in word:
    if ch in guessed:
      display_word = display_word+ch+" "
    else:
      display_word = display_word+"- "
  text = word_font.render(display_word, True, blue)
  screen.blit(text, (250, 300))

  tries = "Tries : " + str(hangman_tries)
  tries_text = inst_font.render(tries, True, blue)
  screen.blit(tries_text, (50, 50))

  display.flip()