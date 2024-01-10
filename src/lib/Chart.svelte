<script lang="ts">
    import { onMount } from "svelte";
    import { Chart, type ChartConfiguration } from "chart.js";

    export let content: ChartConfiguration = {
        type: "bar",
        data: {
            datasets: [],
        },
    };

    onMount(async () => {
        const ctx = document.getElementById("chart") as HTMLCanvasElement;
        new Chart(ctx, content);
    });
</script>

<div>
    <canvas id="chart"></canvas>
</div>
