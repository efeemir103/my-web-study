<script>
	import Navbar from './Navbar.svelte';
	import Player from './Player.svelte';
	import AddPlayer from './AddPlayer.svelte';
	let players = [];
	fetch('https://randomuser.me/api/?results=10')
		.then(response => {
			if(response.status === 200){
				response.json().then(data => {
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
	
	const addPlayer = (e) => {
		const newPlayer = e.detail;
		console.log(newPlayer);
		players = [...players, newPlayer];
	};
	const removePlayer = (e) => {
		players = players.filter(player => player.name !== e.detail);
	}
</script>

<Navbar />
<div class="container">
	<AddPlayer on:addplayer={addPlayer} />
	{#if players.length === 0}
		<p>No Players</p>
	{:else}
		{#each players as player}
			<Player name={player.name} points={player.points} on:removeplayer={removePlayer}/>
		{/each}
	{/if}
</div>