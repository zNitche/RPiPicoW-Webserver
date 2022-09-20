from pws.config import ServerConfig


def load_template_from_file(template_path, template_root_path=ServerConfig.TEMPLATES_ROOT_PATH):
    path = f"{template_root_path}/{template_path}"

    with open(path, "r") as file:
        template = file.read()

    return template


def parse_context(context):
    parsed_context = {}

    for context_key in context:
        parsed_context["{{" + context_key + "}}"] = context[context_key]

    return parsed_context


def parse_template_with_context(template, context):
    parsed_template = template
    parsed_context = parse_context(context)

    for context_key in parsed_context:
        parsed_template = parsed_template.replace(context_key, parsed_context[context_key])

    return parsed_template
