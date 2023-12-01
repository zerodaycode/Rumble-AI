# Rumble-AI, the open source virtual assistant

Tired of those... `unnamed?` virtual assistants that tracks every word, move, action and thought?

Be welcome to the big, and NOT only one but not as other ones open source virtual assistant **RUMBLE-AI**

[![GitHub Issues](https://img.shields.io/github/issues/zerodaycode/Zork.svg)](https://github.com/zerodaycode/Rumble-AI/issues)</br>
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/zerodaycode/Zork.svg)](https://github.com/zerodaycode/Rumble-AI/pulls)</br>
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

## Skills

One of the most important parts of this `artifical consciousness` it's the ability to perform actions, similar to those that a human consciousness might perform.

It's more than obviously that this is a very basic design compare to a human consciousness, but the motivation behind this it's to create a `Artificial Intelligence` that could be improved by anyone, thanks to the open source world.

There's actually two kinds of skills

- **`internals`**: The ones that are directly implemented in the codebase

- **`plugins`** : The ones that are provided by external users (or literally, anyone), that design its own functionality and want to run it inside **Rumble**. More about plugins later

// To-do List the internals

## Developers zone

This is the place where the contributors of the project can gather
the most important information in order to be able to run locally
the project, contribute to the codebase and deploy their changes!

### Quick notes

> The **Zero Day Code** development team, mostly use Unix-like terminal emulators, even if we are working on Linux. That just standardize our workflow across the different projects of the organization and across the multiple OS that we are typically using, so you'll find a **`alias.sh`** script to automate part of our job.
Obviously, you're free to decide if you want to adhere to this, but some parts of the documentation directly assumes it's usage.

### Installation guide

First, make a fork of this repository, and clone the fork into your machine.

Well, you're now in possession of a copy of our source code. Common sense applies here. Before all, make sure that you read our [Contributing Guidelines](/Rumble-AI/CONTRIBUTING.md), then, proceed to implement your desired changes in your local fork.
When you're satisfied with the results, just open us a PR, and the development team will be glad to review.

Please, make sure that your changes adheres correctly to the technical specifications of the project, which you'll find mostly along this document.

Run then (if you will) from the root of the project the command:

```bash
. ./alias.sh
```

Now, we strongly recommend you to create a **Python virtual environment**, that will maintain isolated the dependencies required for run this project for the global Python installation in your machine. For that, you can refer directly to [Creation of virtual environments](https://docs.python.org/3.11/library/venv.html#venv-def).

And with your already created virtual environment:

```bash
venv_up
```

For installing the required dependencies given the actual state of the project, just run:

```bash
pip install .
```

When **pip** finish its job, you'll be good to go, and start your coding journey.

### Running **Rumble-AI** locally

Finally:

```bash
python main.py
```

And you'll start to see **Rumble** in action!

### The way on how the Rumble's code has been design

The factory design pattern it's the **keystone** behind the design.

Why? Rumble it's designed to achieve two main goals, when talking about his source code:

- 1: Source code has to be easy to maintain, once his base logic it's written
- 2: Rumble skills need an easy and a scalable way to grow, in their quality and actions

### How factory pattern helps on this purpose?

Because it's really easy to develop "client code", where the internal details of the implementation are hidden.

And by client code, here we are referring two things:

- The internal skills, those who has been written directly on the source code, but through the `Skills Factory`.
- The external skills, or **plugins**, who can be written as an external python modules or python modules bind with other libraries for anyone.

The **factory** it's the primary responsible for instantiate the objects that will perform the actions of the skills

It's implemented as a way of handle the management of the Rumble's skills, the `plugin` system where anyone can implement its own skills, or download them from internet.

The trade-off: Now we had a more verbose way code on the factory side, but, it's just one site. And written once.
Now, that it's already implemented, we can really grow up the number of Rumble's skills.

## How to contribute to improve Rumble's skills?

This part of the project it's still at early stages, and the **plugins'** system it's far from complete yet, but however, anyone can write new **internal skills**, directly in the source code.

**How?**

- Create a fork of this project

- Go to the `..src.skills` folder, and create a new one, with the name of your skill.

> Note: PEP8 Python's style guidelines should be always respected.

- Create a new Python class with the name of your skill. This one should inherit the abstract class `skill`.
- You should create a constructor **always** like this one.
- If you need to pass more data via args, create as much as you need to fit your needs, or use the Python's
shorthand for this, with `**kwargs`.
- A concrete example, could be something like:

```python
from ...core.skill import Skill  # Don't forget about this one


class Example(Skill):
"""Performs some action"""

    def __init__(self, name, description, tags, id_language, optional1, **kwargs):
        # Mandatory attributes
        self.name: list[str] = name
        self.description: str = description
        self.tags: list[str] = tags
        self.id_language: int = id_language

        # Optional one (use as much as you need)
        self.optional1 = optional1

        # **kwargs variant:
        self.optional1 = kwargs['skills_dict_key'].get('value', 'default')

    def __str__(self):
        return self.name[self.id_language]

    # The skill action should always be written inside this 'play' method.
    def play(self) -> str:
        return f'{self.my_method()}, {self.my_another_method}!'

    # User defined method
    def my_method(self):
        return 'Hello'

    def my_another_method(self):
        return 'world'
```

- Under the `..src.core` folder, you will find the `skills_registry.py` file.
- Now, on the `rumble_skills_registry` dict, register a skill with the next format:
  - The dict's `key` **must** be the class name
  - The values must map the class attributes
    - The name parameter must contain a name in English at index 0, and a Spanish name at index 1.
    > Note: This is under evaluation, looking for a more robust implementation
    - The tags are the identifier for your skill when you are talking with `Rumble`

    ```python
    Example: {
        'name': ['example', 'ejemplo'], 
        'description': 'A description about the skill that you are coding',
        'tags': {
            'english': ['example', 'sample', 'more_tags', 'activate skill if this word matches the detection one'],
            'spanish': ['ejemplo', 'palabra_identificativa', 'palabras_que_al_oir_Rumble_activan_la_skill'],
        },
    },
    ```
  
- Finally, make a pull request proposing your new skill. When the skill will be reviewed will be a candidate to become a new Rumble skill.

### Congrats

If everything goes well, you will have contributed to the Rumble's source code with a new skill.
**Thank you!**
