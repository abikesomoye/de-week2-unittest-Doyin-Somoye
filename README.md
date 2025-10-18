# Data Epic Mentoring Program
## Week 2: unittest

## The Challenge
You’re to design a prototype model for an Artificial Pancreas system. Your model receives inputs (carb intake, exercise) and outputs decisions (deliver insulin, warn low glucose, or maintain stability). You will create a class called ArtificialPancreasSystem that simulates basic glucose control using Python.

## Your Mission
In this assignment, you’ll step into the shoes of a Python programmer creating intelligence that cares.
You’ll build a simplified model that responds to glucose changes, exploring how data, logic, and human understanding can come together to support better outcomes.

You’ll analyze how glucose behaves after meals and exercise, design smart reactions to maintain balance, and test your system with structured, data-focused validation, just like you would when building a real-world predictive model.

### The Project: Artificial Pancreas System (APS)
A simplified Python model that simulates intelligent glucose regulation for people with diabetes. This prototype mimics how an artificial pancreas might respond to meals, exercise, and glucose fluctuations using basic logic and data-driven decisions.

**Project Overview**

Millions of people with diabetes make daily decisions about insulin, food, and activity. This system models how technology can support those decisions by:
+ Tracking glucose changes after meals and exercise
+ Predicting actions like insulin delivery or low-glucose warnings
+ Maintaining glucose stability within a healthy range

**Features**
+ meal(carbs): Simulates glucose increase after eating
+ exercise(duration): Simulates glucose decrease after physical activity
+ predict_action(): Decides whether to deliver insulin, warn about low glucose, or maintain stability
+ Tracks total insulin delivered
+ Prevents glucose from dropping below safe minimum (50 mg/dL)

**Testing**
Tests are written using pytest and cover:
+ Glucose changes after meals and exercise
+ Correct action prediction based on glucose level
+ Insulin tracking and glucose safety limits
+ Sequential event handling
+ Input validation for negative or non-numeric values


To run tests:
*pytest test_artificial_pancreas.py*

