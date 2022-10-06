from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    email: str = None
    location: str = None
    company: str = None
    massage: str = None