def main (): 
  n, l, c = map(int, input().split())
  count = 0
  line = 0
  page = 0
  words = ''

  def random_word_generate(min_length = 3, max_length = 10):
    import random
    import string
    length = random.randint(min_length, max_length)
    return ''.join(random.choices(string.ascii_lowercase, k=length))
  
  for i in range(n):
    words += random_word_generate() + ' '


  print(words)
  print(len(words))

  line = count / c
  
  print(line)
  print(page)

if __name__ == '__main__':
  while True:
    try:
      main()
    except EOFError:
      break