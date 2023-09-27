Here is the README for the Python project based on the idea "AI Poet":
```vbnet
Title: AI Poet
Description: An AI-based tool that generates unique poems based on user input or existing poetry. The program relies solely on web APIs and libraries to function, without requiring any local files on the user's PC. It uses OpenAI GPT as a model for generating creative text.

How it works:
1. User inputs a topic or selects an existing poem from a database.
2. The AI Poet utilizes OpenAI GPT to generate a series of lines based on the input topic or poem.
3. The user can choose which lines they prefer, and the AI will continue generating new lines until the desired poem is complete.
4. Once the poem is finalized, it can be shared online or saved as a text file.

Python code using OpenAI GPT:
```python
import openai
from typing import Union
class Poet:
    def __init__(self):
        self.poem = ""
    
    def generate_lines(self, prompt: str) -> List[str]:
        model = openai.GPT(prompt=prompt)
        lines = model.generate(length=4)
        
        return [line for line in lines if len(line) > 0]
    
    def add_lines_to_poem(self, new_lines: List[str]) -> None:
        self.poem += "\n".join(new_lines)
``` and the provided program:
```python
import random
from collections import Counter
class PoemGenerator:
    def __init__(self):
        self.poetry_api = get_random_web_service()
    
    def generate_unique_poem(self, poem=None, style="Shakespearean"):
        if not poem:
            poem = read_existing_poem()
        
        words = self.split_words(poem)
        lines = self.generate_lines(words, style)
    
        return "\n".join(lines)
    
    def split_words(self, text):
        return [word for word in text.lower().split()]
    
    def generate_lines(self, words, style="Shakespearean"):
        line_length = get_line_length(style=style)
        
        lines = []
        current_line = ""
```