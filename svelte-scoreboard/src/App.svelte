<script>
	// Import custom Svelte components.
	import Navbar from './Navbar.svelte';
	import Player from './Player.svelte';
	import AddPlayer from './AddPlayer.svelte';

	// An object array containing users.
	let players = [];

	// Use fetch api to get 10 random users.
	fetch('https://randomuser.me/api/?results=10')
		.then(response => {
			if(response.status === 200){
				response.json().then(data => {
					// Manipulate each object in returned data so there is only name and points fields.
					players = data["results"].map(o => {
						let newObj = {
							name: o["name"]["first"] + " " + o["name"]["last"],
							points: o["location"]["street"]["number"]
						};
						return newObj;
					});
				});
			}
    	})
    	.catch(err => {
			console.log('Fetch Error: ', err);
			// If couldn't fetch data initiate players with default data.
			players = [
				{
					name: "John Doe",
					points: 53
				},
				{
					name: "Sam Smith",
					points: 45
				},
				{
					name: "Sara Wilson",
					points: 34
				}
			];
		  });
	
	// Handle addplayer event.
	const addPlayer = (e) => {
		const newPlayer = e.detail;
		console.log(newPlayer);
		players = [...players, newPlayer];
	};

	// Handle removeplayer event.
	const removePlayer = (e) => {
		players = players.filter(player => player.name !== e.detail);
	}
</script>

<!-- Custom component "Navbar.svelte" -->
<Navbar />
<div class="container">
	<!-- Custom component "AddPlayer.svelte" -->
	<AddPlayer on:addplayer={addPlayer} />
	<!-- Conditional html elements -->
	{#if players.length === 0}
		<p>No Players</p>
	{:else}
		<!-- Loopthrough each player -->
		{#each players as player}
			<!-- Custom component "Player.svelte" -->
			<Player name={player.name} points={player.points} on:removeplayer={removePlayer}/>
		{/each}
	{/if}
</div>