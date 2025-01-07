from typing import AsyncGenerator
import litellm

class BaseAgent_v1:
    def __init__(
        self,
        name: str,
        system_prompt: str,
        litellm_model: str = None,
        model_kwargs=None
    ):
        """Initialize an agent with a name, model name, system prompt, and optional functions.
        
        Args:
            name: Name of the agent
            litellm_model: Model identifier for litellm
            system_prompt: The system prompt to guide agent behavior
            model_kwargs: Optional generation parameters like temperature
        """
        self.name = name
        self.system_prompt = system_prompt
        self.model = litellm_model or "openai/gpt-4o"
        self.model_kwargs = model_kwargs or {
            "temperature": 0.2,
            "max_tokens": 1000
        }

    async def next_response(
        self,
        messages: list
    ) -> AsyncGenerator[str, None]:
        """Get next response as a stream.
        
        Args:
            messages: The conversation history
        
        Yields:
            Tokens from the response stream
        """
        response = await litellm.acompletion(
            model=self.model,
            messages=messages,
            stream=True,
            **self.model_kwargs
        )
        
        async for chunk in response:
            if token := chunk.choices[0].delta.content:
                yield token 