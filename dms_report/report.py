import json
import os
from typing import Literal

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


class media(BaseModel):
    src: str
    caption: str = ''


class img(BaseModel):
    type: str = "img"
    body: media


class video(BaseModel):
    type: str = "video"
    body: media


class dataset(BaseModel):
    label: str
    data: list[int]


class chart_data(BaseModel):
    labels: list[str]
    datasets: list[dataset]


class chart_body(BaseModel):
    type: Literal["line", "bar"]
    data: chart_data


class chart(BaseModel):
    type: str = "chart"
    body: chart_body


Section = h1 | p | grid | img | video | chart


class Report:
    def __init__(self, sections: list[Section]):
        self.sections = sections

    def write(self, file="public/report.json"):
        os.makedirs(os.path.dirname(file), exist_ok=True)
        with open(file, "w") as f:
            report = [
                section.model_dump()
                for section in self.sections]

            json.dump(report, f)


