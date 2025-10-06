from enum import Enum
from pydantic import BaseModel, Field
from pydantic import ValidationError


class ActivityLevel(str, Enum):
    # Primary activity levels as per solution proposal (1.4, 1.6, 1.8 multipliers)
    LIGHT = "light"
    MODERATE = "moderate"
    HIGH = "high"

class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"

class UserProfile(BaseModel):
    age: int = Field(..., ge=1, le=120, description="Age in years (1-120)")
    gender: Gender
    height: float = Field(..., gt=0, le=300, description="Height in cm (1-300)")
    weight: float = Field(..., gt=0, le=500, description="Current weight in kg (0.1-500)")
    activity_level: ActivityLevel

class MealPlanningContext(BaseModel):
    meal_type: str = Field(..., description="Type of meal (breakfast, lunch, dinner, snack)")
    cultural_adaptations: dict = Field(default_factory=dict, description="Cultural adaptation preferences")


MEAL_PLAN_USER_PROMPT_TEMPLATE = """
Create a {context.meal_type} meal for a {profile.age}-year-old {profile.gender.value} with {profile.activity_level.value} activity level.

Additional context:
- Current weight: {profile.weight}kg
- Height: {profile.height}cm  
- Cultural adaptations: {context.cultural_adaptations}

Make this meal culturally authentic, nutritionally balanced, and perfectly aligned with all dietary restrictions.
"""

try:
    user = UserProfile(
        age=30,
        gender=Gender.MALE,
        height=175.5,
        weight=70.2,
        activity_level=ActivityLevel.MODERATE
    )

    meal_context = MealPlanningContext(
        meal_type="lunch",
        cultural_adaptations={
                    "region": "North India",
                    "spice_level": "medium",
                    "vegetarian": False}
    )

    print(MEAL_PLAN_USER_PROMPT_TEMPLATE.format(
        profile=user,
        context=meal_context
    ))

except ValidationError as e:
    raise e