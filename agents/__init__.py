"""
Agent package initialization.
This module automatically imports and registers all available agents.
"""

# First, import the base components
from .base_agent import BaseAgent
from .agent_factory import AgentFactory

# Import all specialized agents
from .movie_agent import MovieAgent
from .movie_reviews_agent import MovieReviewsAgent
from .implementation_agent import ImplementationAgent
from .planning_agent import PlanningAgent
from .supervisor_agent import SupervisorAgent

# Expose the main classes and agents for easy access
__all__ = [
    # Core components
    'BaseAgent',
    'AgentFactory',
    
    # Specialized agents
    'MovieAgent',
    'MovieReviewsAgent',
    'ImplementationAgent',
    'PlanningAgent',
    'SupervisorAgent',
]

# Note: Registration happens automatically when each agent module is imported
# because AgentFactory.register() is called at the module level in each agent file.