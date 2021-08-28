# Rumble-AI, the open source virtual assistant

Tired of those... `unnamed?` virtual assistants that tracks every word, move, action and thought?

Be welcome to the big, and NOT only one but not as other ones open source virtual assistant **RUMBLE!**

## Skills

One of the most important parts of this `artifical consciousness` it's the is the ability to perform actions, similar 
to those that a human consciousness might perform.

It's more than obviously that this is a very basic design compare to a human consciousness,
but the motivation behind this it's to create an `Artificial Intelligence` that could be improved by anyone, 
thanks to the open source world.

## The way on how the Rumble's code has been design

The factory desing pattern it's the **keystone** behind the desing.

    Why? Rumble it's designed to achieve to main goals, when talking about his source code:

    - 1: Source code has to be easy to mantain, once his base logic it's written
    - 2: Rumble skills need an easy and an scalable way to grow, in quality, actions and, of course, 
         in number of skills.

## How factory pattern helps on this purpose?

Because it's really easy to develop "client code", where the internal details 
of the implementation are hidden.

And by client code, here we are refering two things:

    - The internal skills, those who has been written directly on the source code, but through the `Skills Factory`.
    - The external skills, or **plugins**, who can be written as an external libraries for anyone.

The **factory** it's the primary responsable of instanciate the objects that will performs the actions of the skills

It's implemented as a way of handle the management of the Rumble's skills, the `plugin` system 
where anyone can implement it's own skills, or download them from internet.

The tradeoff: Now we had a more verbose way code on the factory side, but, it's just one site. And written once. 
Now, that it's already implemented, we can really grow up the number of Rumble's skills.


## How to contribute to improve Rumble's skills?

In this early stages, and due to the **plugins** system it's not implemented yet, anyone can write new **internal skills**.

**How?**

- Create a fork of this project

- Go to the `..src.skills` folder, and create a new one, with the name of your skill. PEP8 Python's style guidelines
  should be always followed for the naming convertions. 

  - Create a new Python class with the name of your skill. This one should inherit the abstract class `skill`.
  - You should create a constructor **always** like this one. 
  - If you need to pass more data via args, create as much as you need to fit your needs, or use the Python's
    shorthand for this, with `**kwargs`.
  - A concrete example, could be something like:
  ```
  from ...core.skill import Skill  # Don't forget about this one
  
  
  class Example(Skill):
    """
        Performs a designed action
    """

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
      - The name parameter must contains a name in English at index 0, and an spanish name at index 1.
      - The tags are the identifier for your skill when you are talking with `Rumble`
    
    ```
    Example: {
        'name': ['example', 'ejemplo'], 
        'description': 'A description about the skill that you are coding',
        'tags': {
            'english': ['example', 'sample', 'more_tags', 'activate skill if this word matches the detection one'],
            'spanish': ['ejemplo', 'palabra_identificativa', 'palabras_que_al_oir_Rumble_activan_la_skill'],
        },
    },
    ```
  
- Finally, make a pull request proposing your new skill. When the skill will be reviewed will be
    a candidate to become a new Rumble skill.

### Congrats!

If everything goes well, you will have contributed to the Rumble's source code with a new skill.
**Thank you!**