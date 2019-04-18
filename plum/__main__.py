# pylint: disable=import-error, missing-docstring
from helper import CLI_ARGS, show_all_help

if not CLI_ARGS:
    print("Plum is a python project scaffolder. Its the first ever tool",
          "for the python developer to create and manage python workflow")
    show_all_help()
    print("Note: To know more about command, add 'help' followed by command")
    print("      For example, 'plum help init'")
