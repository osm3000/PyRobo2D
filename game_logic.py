"""
Here, I put the different classes descriping differnt games that I want to test.
Each game logic should have the appropriate maps
Game logic only sees the full robot status. It doesn't see anything else in the game engine. It return a signal when the game (finite state
machine) is done.
"""
class GameLogicBase:
    def __init__(self):
        self.game_fsm = {}
        self.game_over = False
        self.game_score = 0
        self.env_changes = {}

    def update_fsm(self, robot_status):
        raise (NotImplemented)

class Collect_Ball_Simple(GameLogicBase):
    """
    The target here is to collect one ball only, and put it in the basket.
    """
    def __init__(self):
        super(Collect_Ball_Simple, self).__init__()
        self.game_fsm['ball_collected'] = False
        self.game_fsm['ball_scored'] = False

    def update_fsm(self, robot_status):
        if not self.game_over:
            for keys in robot_status.collisions[-1]:
                # I only need to check on the 2nd term on the key, to see if it is a ball or not
                if 'ball' in keys[1].lower():
                    if robot_status.collisions[-1][keys] == True:
                        self.game_fsm['ball_collected'] = True
                        self.env_changes['remove'] = [keys[1]]
                        break # No need to continue the for loop

                elif 'basket' in keys[1].lower():
                    if self.game_fsm['ball_collected'] == True:
                        if robot_status.collisions[-1][keys] == True:
                            self.game_fsm['ball_collected'] = False
                            self.game_fsm['ball_scored'] = True

                            self.game_over = True
                            self.game_score += 10
                            break # No need to continue the for loop
        return self.game_over, self.game_score, self.env_changes

class Collect_Ball_Full(GameLogicBase):
    """
    The target here is to collect one ball only, and put it in the basket.
    """
    def __init__(self, max_balls=4):
        super(Collect_Ball_Full, self).__init__()
        self.game_fsm['ball_collected'] = False
        self.game_fsm['ball_scored'] = False
        self.nb_balls_collected = 0
        self.max_balls = max_balls

    def update_fsm(self, robot_status):
        if not self.game_over:
            for keys in robot_status.collisions[-1]:
                # I only need to check on the 2nd term on the key, to see if it is a ball or not
                if 'ball' in keys[1].lower():
                    if not self.game_fsm['ball_collected']:
                        if (robot_status.collisions[-1][keys] == True):
                            self.game_fsm['ball_collected'] = True
                            self.env_changes['remove'] = [keys[1]]
                            break # No need to continue the for loop

                elif 'basket' in keys[1].lower():
                    if self.game_fsm['ball_collected'] == True:
                        if robot_status.collisions[-1][keys] == True:
                            self.game_fsm['ball_collected'] = False
                            self.game_fsm['ball_scored'] = True

                            self.game_score += 10
                            self.nb_balls_collected += 1

                            if self.nb_balls_collected == self.max_balls:
                                self.game_over = True

                            break # No need to continue the for loop
        return self.game_over, self.game_score, self.env_changes
