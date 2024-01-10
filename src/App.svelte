<script lang="ts">
  import type { ChartConfiguration } from "chart.js";
  import { onMount } from "svelte";
  import Chart from "./lib/Chart.svelte";

  interface h1 {
    type: "h1";
    content: string;
  }

  interface chart {
    type: "chart";
    content: ChartConfiguration;
  }

  interface grid {
    type: "grid";
    content: Section[];
  }

  interface video {
    type: "video";
    content: { src: string };
  }

  type Section = h1 | chart | grid | video;

  let report: Section[] = [];

  onMount(async () => {
    report = await (await fetch("report.json")).json();
  });
</script>

<main>
  {#each report as section}
    {#if section.type === "h1"}
      <h1>{section.content}</h1>
    {/if}

    {#if section.type === "chart"}
      <Chart content={section.content} />
    {/if}

    {#if section.type === "video"}
      <video src={section.content.src}>
        <track kind="captions" />
      </video>
    {/if}
  {/each}
</main>

<style>
</style>
