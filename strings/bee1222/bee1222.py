import random
import string

def main (): 
  n, l, c = map(int, input().split())
  words = ''
  debugWords = "a de i de o"

  def random_word_generate(min_length = 3, max_length = 10):
    length = random.randint(min_length, max_length)
    return ''.join(random.choices(string.ascii_lowercase, k=length))

  def page_counter(words, l, c): # "a de i de o", 2, 2
    words = words.split() # ['a', 'de', 'i', 'de', 'o']
    line = 1
    current_line = ''
    iteration = 1

    for word in words:
      print(f"{iteration} iteração do for") # 1 | 2
      print("tamanho da linha atual: ", len(current_line)) # 0 | 1
      print("tamanho da palavra: ", len(word)) # 1 | 2
      print("palavra: ", word) # 'a' | 'de'
      iteration += 1 # iteração = 2 | iteracao = 3 

      if len(word) + len(current_line) + (1 if current_line else 0) > c: # False | True
        line += 1 # line = 2
        current_line = word #current_line = 'de'
      else:
        current_line = (current_line + ' ' + word) if current_line else word # current_line = 'a' | 

    print("fora do for o currentLine: ", current_line, len(current_line))
    print("fora do for o line: ", line)
    if current_line:
      line += 1

  
  for i in range(n):
    words += random_word_generate() + ' '

  page_counter(debugWords, 2, 2)

if __name__ == '__main__':
  while True:
    try:
      main()
    except EOFError:
      break