<template>
  <div class="order-status-container">
    <div v-if="status === 'pending'" class="status-box">
      <div class="spinner"></div>
      <h2>Подтверждаем оплату...</h2>
      <p>Обычно это занимает несколько секунд</p>
    </div>

    <div v-else-if="status === 'paid'" class="status-box success">
      <div class="icon">✅</div>
      <h1>Заказ оплачен!</h1>
      <p>Ваш заказ начал собираться!</p>
      <p>Всю информацию по срокам доставки отправим на почту в ближайшее время</p>
      <router-link to="/" class="btn">На главную</router-link>
    </div>

    <div v-else class="status-box error">
      <div class="icon">❌</div>
      <h1>Оплата не подтверждена</h1>
      <p v-if="attempts >= maxAttempts">
        Время ожидания истекло. Если деньги списались, свяжитесь со мной.
      </p>
      <p v-else>Платеж был отклонен или отменен.</p>
      <div class="actions">
        <router-link to="/" class="btn secondary">На главную</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import axios from 'axios'
import { useCartStore } from '@/stores/cart'
import { getSessionId } from '@/utils/session'

const cartStore = useCartStore()

const status = ref('pending')
const attempts = ref(0)
const maxAttempts = 5
let pollInterval = null

const checkStatus = async () => {
  try {
    const { data } = await axios.get('/api/payments/last-status', {
      headers: { 'x-session-id': getSessionId() },
    })

    if (data.status === 'paid') {
      status.value = 'paid'
      stopPolling()
      cartStore.items = []
      cartStore.total = 0
    } else if (data.status === 'failed') {
      status.value = 'failed'
      stopPolling()
    }
  } catch (error) {
    console.error('Ошибка проверки статуса:', error)
  }

  attempts.value++
  if (attempts.value >= maxAttempts && status.value === 'pending') {
    status.value = 'failed'
    stopPolling()
  }
}

const stopPolling = () => {
  if (pollInterval) clearInterval(pollInterval)
}

onMounted(() => {
  checkStatus()
  pollInterval = setInterval(checkStatus, 3000)
})

onUnmounted(() => {
  stopPolling()
})
</script>

<style scoped>
.status-box.success {
  border-top: 5px solid #4caf50;
}
.status-box.error {
  border-top: 5px solid #f44336;
}

.order-status-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  text-align: center;
  background-color: #f4f7f6;
}
.status-box {
  max-width: 450px;
  width: 100%;
  padding: 50px;
  border-radius: 24px;
  background: white;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
}
</style>
