import heapq

expanded_cell_count = 0
itera = 0 

start_x = 0
start_y = 0
goal_x = 0
goal_y = 0

counter = 0
pathcost = {}
know_grid = [[0]*101 for _ in range(101)] # array of type State
org_grid = [[0]*101 for _ in range(101)] # int array, 1=blocked,0=unblocked
CLOSED = {}
path = []

class State:
  def __init__(self,g,h,f,parent,search,x,y,isBlocked):
    self.g = g
    self.h = h
    self.f = f
    self.parent = parent
    self.search = search
    self.x = x
    self.y = y
    self.isBlocked = isBlocked

  # implementation : node_name in heap_name -> returns T/F - WORKS
  def __eq__(self, other):
    return (self.x == other.x) and (self.y == other.y)

  # used to structure the heap according to f-values - WORKS :)
  def __cmp__(self, other):
    return cmp(self.f, other.f)

def pop(heap):

  output = heapq.heappop(heap)
  temp_list = list()

  if any(node.f == output.f for node in heap):
    while any(node.f == output.f for node in heap):
      # compare g-values
      temp_1 = heapq.heappop(heap)
      if temp_1.g > output.g: # CHANGE HERE FOR less than
        temp_2 = output
        output = temp_1
        temp_list.append(temp_2)
      else:
        temp_list.append(temp_1)

  # pushing all elements back into heap
  while len(temp_list) != 0:
    heapq.heappush(heap, temp_list.pop())
  return output

def InitializeState(s): # s is a state
  global goal_x
  global goal_y
  global counter
  global pathcost # hashtable

  if s.search == 0:
    s.h = abs((s.x - goal_x)) + abs((s.y - goal_y)) # manhattan distance
    s.g = float("inf")
  elif s.search != counter:
    if s.g + s.h < pathcost.get(s.search): # updated heuristic
      s.h = pathcost.get(s.search) - s.g
    s.g = float("inf")
  s.search = counter

def CleanForwardPath(start_state,goal_state):
  global itera#THIS BLOCK
  newpath = "/Users/aarti/Desktop/ai_pa1/src/iterations/iteration" + str(itera) + ".txt"
  ptr = goal_state
  finalPath(newpath,goal_state.x,goal_state.y,'T')
  finalPath(newpath,start_state.x,start_state.y,'A')
  while ptr is not None and (ptr.x != start_state.x or ptr.y != start_state.y):
    finalPath(newpath,ptr.x,ptr.y,'_')
    ptr2 = ptr.parent
    ptr.parent = None
    ptr = ptr2


def findPath(start_state, goal_state):
  global path
  ptr = know_grid[goal_state.y][goal_state.x]
  while ptr.x != start_state.x or ptr.y != start_state.y:
    path.insert(0, ptr)
    ptr = ptr.parent


def ComputePath(start_state):
  global goal_x
  global goal_y
  global pathcost # key=counter,val=s.g+s.h
  global counter
  global know_grid
  global CLOSED

  OPEN = []
  heapq.heappush(OPEN, start_state)

  while len(OPEN) != 0:
    s = pop(OPEN)
    CLOSED.update({(s.x,s.y) : s})

    if (s.x == goal_x and s.y == goal_y):
      pathcost.update({counter : (s.g + s.h)})
      return True

    i = 1 # evaluate all succ of s
    while i < 5:
      if i == 1: # north
        succ_x = s.x
        succ_y = s.y + 1
      if i == 2: # east
        succ_x = s.x + 1
        succ_y = s.y
      if i == 3: # south
        succ_x = s.x
        succ_y = s.y - 1
      if i == 4: # west
        succ_x = s.x - 1
        succ_y = s.y

      if succ_x > 100 or succ_x < 0 or succ_y > 100 or succ_y < 0: # not in-bounds
        i = i + 1
        continue
      
      succ = know_grid[succ_y][succ_x] # succ = successor

      if succ.isBlocked == 1: # blocked
        i = i + 1
      else:
        InitializeState(succ) # initializes the appropriate h val
        if succ.g > s.g + 1:
          succ.g = s.g + 1
          succ.parent = s
          succ.f = succ.g + succ.h
          if succ in OPEN:
            OPEN.remove(succ)
          heapq.heappush(OPEN, succ) # push succ to OPEN
        i = i + 1

  return False

def updateGrid(x, y):
  global org_grid
  global know_grid

  i = 1
  while i < 5:
    if i == 1: # north
      neigh_x = x
      neigh_y = y + 1
    if i == 2: # east
      neigh_x = x + 1
      neigh_y = y
    if i == 3: # south
      neigh_x = x
      neigh_y = y - 1
    if i == 4: # west
      neigh_x = x - 1
      neigh_y = y

    # checks that index is within range
    if neigh_x > 100 or neigh_x < 0 or neigh_y > 100 or neigh_y < 0:
      i = i + 1
      continue
    if org_grid[neigh_y][neigh_x] == 1:
      know_grid[neigh_y][neigh_x].isBlocked = 1

    i = i + 1


def main():
  global counter
  global start_x
  global start_y
  global goal_x
  global goal_y
  global path
  global expanded_cell_count
  final_path = []

  counter = counter + 1
  ogfile = "/Users/aarti/Desktop/ai_pa1/tests/grid13.txt"
  txt_file = open(ogfile, "r")
  fl = txt_file.readlines() 

  # coordinates
  start_x = start_x + 0
  start_y = start_y + 0
  goal_x = goal_x + 100
  goal_y = goal_y + 100
  
  fpath = "/Users/aarti/Desktop/ai_pa1/src/iterations/final.txt"
  grid = open(ogfile,"r")
  blocks = grid.read()
  grid.close()
  p5 = open(fpath,'w+')
  p5.write(blocks)
  p5.close() #THIS BLOCK

  finalPath(fpath,start_x,start_y,'A')
  finalPath(fpath,goal_x,goal_y,'T')
  
  finalPath(fpath,start_x,start_y,'A')
  finalPath(fpath,goal_x,goal_y,'T')#THIS BLOCK

  # lines 40-43 pseudocode (setting state attributes)
  i = 0
  j = 0
  for row in org_grid:
    j = 0
    for col in row:
      # (g,h,f,parent,search,x,y,isBlocked)
      know_grid[i][j] = State(None,None,None,None,0,j,i,0)
      if fl[i][j] == "O":
        org_grid[i][j] = 0
      else:
        org_grid[i][j] = 1
      j = j+1
    i = i+1

  txt_file.close()

  # while start != goal
  while start_x != goal_x or start_y != goal_y:
    
    global itera #THIS BLOCK
    itera = itera+1  
    newpath = "/Users/aarti/Desktop/ai_pa1/src/iterations/iteration" + str(itera) + ".txt"
    p1 = open(ogfile,"r")
    blocks = p1.read()
    p1.close()
    p2 = open(newpath,'w')
    p2.write(blocks)
    p2.close() 
   
    start_state = know_grid[start_y][start_x]
    goal_state = know_grid[goal_y][goal_x]

    InitializeState(start_state)
    InitializeState(goal_state)
    CleanForwardPath(start_state,goal_state)

    updateGrid(start_x,start_y)


    start_state.g = 0
    start_state.f = start_state.g + start_state.h

    if ComputePath(start_state) == False:
      print "goal is not reachable"
      expanded_cell_count = expanded_cell_count + len(CLOSED)
      print "expanded cell count : ", expanded_cell_count
      return

    findPath(start_state,goal_state)

    for element in path:
      if know_grid[element.y][element.x].isBlocked == 0:
        start_x = element.x # "moves" start one spot, i.e. reassigns val
        start_y = element.y
	updateGrid(element.x,element.y)
        final_path.append(element)
      else: # is blocked
        updateGrid(element.x,element.y)
        del path[:] # clears path list
        break

    counter = counter + 1

  expanded_cell_count = expanded_cell_count + len(CLOSED)
  printList(final_path)
  createBoard(fpath,final_path,ogfile) #THIS BLOCK [LINE]
  
  print "expanded cell count : ", expanded_cell_count

def findIndex(x,y):#THIS BLOCK
  return ((y*102)+x+1)-1

def finalPath(path,x,y,var):#THIS BLOCK
  grid = open(path, "r")
  blocks = grid.read()
  grid.close()
  cList = list(blocks)
  index = findIndex(x,y)
  if (cList[index] == 'T') or (cList[index] == 'A'):
    return
  else:
    cList[index] = var
  new = ""
  for x in cList:
    new += x
  path = open(path,'w')
  path.write(new)
  path.close()

def createBoard(path,coord,ogfile):#THIS BLOCK
  #create basic board
  ind = 1
  grid = open(ogfile, "r")
  blocks = grid.read()
  grid.close()
  cList = list(blocks);
  for element in coord:
    if ind == 1:
      index = findIndex(element.x,element.y)
      cList[index] = 'A'
    elif ind == len(coord):
      index = findIndex(element.x,element.y)
      cList[index] = 'T'
    else:
      index = findIndex(element.x,element.y)
      cList[index] = '_'
    ind = ind + 1
  new = ""
  for x in cList:
    new += x
  path5 = open(path,'w')
  path5.write(new)
  path5.close()


def printList(l):
  for x in l:
    print x.x, ", ", x.y

if __name__ == "__main__":
  main()

