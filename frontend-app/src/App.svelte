<script lang="ts">
  let html = '';
  let tree = null;
  let error = '';

  async function parse() {
    error = '';
    try {
      const response = await fetch('http://127.0.0.1:8000/api/parse/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ html }),
      });
      const data = await response.json();
      if (response.ok) {
        tree = data.tree;
      } else {
        error = data.error || 'Failed to parse HTML';
      }
    } catch (e) {
      error = 'Failed to connect to the backend';
    }
  }
</script>

<div class="container">
  <h1>HTML Tree Visualizer</h1>
  <textarea bind:value={html} placeholder="Paste your HTML here..." rows="10" cols="80"></textarea>
  <button on:click={parse}>Parse HTML</button>
  {#if error}
    <p class="error">{error}</p>
  {/if}
  {#if tree}
    <div class="tree-container">
      <TreeVisualization {tree} />
    </div>
  {/if}
</div>

<style>
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
  }
  textarea {
    width: 100%;
    margin-bottom: 10px;
  }
  button {
    padding: 10px 15px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  .error {
    color: red;
  }
  .tree-container {
    margin-top: 20px;
    border: 1px solid #ccc;
    padding: 10px;
    border-radius: 4px;
  }
</style>