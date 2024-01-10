<script lang="ts">
    import Chart from "./Chart.svelte";
    import { type Content } from "../content";
    export let content: Content[] = [];
</script>

{#each content as section}
    {#if section.type === "h1"}
        <h1>{section.body}</h1>
    {/if}

    {#if section.type === "p"}
        <p>{section.body}</p>
    {/if}

    {#if section.type === "chart"}
        <Chart content={section.body} />
    {/if}

    {#if section.type === "grid"}
        <div class="grid">
            <svelte:self content={section.body} />
        </div>
    {/if}

    {#if section.type === "video"}
        <video src={section.body.src} controls>
            <track kind="captions" />
        </video>
    {/if}
{/each}
