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
                        break # No need to continue the for loop

                elif 'basket' in keys[1].lower():
                    if self.game_fsm['ball_collected'] == True:
                        if robot_status.collisions[-1][keys] == True:
                            self.game_fsm['ball_scored'] = True
                            self.game_over = True
                            self.game_score += 10
                            break # No need to continue the for loop
        return self.game_over, self.game_score
