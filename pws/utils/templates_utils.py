from pws.config import ServerConfig


def load_template_from_file(template_path, template_root_path=ServerConfig.TEMPLATES_ROOT_PATH):
    path = f"{template_root_path}/{template_path}"

    with open(path, "r") as file:
        template = file.read()

    return template
