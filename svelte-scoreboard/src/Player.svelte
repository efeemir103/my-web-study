<script>
    // Use Event Dispatcher to send an event to main process.
    import { createEventDispatcher } from 'svelte';

    // Create a event dispatcher.
    const dispatch = createEventDispatcher();
    
    // Load props passed in.
    export let name;
    export let points;
    // Show point changing buttons.
	let showControls = false;

    // Handle on:click events.
	const addPoint = () => points++;
	const removePoint = () => points--;
    const toggleControls = () => showControls = !showControls;
    const onDelete = () => dispatch("removeplayer", name);
</script>

<style>
	h1 {
		color: #204f6e;
	}

	h3 {
		margin-bottom: 10px;
	}
</style>

<!-- Player Card -->
<div class="card">
    <h1>
        {name}
        <button class="btn btn-sm" on:click={toggleControls}>
            <!-- Switch in between "-" and "+" -->
            {#if showControls}-{:else}+{/if}
        </button>
        <button class="btn btn-danger" on:click={onDelete}>x</button>
    </h1>
    <h3>Points: {points}</h3>
    <!-- Control section -->
    {#if showControls}
    <button class="btn" on:click={addPoint}>+1</button>
    <button class="btn btn-dark" on:click={removePoint}>-1</button>
    <input type="number" bind:value={points} />
    {/if}
</div>