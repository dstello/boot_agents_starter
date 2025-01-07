# LLM Agent Framework Starter

A starter project for building your own LLM agent framework with streaming, function calling, and agent delegation capabilities.

## Features

- **Streaming Support**: Built-in streaming for both raw responses and structured content (messages and XML tags)
- **Function Calling**: XML-based function calling system with automatic result handling
- **Agent Delegation**: Built-in support for delegating tasks to specialized agents
- **Artifact Management**: Automatic handling of text-based artifacts and image attachments
- **Chainlit Integration**: Ready-to-use integration with Chainlit for a beautiful chat interface

## Core Components

- `BaseAgent`: The foundation class implementing streaming, function calling, and delegation
- `MovieAgent`: An example implementation showing how to build specialized agents
- `app.py`: A Chainlit-based chat application showcasing the framework's capabilities

## Getting Started

1. Clone the repository
2. Copy `.env_sample` to `.env` and fill in your API keys
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the application:
   ```bash
   chainlit run app.py
   ```

## Key Features of BaseAgent

- **Streaming Response Processing**: 
  - `next_response()`: Get a single streamed response
  - `react_to()`: Auto-handle function calls and agent delegations
  - Support for XML tag processing and message content separation

- **Built-in Functions**:
  - `updateArtifact`: Create or update files in the artifacts directory
  - `saveImage`: Save images from the conversation to the artifacts directory

- **Artifact Management**:
  - Automatic inclusion of text-based artifacts in system context
  - Support for various file types including images

## Building Your Own Agent

1. Inherit from `BaseAgent`
2. Define your system prompt
3. Implement any custom functions
4. Register with `AgentFactory`

Example:
```python
class CustomAgent(BaseAgent):
    def __init__(self, name="Custom Assistant", litellm_model=None, model_kwargs=None):
        super().__init__(
            name=name,
            system_prompt=YOUR_SYSTEM_PROMPT,
            litellm_model=litellm_model,
            model_kwargs=model_kwargs
        )

    def custom_function(self, arg1, arg2):
        # Implement your function
        pass

AgentFactory.register(CustomAgent)
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

[MIT License](LICENSE) 