def main():
  n1, n2 = map(int, input().split())
  print(n1 ^ n2)

if __name__ == '__main__':
  while True:
    try:
      main()
    except EOFError:
      break