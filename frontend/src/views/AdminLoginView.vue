<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const router = useRouter()

const login = async () => {
  try {
    const formData = new FormData()
    formData.append('username', username.value)
    formData.append('password', password.value)

    const { data } = await axios.post('http://localhost:8000/login', formData)

    localStorage.setItem('admin_token', data.access_token)

    router.push('/admin')
  } catch (error) {
    alert('Неверный логин или пароль')
  }
}
</script>

<template>
  <div class="login-form">
    <input v-model="username" placeholder="Логин" />
    <input v-model="password" type="password" placeholder="Пароль" />
    <button @click="login">Войти</button>
  </div>
</template>
