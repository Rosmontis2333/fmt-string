<script lang="ts" setup>
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Input } from '@/components/ui/input'

const props = defineProps<{
  taskId: string
}>()

const emit = defineEmits<{
  handleFile: [event: Event]
}>()
</script>

<template>
  <Card
    class="font-orbitron border-2 border-zinc-600 rounded-lg p-6 bg-transparent backdrop-blur-sm select-none"
  >
    <CardHeader>
      <CardTitle class="text-xl">Get Task ID</CardTitle>
    </CardHeader>
    <CardContent>
      <form class="space-y-4 flex flex-col">
        <label>
          <span class="font-orbitron">Upload file:</span>
          <Input
            class="border-2 border-zinc-600 rounded-lg h-10 w-full cursor-pointer"
            type="file"
            @change="emit('handleFile', $event)"
          />
        </label>
        <label class="font-orbitron">
          Your Task ID:
          <div
            class="border-2 border-zinc-600 rounded-sm h-fit w-full flex items-center px-4 py-2 text-orange-500 select-text wrap-anywhere cursor-text"
          >
            {{ props.taskId }}
          </div>
        </label>
      </form>
    </CardContent>
  </Card>
</template>
