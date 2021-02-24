# by Kami Bigdely
# Extract class
class Cooked:

    WELL_DONE = 3000
    MEDIUM = 2500
    COOKED_CONSTANT = 0.05
    
    def __init__(self, desired_state):
        self.desired_state = desired_state
        

    @classmethod
    def level(cls):
        if desired_state == 'well-done':
            return cls.WELL_DONE
        elif desired_state == 'medium':
            return cls.MEDIUM
        else:
            raise ValueError('this is raw')

    def get_progress(self, time, temperature, pressure):
        self.progress = time * temperature * pressure * self.COOKED_CONSTANT
        return self.is_criteria_satisfied()

    def is_criteria_satisfied(self):
        if self.progress >= self.level():
            print('cooking is done.')
        else:
            print('ongoing cooking.')
        return


# def is_cookeding_criteria_satisfied(time, temperature, 
#                                     pressure, desired_state):
#     return is_well_done(time, temperature, pressure, desired_state) or \
#            is_medium(time, temperature, pressure, desired_state)


# def is_well_done(time, temperature, pressure, desired_state):    
#     return desired_state == 'well-done' and  \
#            get_cooking_progress(time, temperature, pressure) >= WELL_DONE


# def is_medium(time, temperature, pressure, desired_state):
#     return desired_state == 'medium' and  \
#            get_cooking_progress(time, temperature, pressure) >= MEDIUM

# def get_cooking_progress(time, temperature, pressure):
#     return time * temperature * pressure * COOKED_CONSTANT


time = 30 # [min]
temp = 103 # [celcius]
pressure = 20 # [psi]
desired_state = 'well-done'

cooked = Cooked(desired_state)
cooked.get_progress(time, temp, pressure)


# if is_cookeding_criteria_satisfied(time, temp, pressure, desired_state):
#     print('cooking is done.')
# else:
#     print('ongoing cooking.')