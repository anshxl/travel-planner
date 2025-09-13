# agents/crew_setup.py

from crewai import Crew, Task # type: ignore
from .main_agent import MainAgent
from .itinerary_agent import ItineraryAgent
from .resource_agent import ResourceAgent
from .media_agent import MediaAgent

def build_travel_crew():
    # Define tasks for each agent
    itinerary_task = Task(
        description="Plan a trip itinerary for a destination, dates, and preferences.",
        agent=ItineraryAgent,
    )

    resource_task = Task(
        description="Organize flights, hotels, and user-provided notes into a structured plan.",
        agent=ResourceAgent,
    )

    media_task = Task(
        description="Fetch free image URLs for the itinerary’s activities and locations.",
        agent=MediaAgent,
    )

    # Main agent pulls everything together
    main_task = Task(
        description="Orchestrate the itinerary, resources, and media into a complete trip plan.",
        agent=MainAgent,
    )

    # Crew orchestrates the tasks
    travel_crew = Crew(
        agents=[MainAgent, ItineraryAgent, ResourceAgent, MediaAgent],
        tasks=[itinerary_task, resource_task, media_task, main_task],
        verbose=True
    )

    return travel_crew
