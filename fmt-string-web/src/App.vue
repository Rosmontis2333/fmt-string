<script setup lang="ts">
import Header from '@/components/PageHeader.vue'
</script>

<template>
  <main class="m-auto w-full min-h-full h-fit absolute text-zinc-600">
    <div class="w-3xl m-auto bg-zinc-50/60 px-12 py-4 backdrop-blur-sm">
      <Header />
      <hr class="border-zinc-600 mt-4 mb-8 border" />
      <RouterView />
    </div>
  </main>
</template>

<style scoped lang="scss"></style>
