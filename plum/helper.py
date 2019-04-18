# pylint: disable=missing-docstring
from sys import argv
FILE = argv.pop(0)
CLI_ARGS = argv
USAGE = "usage: {} [commands] project-name".format(FILE)

HELP = {
    "init": {
        "help": "initializes the project",
        "example": ["plum init <project-name>"],
        "subcommand": {
            "project-name": {
                "required": False,
                "help": "the project name to select",
                "default": "current directory name"
            },
            "executable": {
                "required": False,
                "help": "pass this if you want to create '__main__.py' file"
            }
        }
    },
    "pack": {
        "help": "builds the project for distribution",
        "example": ["plum pack"],
        "subcommand": {}
    },
    "publish": {
        "help": "publish the project on git hub/lab / bitbucket / pypi"
    }
}


COMMANDS = HELP.keys()


def show_all_help():
    """
    Function to show all the commands help
    """
    print("- Command -")
    for key, item in HELP.items():
        print("\t{}\t{}\n".format(key, item["help"]))
