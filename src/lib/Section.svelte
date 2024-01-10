<script lang="ts">
    import Chart from "./Chart.svelte";
    import { type Content } from "../content";
    export let content: Content[] = [];
</script>

<div class="section">
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
                {#each section.body as content}
                    <svelte:self {content} />
                {/each}
            </div>
        {/if}

        {#if section.type === "video"}
            <video src={section.body.src}>
                <track kind="captions" />
            </video>
        {/if}
    {/each}
</div>
