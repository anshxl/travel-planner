# agents/crew_setup.py

from crewai import Crew, Task # type: ignore
from .main_agent import MainAgent
from .itinerary_agent import ItineraryAgent
from .resource_agent import ResourceAgent
from .media_agent import MediaAgent

def build_travel_crew():
    itinerary_task = Task(
        description="Plan a trip itinerary for a destination, dates, and preferences.",
        agent=ItineraryAgent,
        expected_output="A structured daily plan with activities and timing"
    )

    resource_task = Task(
        description="Organize flights, hotels, and user-provided notes into a structured plan.",
        agent=ResourceAgent,
        expected_output="A structured summary of flights, hotels, and notes"
    )

    media_task = Task(
        description="Fetch free image URLs for the itinerary’s activities and locations.",
        agent=MediaAgent,
        expected_output="A list of image URLs associated with itinerary activities"
    )

    main_task = Task(
        description="Orchestrate the itinerary, resources, and media into a complete trip plan.",
        agent=MainAgent,
        expected_output="A complete trip plan that combines itinerary, resources, and media"
    )

    travel_crew = Crew(
        agents=[MainAgent, ItineraryAgent, ResourceAgent, MediaAgent],
        tasks=[itinerary_task, resource_task, media_task, main_task],
        verbose=True
    )

    return travel_crew