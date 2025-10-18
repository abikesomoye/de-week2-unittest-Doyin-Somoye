
class ArtificialPancreasSystem:
    """A simplified model for data-driven glucose regulation."""

    GLUCOSE_PER_CARB = 0.5       # fixed increase per carb unit
    GLUCOSE_BURN_PER_MIN = 0.3   # fixed decrease per minute of exercise

    def __init__(self, glucose_level, insulin_sensitivity=1.0, target_glucose=100, tolerance=10):
        self.glucose_level = glucose_level
        self.insulin_sensitivity = insulin_sensitivity
        self.target_glucose = target_glucose
        self.tolerance = tolerance 
    
    def meal(self, carbs: float):
        self.glucose_level += carbs * self.GLUCOSE_PER_CARB
        return self.glucose_level
    
    def exercise(self, duration: float):
        self.glucose_level -= duration * self.GLUCOSE_BURN_PER_MIN
        if self.glucose_level < 50:
            self.glucose_level = 50
        return self.glucose_level
    
    def predict_action(self):
        if self.glucose_level > self.target_glucose + self.tolerance:
            action = "deliver_insulin"
            dose = (self.glucose_level - self.target_glucose) * self.insulin_sensitivity
            self.glucose_level -= dose
        elif self.glucose_level < self.target_glucose - self.tolerance:
            action = "warn_low_glucose"
        else:
            action = "maintain"
        
        return action, self.glucose_level 


controller = ArtificialPancreasSystem(100, 1.0, 100, 10 )
controller.meal(40)
controller.exercise(20)
action, level = controller.predict_action()
print(action, level)

