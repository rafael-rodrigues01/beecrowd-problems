import random
import string
import math

def main (): 
  n, l, c = map(int, input().split())
  story = input().strip()

  def page_counter(story, l, c): 
    words = story.split() 
    line = 0
    current_line = ''

    for word in words:

      if len(word) + len(current_line) + (1 if current_line else 0) > c: 
        line += 1 
        current_line = word 
      else:
        current_line = (current_line + ' ' + word) if current_line else word 

    if current_line:
      line += 1

    return line

  page = math.ceil(page_counter(story, l, c) / l)
  print(page)

if __name__ == '__main__':
  while True:
    try:
      main()
    except EOFError:
      break