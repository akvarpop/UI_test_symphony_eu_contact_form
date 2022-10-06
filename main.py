from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    email: str = None
    location: str = None
    company: str = None
    describe_your_project: str = None