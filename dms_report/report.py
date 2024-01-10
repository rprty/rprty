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


class video_body(BaseModel):
    src: str
    caption: str = ''


class video(BaseModel):
    type: str = "video"
    body: video_body


Section = h1 | p | grid | video


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
            video(body=video_body(
                src="https://storage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")),
            video(body=video_body(
                src="https://storage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")),
            video(body=video_body(
                src="https://storage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")),
            video(body=video_body(
                src="https://storage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")),
        ]),
    ])

    report.write("public/report.json")
    report.write("public/report.json")
    report.write("public/report.json")
