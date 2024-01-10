<script lang="ts">
  import { onMount } from "svelte";
  import { type Content } from "./content";
  import Section from "./lib/Section.svelte";

  let content: Content[] = [];

  onMount(async () => {
    content = await (await fetch("report.json")).json();
  });
</script>

<main>
  <Section {content} />
</main>

<style>
</style>
