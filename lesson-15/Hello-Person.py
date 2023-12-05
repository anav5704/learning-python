def Hello(name, lang):
    greetings = {
        "English": "Hello",
        "Hindi": "Namaste"
    }

    msg = f"{greetings[lang]} {name}"

    print(msg)

import argparse

parser = argparse.ArgumentParser(
    description="Provides a personal greeting"
)

parser.add_argument(
    "-n", "--name", metavar="name",
    required=True, help="The name of the person to greet"
)

parser.add_argument(
    "-l", "--language", metavar="language",
    required=True, help="The mother tongue of the person to greet"
)

args = parser.parse_args()

Hello(args.name, args.language)