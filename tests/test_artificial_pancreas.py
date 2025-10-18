import pytest
from artificial_pancreas import ArtificialPancreasSystem  

# Fixture to create a fresh system for each test
@pytest.fixture
def system():
    return ArtificialPancreasSystem(glucose_level=100, insulin_sensitivity=1.0)

# Core behavior tests
def test_glucose_increases_after_meal(system):
    before = system.glucose_level
    system.meal(20)
    after = system.glucose_level
    assert after > before

def test_glucose_decreases_after_excercise(system):
    system.meal(40)
    before = system.glucose_level
    system.exercise(30)
    after = system.glucose_level
    assert after < before

def test_glucose_never_below_min(system):
    system.exercise(500)
    assert system.glucose_level >= 50

# Decision logic tests
def test_action_deliver_insulin(system):
    system.glucose_level = 120
    action, _ = system.predict_action()
    assert action == "deliver_insulin"

def test_action_warn_low_glucose(system):
    system.glucose_level = 80
    action, _ = system.predict_action()
    assert action == "warn_low_glucose"

def test_action_maintain(system):
    system.glucose_level = 105
    action, _ = system.predict_action()
    assert action == "maintain"

# Insulin tracking test
def test_total_insulin_tracking(system):
    system.total_insulin_delivered = 0  # Make sure this attribute exists in your class
    system.glucose_level = 130
    system.predict_action()
    expected_dose = (130 - system.target_glucose) * system.insulin_sensitivity
    assert system.total_insulin_delivered == expected_dose

# Sequential event test
def test_sequential_events(system):
    system.meal(40)
    system.exercise(20)
    action, level = system.predict_action()
    assert action in ["deliver_insulin", "maintain", "warn_low_glucose"]
    assert 50 <= level <= 150

# Invalid input tests
def test_negative_carbs(system):
    with pytest.raises(ValueError):
        system.meal(-10)

def test_negative_exercise(system):
    with pytest.raises(ValueError):
        system.exercise(-5)

def test_non_numeric_carbs(system):
    with pytest.raises(TypeError):
        system.meal("ten")

def test_non_numeric_exercise(system):
    with pytest.raises(TypeError):
        system.exercise("thirty")
