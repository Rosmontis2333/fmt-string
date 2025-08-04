<script lang="ts" setup>
import { onMounted, ref } from 'vue'
import { getServerStatus, uploadFile, uploadTaskId } from '@/lib/requests.ts'
import type { FileUploadResponse } from '@/lib/model.ts'
import GetTaskIdCard from '@/components/GetTaskIdCard.vue'
import FigureGenerateCard from '@/components/FigureGenerateCard.vue'
import LogCard from '@/components/LogCard.vue'

const progress = ref(48)
const taskId = ref<string>('NULL')
const fileUploadResponse = ref<FileUploadResponse | null>(null)
const taskIdUploadResponse = ref<string>()

const log = ref<string>('test')
onMounted(async () => {
  console.log(await getServerStatus())
})

const handleFile = async (event: Event) => {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  if (file) {
    taskId.value = 'NULL'
    fileUploadResponse.value = await uploadFile(file)
    console.log(fileUploadResponse.value)
    taskId.value = fileUploadResponse.value?.task_id ?? ''
    return fileUploadResponse
  } else {
    console.log('No file selected')
  }
}

const handleUploadTaskId = async (taskId: string) => {
  if (taskId !== 'NULL') {
    taskIdUploadResponse.value = await uploadTaskId(taskId)
    console.log(taskIdUploadResponse.value)
  } else {
    console.log('No task id selected')
  }
}
</script>

<template>
  <article class="flex flex-col space-y-12">
    <GetTaskIdCard :taskId="taskId" @handleFile="handleFile" />
    <FigureGenerateCard :taskId :progress @handleUploadTaskId="handleUploadTaskId" />
    <LogCard :log="log" />
  </article>
</template>

<style lang="scss" scoped></style>
