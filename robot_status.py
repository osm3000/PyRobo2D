class RobotStatus:
    def __init__(self, log_robot_pos=True, log_robot_sensors=True, properties={}):
        self.log_robot_pos = log_robot_pos
        self.log_robot_sensors = log_robot_sensors
        self.robot_position = []
        self.robot_rotation = []
        self.robot_sensors_readings = []
        self.collisions = []
        self.ball_collect = []
        self.game_over = False
        self.game_score = 0

        self.properties = properties
        if len(self.properties.keys()) == 0:
            self.properties['position']  = True
            self.properties['rotation']  = True
            self.properties['sensors']   = True
            self.properties['collision'] = False
            self.properties['ball_flag'] = True

    def __str__(self):
        final_string = "History length: " + str(len(self.robot_rotation)) + "\n"
        final_string += "Robot position: " + str(self.robot_position[-1]) + "\n"
        final_string += "Robot rotation: " + str(self.robot_rotation[-1]) + "\n"
        final_string += "Sensors: " + str(self.robot_sensors_readings[-1]) + "\n"
        final_string += "Collisions: " + str(self.collisions[-1]) + "\n"
        final_string += "Ball Falg: " + str(self.ball_collect[-1]) + "\n"
        return final_string

    def get_robot_status(self):
        robot_status_vector = []
        # print ("self.ball_collect: ", self.ball_collect[-1])
        if self.properties['position']:
            robot_status_vector += self.robot_position[-1]
        if self.properties['rotation']:
            robot_status_vector += [self.robot_rotation[-1]]
        if self.properties['sensors']:
            robot_status_vector += self.robot_sensors_readings[-1]
        if self.properties['ball_flag']:
            # robot_status_vector += [self.ball_collect[-1]]
            robot_status_vector += [int(self.ball_collect[-1])]

        return robot_status_vector
