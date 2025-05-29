<script setup lang="ts">
const props = defineProps<{ width: number; height: number }>()
</script>

<template>
  <svg
    :width="props.width"
    :height="props.height"
    viewBox="0 0 37 37"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      d="M18.5 24.6667L17.7929 25.3739L18.5 26.081L19.2071 25.3739L18.5 24.6667ZM19.5 6.16675C19.5 5.61446 19.0523 5.16675 18.5 5.16675C17.9477 5.16675 17.5 5.61446 17.5 6.16675L19.5 6.16675ZM9.25 15.4167L8.54289 16.1239L17.7929 25.3739L18.5 24.6667L19.2071 23.9596L9.95711 14.7096L9.25 15.4167ZM18.5 24.6667L19.2071 25.3739L28.4571 16.1239L27.75 15.4167L27.0429 14.7096L17.7929 23.9596L18.5 24.6667ZM18.5 24.6667L19.5 24.6667L19.5 6.16675L18.5 6.16675L17.5 6.16675L17.5 24.6667L18.5 24.6667Z"
      fill="#52525B"
    />
    <path d="M7.7085 32.375L29.2918 32.375" stroke="#52525B" stroke-width="2" />
  </svg>
</template>

<style scoped></style>
