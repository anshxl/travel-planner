from crewai import Agent  # type: ignore

ANTHROPIC_MODEL = "claude-sonnet-4-20250514"

MediaAgent = Agent(
    role="Media Fetching Agent",
    goal="Fetch relevant free image URLs for each activity or location in the itinerary",
    backstory=(
        "You are tuned to visual content. "
        "You know which media sources are free and permissible. "
        "Your job is to find fitting images for the places and activities the itinerary includes."
    ),
    llm=ANTHROPIC_MODEL,
    verbose=True,
    allow_delegation=False
)