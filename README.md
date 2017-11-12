# PyRobo2D
A light weight 2-D robot simulator.
The target is to have a light weight, easy to use environment, that is evaluated fast. This is suitable for learning algorithms in particular,
like evolutionary algorithms and reinforcement learning.

## Todo list:
* [X] In the collision detection, change the symbolic equations solution (neat, but super slow) to hard-coded solution (ugly, but super fast!)
* [ ] Add robot status class, where the environment can record information about (if selected):
    * The robot position
    * The robot orientations
    * The sensory readings for the robot
* [ ] Build an agent class, that can interact with the environment
* [ ] Rename the window class to be the environment class
* [ ] Add a good abstraction for the 'game logic': what is the task?
* [ ] Test the circle-to-circle collision detection
* [ ] Prevent the robot from going passing environment objects (walls, balls)
* [ ] test for parallel instances
* [ ] Enable adding noise to the sensors
    * The sensor can be randomly goes offline
    * The sensor can have false readings
* [ ] Make a facility to record history for the robot readings. It will be useful later with reinforcement learning (for experience replay).

## Questions:
* Should the reading of the sensors be stored in the sensors instances? or in the robot instance? or just pass them directly to the robot status?

## Plans for the future:
* Unify all the elements in the environment under one base class.
* Unify the robot and the ball under one base class (Ball class). The robot is technically an extension of the Ball class.
* Investigate if using a physics engine, like *pymunk*, adds a lot of overhead to the system
    * The use of a physics engine will greatly reduce the coding needed to collision detection.
* Enable the robots to exchange messages (for the future test of the evolution of language)
* Unify all the data types to be numpy arrays
     * This will enable me to use *numba* to accelerate some parts, most importantly, the collision detection
