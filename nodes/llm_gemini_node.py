from .base_node import BaseNode
from crewai import LLM
import os

class LlmGemini(BaseNode):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_key": ("STRING", {"default": os.getenv("GEMINI_API_KEY")}),
            },
            "optional": {
                "model": ("STRING", {
                    "default": "gemini-2.5-flash"
                }),
            }
        }

    RETURN_TYPES = ("CREWAI_LLM",)
    RETURN_NAMES = ("llm",)

    FUNCTION = "create_llm"
    CATEGORY = "📎CrewAI/LLM" # Changed category for better organization

    def create_llm(self, model, api_key):
        llm = LLM(model=model, api_key=api_key)
        return (llm,)
