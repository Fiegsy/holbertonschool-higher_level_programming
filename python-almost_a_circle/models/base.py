#!/usr/bin/python3
"""This module defines a Base class and some related functionalities."""
import json
import os


class Base:
    """Base class for other classes"""

    _num_instances = 0

    def __init__(self, identifier=None):
        """Initialize a Base instance."""
        if identifier is not None:
            self.identifier = identifier
        else:
            Base._num_instances += 1
            self.identifier = Base._num_instances

    @staticmethod
    def to_json(data):
        """Convert data to JSON."""
        return json.dumps(data) if data else "[]"

    @classmethod
    def save_to_file(cls, instances):
        """Save instances to a JSON file."""
        instances = instances or []
        filename = f"{cls.__name__}_instances.json"
        with open(filename, "w") as file:
            data = [instance.serialize() for instance in instances]
            file.write(cls.to_json(data))

    @staticmethod
    def from_json(json_string):
        """Load data from JSON string."""
        return json.loads(json_string) if json_string else []

    @classmethod
    def create_instance(cls, **kwargs):
        """Create an instance from dictionary."""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        else:
            instance = cls(1)
        instance.update(**kwargs)
        return instance

    @classmethod
    def load_from_file(cls):
        """Load instances from JSON file."""
        filename = f"{cls.__name__}_instances.json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r', encoding="utf-8") as file:
            json_data = file.read()
            data = cls.from_json(json_data)
            instances = [cls.create_instance(**item) for item in data]
        return instances

    def serialize(self):
        """Serialize instance to dictionary."""
        return self.__dict__

    def update(self, **kwargs):
        """Update instance attributes."""
        for key, value in kwargs.items():
            setattr(self, key, value)