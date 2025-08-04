<script lang="ts" setup>
import { Card, CardHeader, CardTitle } from '@/components/ui/card'

const props = defineProps<{
  log: string
}>()
</script>

<template>
  <Card
    class="font-orbitron border-2 border-zinc-600 bg-transparent rounded-lg p-6 backdrop-blur-sm select-none"
  >
    <CardHeader>
      <CardTitle class="text-xl">Log</CardTitle>
    </CardHeader>
    <CardContent>
      <p class="text-sm text-zinc-500 border-2 border-zinc-600 rounded-sm p-2 select-text">
        {{ props.log }}
      </p>
    </CardContent>
  </Card>
</template>
