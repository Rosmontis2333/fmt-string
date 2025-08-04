<script lang="ts" setup>
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { Progress } from '@/components/ui/progress'

const taskId = defineModel<string>('taskId', { required: true })
const progress = defineModel<number>('progress', { required: true })

const emit = defineEmits<{
  handleUploadTaskId: [taskId: string]
}>()
</script>

<template>
  <Card
    class="font-orbitron border-2 border-zinc-600 bg-transparent rounded-lg p-6 backdrop-blur-sm select-none"
  >
    <CardHeader>
      <CardTitle class="text-xl">Figure Generate</CardTitle>
    </CardHeader>
    <CardContent class="space-y-4">
      <form class="space-y-4 flex flex-col">
        <label class="font-orbitron">
          Task ID Input:
          <div class="flex h-10 gap-x-4">
            <Input
              v-model="taskId"
              class="border-2 border-zinc-600 rounded-lg h-full w-3/4 mx-auto"
            />
            <Button
              type="button"
              class="font-orbitron rounded-lg border-2 h-full w-1/4 border-zinc-600 cursor-pointer text-orange-500 hover:text-orange-400"
              variant="outline"
              @click="emit('handleUploadTaskId', taskId)"
            >
              Start
            </Button>
          </div>
        </label>
      </form>
      <div class="flex w-full items-center space-x-2">
        <p class="text-orange-500 text-xl select-none">{{ progress + '%' }}</p>
        <Progress v-model="progress" class="h-3" />
      </div>
      <img class="rounded-sm border-2 border-zinc-600" src="/src/assets/Figure_1.png" />
    </CardContent>
  </Card>
</template>
