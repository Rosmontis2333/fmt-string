import axios, {
  AxiosError,
  type AxiosInstance,
  type AxiosResponse,
  type InternalAxiosRequestConfig,
} from 'axios'

axios.defaults.withCredentials = true

const instance: AxiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  timeout: 3000,
  withCredentials: false,
})

instance.interceptors.request.use(
  async (config: InternalAxiosRequestConfig) => {
    return config
  },
  (error: AxiosError) => {
    console.log(error.response)
    return Promise.reject(error)
  },
)

instance.interceptors.response.use(
  (response: AxiosResponse) => {
    return response
  },
  (error: AxiosError) => {
    console.log(error.response)
    return Promise.reject(error)
  },
)

export default instance
