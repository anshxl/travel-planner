# test_run.py
from agents.crew_setup import build_travel_crew
from dotenv import load_dotenv
load_dotenv()  # automatically loads variables from .env

import os
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("Missing Anthropic API key")

if __name__ == "__main__":
    crew = build_travel_crew()

    # Run a dummy example
    result = crew.kickoff(inputs={
        "destination": "Paris",
        "start_date": "2025-09-20",
        "end_date": "2025-09-25",
        "preferences": {
            "pace": "normal",
            "budget": "medium",
            "activity_types": ["sightseeing", "food"]
        },
        "flight": "AF 007, JFK to CDG",
        "hotel": "Hotel Lutetia",
        "notes": "Anniversary trip"
    })

    print("\n=== Crew Output ===")
    print(result)
