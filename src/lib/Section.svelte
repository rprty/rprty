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

    {#if section.type === "img"}
        <div class="col">
            <img src={section.body.src} alt="" />
            <b>{section.body.caption}</b>
        </div>
    {/if}

    {#if section.type === "video"}
        <div class="col">
            <video src={section.body.src} controls>
                <track kind="captions" />
            </video>
            <b>{section.body.caption}</b>
        </div>
    {/if}
{/each}
