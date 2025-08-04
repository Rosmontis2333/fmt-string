import instance from '@/lib/axiosInstance.ts'
import type { ServerStatus, FileUploadResponse } from '@/lib/model.ts'

export async function getServerStatus(): Promise<string> {
  const response = await instance.get<ServerStatus>('/rosmontis')
  return response.data.message
}

export async function uploadFile(file: File): Promise<FileUploadResponse> {
  const formData = new FormData()
  formData.append('file', file)
  const response = await instance.post('/uploads', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })
  if (response.status === 200) {
    return response.data
  } else {
    throw new Error('Failed to upload file')
  }
}

export async function uploadTaskId(taskId: string): Promise<string> {
  const response = await instance.get(`/start?task_id=${taskId}`)
  if (response.status === 200) {
    return response.data.message
  } else {
    throw new Error('Failed to upload task id')
  }
}
