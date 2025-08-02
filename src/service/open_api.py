"""A module provides a function to complete a prompt with OpenAI's model."""
import logging
from typing import Optional

from openai import AsyncOpenAI
from openai.types.chat import ChatCompletion

from config.config import settings


logger: logging.Logger = logging.getLogger(__name__)


class OpenAIService:
    def __init__(self, api_key: str = settings.openapi_key) -> None:
        self.client = AsyncOpenAI(api_key=api_key)
    
    async def complete_prompt(
        self,
        prompt: str,
        model: str = "gpt-3.5-turbo",
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
    ) -> str:
        """
        Complete a prompt using OpenAI's chat completion.
        
        Args:
            prompt: The prompt to complete.
            model: The model to use for completion.
            temperature: Controls randomness (0.0 to 2.0).
            max_tokens: Maximum number of tokens to generate.
            
        Returns:
            The completed text.
        """
        try:
            completion: ChatCompletion = await self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=model,
                temperature=temperature,
                max_tokens=500,
            )
            return completion.choices[0].message.content or ""
        except Exception as e:
            logger.error(f"Error in OpenAI completion: {e}")
            return "Sorry, I encountered an error processing your request."
        
open_api_service = OpenAIService()