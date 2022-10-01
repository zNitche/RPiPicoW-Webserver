class EndpointBase:
    def __init__(self):
        self.methods = []
        self.template = ""
        self.address = ""

    def get_context(self):
        return {}
