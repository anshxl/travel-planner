from crewai import Agent  # type: ignore

ANTHROPIC_MODEL = "claude-sonnet-4-20250514"

ItineraryAgent = Agent(
    role="Itinerary Planning Agent",
    goal="Generate a day-by-day itinerary given destination, date range, and user preferences",
    backstory=(
        "You are an expert in travel logistics and local attractions. "
        "Based on the user’s destination, dates, pace, and interests, "
        "you propose a logical, exciting itinerary that balances travel, rest, and activities."
    ),
    llm=ANTHROPIC_MODEL,
    verbose=True,
    allow_delegation=False
)