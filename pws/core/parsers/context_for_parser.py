from pws.core.parsers.parser_base import ParserBase
import random


class ContextForParser(ParserBase):
    def __init__(self):
        super().__init__()

        self.begin_pattern = "{%for%}"
        self.end_pattern = "{%endfor%}"

    def get_sequence_uuid(self):
        sequence_uuid = "".join([random.choice([str(digit) for digit in range(10)]) for _ in range(10)])

        return sequence_uuid

    def parse_uuids(self, parse_struct, splitted_template):
        parsed_template = " ".join(splitted_template)

        for uuid, value in parse_struct.items():
            parsed_template = parsed_template.replace(uuid, " ".join(value * 2))

        return parsed_template

    def perform_parsing(self, context, template):
        sequence_started = False
        parsed_template = template[:]

        splitted_template = parsed_template.split()
        splitted_template_cp = splitted_template.copy()

        parse_struct = {}

        for word_id, word in enumerate(splitted_template):
            if word == self.begin_pattern:
                sequence_started = True

                uuid = self.get_sequence_uuid()

                if uuid not in parse_struct.keys():
                    parse_struct[uuid] = []

                splitted_template_cp[word_id] = uuid

            elif word == self.end_pattern:
                sequence_started = False
                splitted_template_cp[word_id] = ""

            else:
                if sequence_started:
                    splitted_template_cp[word_id] = ""

                    parse_struct[uuid].append(word)

        parsed_template = self.parse_uuids(parse_struct, splitted_template_cp)

        return parsed_template
