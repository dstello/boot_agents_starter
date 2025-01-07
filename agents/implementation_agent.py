from agents.base_agent import BaseAgent
from .agent_factory import AgentFactory

IMPLEMENTATION_PROMPT = """
You are a skilled frontend developer specializing in HTML and CSS implementation.

You have access to the following functions:

<available_functions>
{
    "updateArtifact": {
    "description": "Update an artifact file which is HTML, CSS, or markdown with the given contents.",
    "parameters": {
        "type": "object",
        "properties": {
        "filename": {
            "type": "string",
            "description": "The name of the file to update."
        },
        "contents": {
            "type": "string",
            "description": "The markdown, HTML, or CSS contents to write to the file."
        }
        },
        "required": ["filename", "contents"]
    }
    }
}
</available_functions>

To use any function, generate a function call in JSON format, wrapped in \
<function_call> tags. For example:
<function_call>
{
    "name": "updateArtifact",
    "arguments": {
    "filename": "index.html",
    "contents": "<!DOCTYPE html>..."
    }
}
</function_call>

When making a function call, output ONLY the thought process and function call, \
then stop. Do not provide any additional information until you receive the function \
response.
"""

class ImplementationAgent(BaseAgent):
    """
    Subclass of BaseAgent specialized in implementing HTML/CSS components based on provided milestones.
    """

    def __init__(
        self,
        name: str = "Implementation Agent",
        litellm_model: str = "anthropic/claude-3-5-sonnet-latest",
        model_kwargs=None
    ):
        """Initialize the planning agent with default settings.
        
        Args:
            name: Name of the agent
            litellm_model: Model identifier for litellm
            model_kwargs: Optional generation parameters
        """
        super().__init__(
            name=name,
            system_prompt=IMPLEMENTATION_PROMPT,
            litellm_model=litellm_model,
            model_kwargs=model_kwargs
        )

# Register the agent with the factory
AgentFactory.register(ImplementationAgent)