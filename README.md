# SimulatedMazeSearching
This project uses the generalized adaptive A* search algorithm developed by Sven Koenig in order to perform repeated fast-trajectory planning.  This search algorithm uses information from previous searches in order to inform future ones, therefore making each subsequent search increasingly more efficient.  The search uses the heuristic properties of the normal A* algorithm but makes it more consistent.  For more information on the algorithm itself or to read Koenig's research paper on the topic, see the information below:

X. Sun, S. Koenig and W. Yeoh. Generalized Adaptive A*. In Proceedings of the International Joint Conference on Autonomous Agents and Multiagent Systems (AAMAS), pages 469-476, 2008

http://idm-lab.org/bib/abstracts/papers/aamas08b.pdf


LOGISTICS FOR IMPLEMENTATION:

1 The path name for the board to be tested (all boards stored in a sub-folder titled "tests") must be changed at the top of the source code file (located in "src") as well as the (x, y) coordinates of the agent and target in question

2 The folder "iterations", which stores every iteration of the search algorithm after it has found a percieved path and the new position(s) of the agent, must be wiped empty before running a new board otherwise.  Each iteration is represented as a text file with "X" representing blocked cells and "O" representing unblocked cells
