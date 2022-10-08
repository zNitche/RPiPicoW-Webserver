from pws.core.parsers.parser_base import ParserBase


class ContextVarsParser(ParserBase):
    def __init__(self):
        super().__init__()

        self.begin_pattern = "{{"
        self.end_pattern = "}}"

    def get_pattern(self, word):
        pattern_word = self.begin_pattern + word + self.end_pattern

        return pattern_word

    def get_parsed_context(self, context):
        parsed_context = {}

        for context_key in context:
            parsed_context[self.begin_pattern + context_key + self.end_pattern] = context[context_key]

        return parsed_context

    def perform_parsing(self, context, template):
        parsed_context = self.get_parsed_context(context)
        parsed_template = template[:]

        for context_key in parsed_context:
            parsed_template = parsed_template.replace(context_key, str(parsed_context[context_key]))

        return parsed_template
