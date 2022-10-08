from pws.config import ServerConfig

from pws.core.parsers.context_vars_parser import ContextVarsParser
from pws.core.parsers.context_for_parser import ContextForParser


class TemplateParser:
    def __init__(self):
        self.parsers = [
            ContextVarsParser(),
            ContextForParser()
        ]

    def load_template_from_file(self, template_path, template_root_path=ServerConfig.TEMPLATES_ROOT_PATH):
        path = f"{template_root_path}/{template_path}"

        with open(path, "r") as file:
            template = file.read()

        return template

    def perform_parsing(self, template, context):
        if template:
            template = self.load_template_from_file(template)

            for parser in self.parsers:
                template = parser.perform_parsing(context, template)

            return template

        else:
            return ""
