import json
import os

from pydantic import BaseModel


class h1(BaseModel):
    type: str = "h1"
    body: str


class p(BaseModel):
    type: str = "p"
    body: str


class grid(BaseModel):
    type: str = "grid"
    body: list["Section"]


Section = h1 | p | grid


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
        h1(body="Hello, World!"),
        p(body="This is a paragraph"),
        grid(body=[
            h1(body="Hello, World!"),
            p(body="This is a paragraph"),
            grid(body=[
                h1(body="Hello, World!"),
                p(body="This is a paragraph"),
            ]),
            grid(body=[
                h1(body="Hello, World!"),
                p(body="This is a paragraph"),
            ]),
        ]),
    ])

    report.write("public/report.json")
