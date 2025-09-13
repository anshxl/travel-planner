from crewai import Agent  # type: ignore

ANTHROPIC_MODEL = "claude-sonnet-4-20250514"

ResourceAgent = Agent(
    role="Travel Resource Organizer",
    goal="Organize flights, hotels, and user notes into a structured format",
    backstory=(
        "You are highly detail-oriented and care about clarity. "
        "You take raw user-entered travel details and structure them, "
        "so they are easy to display and export."
    ),
    llm=ANTHROPIC_MODEL,
    verbose=True,
    allow_delegation=False
)