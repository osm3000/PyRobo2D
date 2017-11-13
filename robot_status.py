class RobotStatus:
    def __init__(self, log_robot_pos=True, log_robot_sensors=True):
        self.log_robot_pos = log_robot_pos
        self.log_robot_sensors = log_robot_sensors

        #TODO: Instead of storing the info in separate variables, create one dictionary
        # self.robot_position = None
        # self.robot_rotation = None
        # self.robot_sensors_readings = None
        self.messages = dict(RobotPosition=None, RobotRotation=None, RobotSensorsReadings=None)

    # def __call__(self, robot_position, robot_rotation, robot_sensors_readings):
    def __call__(self, **kwargs):
        self.messages['RobotPosition'] = kwargs['RobotPosition']
        self.messages['RobotRotation'] = kwargs['RobotRotation']
        self.messages['RobotSensorsReadings'] = kwargs['RobotSensorsReadings']

    def __str__(self):
        final_string = ""
        for key in self.messages:
            final_string += key + ": " + str(self.messages[key]) + "\n"
        return final_string
