class ParserBase:
    def __init__(self):
        self.begin_pattern = None
        self.end_pattern = None

    def get_pattern(self, word):
        return word

    def perform_parsing(self, context, template):
        pass
