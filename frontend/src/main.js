import './assets/main.css'
import { autoAnimatePlugin } from '@formkit/auto-animate/vue'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios' // 1. Импортируем axios

import App from './App.vue'
import router from './router'

axios.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('admin_token') // Берем токен из хранилища
    if (token) {
      // Если токен есть, добавляем его в заголовки по стандарту Bearer
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  },
)

const app = createApp(App)

app.use(autoAnimatePlugin)
app.use(createPinia())
app.use(router)

app.mount('#app')
