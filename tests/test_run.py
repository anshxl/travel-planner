# test_run.py
from agents.crew_setup import build_travel_crew

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
