"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    }
}

# Additional activities
activities.update({
    "Soccer Team": {
        "description": "Outdoor team sport focusing on skills, fitness, and matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 22,
        "participants": ["noah@mergington.edu", "liam@mergington.edu"]
    },
    "Swimming Club": {
        "description": "Swim training and competitions for all levels",
        "schedule": "Mondays and Wednesdays, 5:00 PM - 6:30 PM",
        "max_participants": 18,
        "participants": ["ava@mergington.edu"]
    },
    "Art Club": {
        "description": "Exploring drawing, painting, and mixed media projects",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["isabella@mergington.edu"]
    },
    "Drama Society": {
        "description": "Acting, play production, and stagecraft",
        "schedule": "Fridays, 4:00 PM - 6:00 PM",
        "max_participants": 25,
        "participants": ["sophia@mergington.edu"]
    },
    "Debate Club": {
        "description": "Practicing argumentation, public speaking, and competitive debates",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 30,
        "participants": ["ethan@mergington.edu"]
    },
    "Math Olympiad": {
        "description": "Advanced problem solving and competition preparation",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["mia@mergington.edu"]
    }
})

# Additional sports, artistic, and intellectual activities
activities.update({
    "Basketball Team": {
        "description": "Competitive basketball training and inter-school matches",
        "schedule": "Mondays, Wednesdays, Fridays, 4:30 PM - 6:00 PM",
        "max_participants": 15,
        "participants": ["jack@mergington.edu", "noah@mergington.edu"]
    },
    "Track and Field": {
        "description": "Running, jumping, and throwing events with training sessions",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 25,
        "participants": ["liam@mergington.edu"]
    },
    "Photography Club": {
        "description": "Explore photography techniques, editing, and exhibitions",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["ava@mergington.edu"]
    },
    "Music Ensemble": {
        "description": "Instrumental and vocal ensemble rehearsals and performances",
        "schedule": "Tuesdays, 5:00 PM - 6:30 PM",
        "max_participants": 30,
        "participants": ["isabella@mergington.edu"]
    },
    "Science Club": {
        "description": "Hands-on experiments, science fairs, and research projects",
        "schedule": "Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["ethan@mergington.edu"]
    },
    "Robotics Club": {
        "description": "Designing, building, and programming robots for competitions",
        "schedule": "Fridays, 4:00 PM - 6:00 PM",
        "max_participants": 18,
        "participants": ["emma@mergington.edu"]
    }
})


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")
    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
