import json
import os
from typing import Any

from pydantic import BaseModel


class Section(BaseModel):
    content: Any


class h1(Section):
    type: str = "h1"
    content: str


class Report:
    def __init__(self, sections: list[Section]):
        self.sections = sections

    def write(self, file: str):
        os.makedirs(os.path.dirname(file), exist_ok=True)
        with open(file, "w") as f:
            report = [
                section.model_dump()
                for section in self.sections]

            json.dump(report, f)


if __name__ == "__main__":
    report = Report([
        h1(content="Hello, World!")
    ])

    report.write("public/report.json")
