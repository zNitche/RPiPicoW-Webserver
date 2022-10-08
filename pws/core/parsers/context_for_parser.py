from pws.core.parsers.parser_base import ParserBase
import random


class ContextForParser(ParserBase):
    def __init__(self):
        super().__init__()

        self.begin_pattern = "{%for%}"
        self.end_pattern = "{%endfor%}"

    def perform_parsing(self, context, template):
        tmp_struct = []
        parsed_template = template

        tmp_uuid = "".join(random.choice([str(digit for digit in range(10))]) for _ in range(10))

        sequence_started = False

        for word in template.split():
            stripped_word = word.strip()

            if stripped_word == self.begin_pattern:
                parsed_template = parsed_template.replace(word, tmp_uuid)

                sequence_started = True

            elif stripped_word == self.end_pattern:
                sequence_started = False

                parsed_template = parsed_template.replace(word, "")
                parsed_template = parsed_template.replace(tmp_uuid, " ".join(tmp_struct * 2))

                tmp_struct = []

            else:
                if sequence_started:
                    tmp_struct.append(word)

        return parsed_template
