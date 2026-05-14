<script lang="ts">
  export let tree;

  function renderNode(node, depth = 0) {
    return {
      tag: node.tag,
      attrs: node.attrs,
      depth,
      children: node.children ? node.children.map(child => renderNode(child, depth + 1)) : [],
    };
  }

  $: renderedTree = tree ? renderNode(tree) : null;
</script>

{#if renderedTree}
  <div class="tree">
    {#each [renderedTree] as [node]}
      <Node {node} />
    {/each}
  </div>
{/if}

<style>
  .tree {
    font-family: monospace;
    white-space: pre;
  }
  .node {
    margin-left: 20px;
    padding: 5px;
    border-left: 1px solid #ccc;
  }
  .tag {
    font-weight: bold;
    color: #007BFF;
  }
  .attrs {
    color: #666;
    font-size: 0.9em;
  }
</style>