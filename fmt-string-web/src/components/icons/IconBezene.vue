<script setup lang="ts">
const props = defineProps<{ width: number; height: number }>()
</script>

<template>
  <svg
    :width="props.width"
    :height="props.height"
    viewBox="0 0 64 64"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      d="M58.7129 16.5771V47.4219L32 62.8447L5.28711 47.4219V16.5771L32 1.1543L58.7129 16.5771Z"
      stroke="#52525B"
      stroke-width="2"
    />
    <path d="M11 21L32 9" stroke="#52525B" stroke-width="2" stroke-linecap="round" />
    <path d="M11 44L32 56" stroke="#52525B" stroke-width="2" stroke-linecap="round" />
    <path d="M51.5 20V46" stroke="#52525B" stroke-width="2" stroke-linecap="round" />
  </svg>
</template>

<style scoped></style>
