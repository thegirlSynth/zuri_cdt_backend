class ObstructionDetector:
    def __init__(self, speed, distance):
        self.speed = speed
        self.distance = distance
    
    def calculate_expected_time(self):
        expected_time = (self.distance / self.speed) * 60
        return expected_time
    
    def check_obstruction(self, actual_time):
        expected_time = self.calculate_expected_time()

        if actual_time > expected_time + 60:
            return True
        else:
            return False
