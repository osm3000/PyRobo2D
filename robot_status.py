class RobotStatus:
    def __init__(self, log_robot_pos=True, log_robot_sensors=True):
        self.log_robot_pos = log_robot_pos
        self.log_robot_sensors = log_robot_sensors
        self.robot_position = []
        self.robot_rotation = []
        self.robot_sensors_readings = []

    def __str__(self):
        final_string = "History length: " + str(len(self.robot_rotation)) + "\n"
        final_string += "Robot position: " + str(self.robot_position[-1]) + "\n"
        final_string += "Robot rotation: " + str(self.robot_rotation[-1]) + "\n"
        final_string += "Sensors: " + str(self.robot_sensors_readings[-1]) + "\n"
        return final_string
