<script lang="ts" setup>
import { Input } from '@/components/ui/input'
import { Progress } from '@/components/ui/progress'
import { onMounted, ref } from 'vue'
import { Button } from '@/components/ui/button'
import { getServerStatus, uploadFile } from '@/lib/requests.ts'
import type { UploadResponse } from '@/lib/model.ts'
import { CardContent, CardTitle } from '@/components/ui/card'

const progress = ref(48)
const taskId = ref<string>(
  'TestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTest',
)
let uploadResponse: UploadResponse
const log = ref<string>('test')
onMounted(async () => {
  console.log(await getServerStatus())
})

const handleFile = async (event: Event) => {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  if (file) {
    uploadResponse = await uploadFile(file)
    console.log(uploadResponse)
    return uploadResponse
  } else {
    console.log('No file selected')
  }
}
</script>

<template>
  <article class="flex flex-col space-y-12">
    <Card
      class="font-orbitron border-2 border-zinc-600 rounded-lg p-6 backdrop-blur-sm select-none"
    >
      <CardHeader>
        <CardTitle class="text-xl">Get Task ID</CardTitle>
      </CardHeader>
      <CardContent class="my-4">
        <form class="space-y-4 flex flex-col">
          <label>
            <span class="font-orbitron">Upload file:</span>
            <Input
              class="border-2 border-zinc-600 rounded-lg h-10 w-full cursor-pointer"
              type="file"
              @change="handleFile"
            />
          </label>
          <label class="font-orbitron">
            Your Task ID:
            <div
              class="border-2 border-zinc-600 rounded-sm h-fit w-full flex items-center px-4 py-2 text-orange-500 select-text wrap-anywhere cursor-text"
            >
              {{ taskId }}
            </div>
          </label>
        </form>
      </CardContent>
    </Card>
    <Card
      class="font-orbitron border-2 border-zinc-600 rounded-lg p-6 backdrop-blur-sm select-none"
    >
      <CardHeader>
        <CardTitle class="text-xl">Figure Generate</CardTitle>
      </CardHeader>
      <CardContent class="my-4 space-y-4">
        <form class="space-y-4 flex flex-col">
          <label class="font-orbitron">
            Task ID Input:
            <div class="flex h-10 gap-x-4">
              <Input
                v-model="taskId"
                class="border-2 border-zinc-600 rounded-lg h-full w-3/4 mx-auto"
              />
              <Button
                class="font-orbitron rounded-lg border-2 h-full w-1/4 border-zinc-600 cursor-pointer text-orange-500 hover:text-orange-400"
                variant="outline"
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
    <Card
      class="font-orbitron border-2 border-zinc-600 rounded-lg p-6 backdrop-blur-sm select-none"
    >
      <CardHeader>
        <CardTitle class="text-xl">Log Output</CardTitle>
      </CardHeader>
      <CardContent class="my-4">
        <div
          class="border-2 border-zinc-600 rounded-sm h-fit w-full flex items-center px-4 py-2 select-text wrap-anywhere cursor-text"
        >
          {{ log }}
        </div>
      </CardContent>
    </Card>
  </article>
</template>

<style lang="scss" scoped></style>
