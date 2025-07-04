import instance from '@/lib/axiosInstance.ts'
import type { ServerStatus, UploadResponse } from '@/lib/model.ts'

export async function getServerStatus(): Promise<string> {
  const response = await instance.get<ServerStatus>('/rosmontis')
  return response.data.message
}

export async function uploadFile(file: File): Promise<UploadResponse> {
  const formData = new FormData()
  formData.append('file', file)
  const response = await instance.post('/uploads', formData)
  return response.data
}
