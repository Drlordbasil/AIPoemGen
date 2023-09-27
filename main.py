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

        for word in words:
            if len(current_line) < line_length:
                current_line += word + " "
            else:
                lines.append(current_line[:-1])
                current_line = word + " "

        lines.append(current_line[:-1])

        return lines

    def get_random_web_service():
        pass
