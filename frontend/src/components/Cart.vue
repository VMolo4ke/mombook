<script setup>
import CartItem from './CartItem.vue'
import { useCartStore } from '@/stores/cart'
import InfoClient from './InfoClient.vue'
import { ref } from 'vue'

const cartStore = useCartStore()
const isOpenCheckout = ref(false)

const emit = defineEmits(['close'])

const handleClose = () => {
  emit('close')
}

const closeInfoClient = () => {
  isOpenCheckout.value = false
}

const toCheckout = async () => {
  isOpenCheckout.value = true
}
</script>

<template>
  <div class="cart__container">
    <InfoClient
      :style="{ display: isOpenCheckout ? 'flex' : 'none' }"
      @closeInfoClient="closeInfoClient"
    />
    <div class="cart__overlay"></div>
    <div class="cart">
      <div class="cart__head">
        <img class="cart__close" src="../assets/image/arrow-left.svg" @click="handleClose" />
        <h2 class="cart__title">Корзина</h2>
      </div>
      <div class="cart__content" v-auto-animate>
        <CartItem
          v-for="item in cartStore.items"
          :key="item.product_id"
          :name="item.name"
          :price="item.price"
          :quantity="item.quantity"
          :image_url="item.image_url"
          :product_id="item.product_id"
        />
      </div>
      <div class="cart__pay">
        <div class="cart__total">
          <span>Итого</span><span></span><span>{{ cartStore.total }} ₽</span>
        </div>
        <button class="cart__button" @click="toCheckout" :disabled="cartStore.items.length === 0">
          Оплатить
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.cart__overlay {
  z-index: 5;
  position: fixed;
  width: 100%;
  height: 100vh;
  background: #000;
  opacity: 0.7;
}
.cart {
  right: 0;
  z-index: 10;
  position: fixed;
  height: 100vh;
  width: 100%;
  max-width: 430px;
  background: #fff;
  border: 1px solid var(--color-background-mute);
  display: flex;
  flex-direction: column;
  transition: 1s;
}
.cart__content {
  width: 95%;
  margin: 0 auto 90px;

  overflow: scroll;
  -ms-overflow-style: none;
  scrollbar-width: none;
}
.cart__content::-webkit-scrollbar {
  display: none;
}
.cart__pay {
  position: absolute;
  bottom: -3px;
  padding: 5px 0 20px 0;
  width: 95%;
  left: 2.5%;
  background: var(--color-background);
}
.cart__total {
  font-size: 18px;
  display: flex;
  align-items: center;
  gap: 5px;
  margin: 0 0 10px 0;
}
.cart__total span:nth-child(2) {
  border-bottom: 1px dashed #000;
  height: 16px;
  flex: 1;
}
.cart__button {
  cursor: pointer;
  background: var(--button-background);
  color: #fff;
  font-weight: 600;
  border: none;
  width: 100%;
  height: 40px;
  border-radius: 5px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
}
@media screen and (max-width: 500px) {
  .cart__button {
    margin: 0 auto 30px;
  }
}
@media screen and (max-width: 500px) {
  .client {
    background: var(--color-background-);
  }
}
.cart__head {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
  margin: 0 0 10px 0;
}
.cart__close {
  margin: 3px 0 0 0;
  width: 25px;
  transition: 0.2s;
  cursor: pointer;
}
.cart__close:hover {
  scale: 1.1;
  transform: translate3d(-1px, -1px, 0);
}
</style>
