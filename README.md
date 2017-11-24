# PyRobo2D
A light weight 2-D robot simulator.
The target is to have a light weight, easy to use environment, that is evaluated fast. This is suitable for learning algorithms in particular,
like evolutionary algorithms and reinforcement learning.

## Todo list:
- [x] In the collision detection, change the symbolic equations solution (neat, but super slow) to hard-coded solution (ugly, but super fast!)
- [x] Add robot status class, where the environment can record information about (if selected) - all concatenated and normalized -:
    - The robot position
    - The robot orientations
    - The sensory readings for the robot
- [x] Build an agent class, that can interact with the environment
- [x] Fix the keyboard agent (broken at the moment)
    - Instead of making a special keyboard agent, I will just add an option in the window class to either take the keys from the agent or
    from the keyboard. The problem is that I need an active window in order to detect the keys.
- [x] Add a good abstraction for the 'game logic': what is the task?
    - This is the Finite State Machine of the game
    - It will depend a lot on the robot status message. It should not see inside the game engine
    - It will return a game over signal (to make an early shut down for the game) + a game score
        - Irrelevant: Add an option to penalize the score based on the time consumed.
        - The game score is an input to the game agent (is this format appropriate for reinforcement learning?)
            - Think about this point again.
- [x] Test the circle-to-circle collision detection
- [x] Prevent the robot from going passing environment objects (walls, balls)
- [ ] Test for parallel instances
- [x] Make a facility to record history for the robot readings. It will be useful later with reinforcement learning (for experience replay).
- [x] Subtract the sensor reading from the robot radius --> to correct the reading
- [x] Add 3 options for each object in the environment: visible, detectable and collidable
    - Visible means it will be drawn or not --> DONE
        - Assume that I am working with invisible window (for simulation purposes), do I need to draw things in the canvas? Should I disable all
        drawing?
            - NOP (Yay! This will accelerate things a lot! in simulation mode)
    - Detectable means sensors can detect it
    - Collidable means they prevent the robot from going further.
- [ ] Rename the window class to be the environment class
- [x] Make the agent generic (it doesn't see the dictionary of actions, only the number of actions needed)
- [x] Add a small function that builds walls surrounding the window
  - Will be done manually for now
- [ ] Create a special class for *maps*
- [x] Add a name for the class instance
- [ ] Enable adding noise to the sensors
    - The sensor can be randomly goes offline
    - The sensor can have false readings
- [ ] Integrate my NN into one of the agents and test it
- [x] Enable the removal of an object (a ball for example) during the game
- [ ] Restructure the collision detection in a nicer way.

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
