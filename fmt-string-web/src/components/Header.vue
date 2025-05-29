<script lang="ts" setup>
import IconBezene from '@/components/icons/IconBezene.vue'
import { useRoute } from 'vue-router'

const route = useRoute()
</script>

<template>
  <nav class="flex items-center py-2 mb-4 font-orbitron text-xl justify-between">
    <div class="flex items-center space-x-2 select-none">
      <IconBezene :height="48" :width="48" />
      <p class="font-medium">
        <span class="text-orange-500">FMT </span>
        <span>STRING</span>
      </p>
    </div>
    <RouterLink
      :class="route.name === 'main' ? 'text-orange-500 underline' : 'text-zinc-600'"
      to="/"
    >
      Main
    </RouterLink>
    <RouterLink
      :class="route.name === 'tutorial' ? 'text-orange-500 underline' : 'text-zinc-600'"
      to="/tutorial"
      >Tutorial
    </RouterLink>
    <RouterLink
      :class="route.name === 'about' ? 'text-orange-500 underline' : 'text-zinc-600'"
      to="/about"
      >About
    </RouterLink>
  </nav>
</template>

<style scoped></style>
