<script setup>
import { ref } from 'vue'
import { useCartStore } from '@/stores/cart'

const cartStore = useCartStore()

const emit = defineEmits(['closeInfoClient'])

const handleClose = () => {
  emit('closeInfoClient')
}

const email = ref('')
const tel = ref('')
const address_city = ref('')
const address_street = ref('')
const address_index = ref('')

const handleCheckout = async () => {
  if (
    email.value &&
    tel.value &&
    address_city.value &&
    address_street.value &&
    address_index.value
  ) {
    const body = {
      email: email.value,
      tel: tel.value,
      address: `${address_city.value}, ${address_street.value}, ${address_index.value}`,
    }
    await cartStore.checkout(body)
  } else {
    alert('Поля не должны быть пустыми')
  }
}
</script>

<template>
  <div class="client">
    <div class="client_form">
      <div class="client__title">Информация для доставки</div>
      <input v-model="tel" type="tel" placeholder="Номер" autocomplete="tel" />
      <input v-model="email" type="email" placeholder="Почта" autocomplete="email" />
      <input v-model="address_city" type="text" placeholder="Город" autocomplete="" />
      <input
        v-model="address_street"
        type="text"
        placeholder="Улица, дом, кваритра"
        autocomplete=""
      />
      <input v-model="address_index" type="text" placeholder="Почтовый индекс" autocomplete="" />
      <div class="client__back" @click="handleClose">Вернуться в корзину</div>
      <button class="client__button" @click="handleCheckout">Перейти к оплате</button>
    </div>
  </div>
</template>

<style scoped>
.client {
  position: fixed;
  width: 100%;
  height: 100vh;
  background: #00000064;
  z-index: 100;
  display: flex;
  justify-content: center;
  align-items: center;
}
.client_form {
  display: flex;
  flex-direction: column;
  width: 400px;
  padding: 20px;
  background: #fff;
  border-radius: 10px;
}
.client_form input {
  margin: 0 0 10px 0;
  padding: 4px 8px;
  border-radius: 5px;
  outline: none;
}
.client_form input:focus {
  box-shadow: 1px 1px #333;
}
.client__title {
  font-size: 18px;
  margin: 0 0 10px 0;
}
.client__button {
  border: none;
  padding: 10px;
  color: #fff;
  background: var(--button-background);
  border-radius: 7px;
  cursor: pointer;
}
.client__back {
  cursor: pointer;
  font-size: 14px;
  margin: 2px 0 10px 0;
  color: #333;
  text-decoration: none;
}
</style>
