<script lang="ts">
  export let node;
</script>

<div class="node" style="margin-left: {node.depth * 20}px">
  <span class="tag">&lt;{node.tag}&gt;</span>
  {#if Object.keys(node.attrs).length > 0}
    <span class="attrs">
      {#each Object.entries(node.attrs) as [key, value]}
        {key}="{value}"
      {/each}
    </span>
  {/if}
  {#if node.children.length > 0}
    <div class="children">
      {#each node.children as child}
        <Node {child} />
      {/each}
    </div>
  {/if}
  <span class="tag">&lt;/{node.tag}&gt;</span>
</div>