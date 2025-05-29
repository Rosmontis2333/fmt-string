<script setup lang="ts">
import Header from '@/components/Header.vue'
</script>

<template>
  <main class="m-auto w-full min-h-full h-fit absolute text-zinc-600">
    <div class="w-2xl m-auto">
      <Header/>
      <RouterView />
    </div>
  </main>
</template>

<style scoped lang="scss">
main {
  background-image: url('/src/assets/hexagon.svg');
  background-size: contain;
  background-attachment: fixed;
  background-repeat: no-repeat;
  background-position-x: center;
}
</style>
