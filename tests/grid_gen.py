import random
import sys
import png

def main():

  for i in range(50):
    grid_arr = buildGrid(i)
    buildPNG(grid_arr, i)

def isBlocked():
  random_number = random.randint(1, 10)

  if random_number <= 3:
    return 1
  else:
    return 0

def buildGrid(file_number):
  arr = [[0]*101 for _ in range(101)]
  i = 0
  j = 0

  file_name = "grid" + str(file_number).zfill(2) + ".txt"
  f = open(file_name, "w+")

  for row in arr:
    j = 0
    for col in row:
      if isBlocked() == 1:
        f.write("X")
        arr[i][j] = 0
      else:
        f.write("O")
        arr[i][j] = 1
      j = j + 1
    i = i + 1
    f.write("\n")

  f.close()
  return arr

def buildPNG(arr, file_number):
  file_name = "grid" + str(file_number).zfill(2) + ".png"
  arr = map(lambda x: map(int, x), arr)

  f = open(file_name, 'wb')
  w = png.Writer(len(arr[0]), len(arr), greyscale=True, bitdepth=1)
  w.write(f, arr)
  f.close()

if __name__=="__main__":
  main()








