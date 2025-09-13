from crewai import Agent # type: ignore

ANTHROPIC_MODEL = "claude-sonnet-4-20250514"

MainAgent = Agent(
    role="Coordinator Agent",
    goal="Manage the itinerary, resource, and media agents to produce a full trip plan",
    backstory=(
        "You are a seasoned travel planner coordinator. "
        "You take user inputs (destination, dates, preferences), "
        "call on sub-agents to plan the trip, gather resources, and fetch media, "
        "and then merge all results into a final polished plan."
    ),
    llm=ANTHROPIC_MODEL,
    verbose=True,
    allow_delegation=False
    )