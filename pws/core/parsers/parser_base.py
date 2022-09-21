class ParserBase:
    def __init__(self):
        self.begin_pattern = None
        self.end_pattern = None

    def check_pattern(self, context_item):
        return False

    def perform_parsing(self, context, template):
        pass
