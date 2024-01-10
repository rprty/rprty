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

interface video {
    type: "video";
    body: { src: string };
}

export type Content = h1 | chart | grid | video | p;
