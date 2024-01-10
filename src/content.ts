import type { ChartConfiguration } from "chart.js/auto"

interface h1 {
    type: "h1";
    body: string;
}

interface p {
    type: "p";
    body: string;
}

interface chart {
    type: "chart";
    body: ChartConfiguration;
}

interface grid {
    type: "grid";
    body: Content[];
}

interface img {
    type: "img";
    body: { src: string, caption: string };
}

interface video {
    type: "video";
    body: { src: string, caption: string };
}

export type Content = h1 | p | chart | grid | img | video ;
