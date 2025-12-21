<script setup>
import { useCartStore } from '@/stores/cart'
import { computed, ref } from 'vue'

const cartStore = useCartStore()

const props = defineProps({
  product_id: Number,
  name: String,
  price: Number,
  quantity: Number,
  image_url: String,
})

const quantity = ref(props.quantity)

const increment = async () => {
  cartStore.updateQuantity(props.product_id, quantity.value + 1)
  quantity.value++
}

const decrement = async () => {
  if (quantity.value > 1) {
    cartStore.updateQuantity(props.product_id, quantity.value - 1)
    quantity.value--
  }
}

const delItemFromCart = async () => {
  cartStore.removeItem(props.product_id)
}
</script>

<template>
  <div class="cart-item">
    <div class="cart-item__delete" @click="delItemFromCart">
      <img src="../assets/image/delete-icon.svg" alt="" />
    </div>
    <img class="cart-item__image" :src="image_url" />
    <div class="cart-item__info">
      <div class="cart-item__title">{{ name }}</div>
      <div class="cart-item__price">{{ price * quantity }} ₽</div>
      <div class="cart-item__action">
        <div class="cart-item__count">
          <div class="cart-item__operation minus" @click="decrement">-</div>
          <div class="cart-item__quantity">{{ quantity }}</div>
          <div class="cart-item__operation" @click="increment">+</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.cart-item {
  position: relative;
  width: 100%;
  display: flex;
  gap: 10px;
  margin: 0 0 25px 0;
}
.cart-item__image {
  width: 100px;
  height: 100px;
  border-radius: 10px;
}
.cart-item__info {
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
.cart-item__title {
  font-size: 18px;
  font-weight: 700;
}
.cart-item__price {
  font-size: 16px;
  font-weight: 600;
  color: #ff4294;
  flex: 1;
}
.cart-item__action {
  margin: 0 0 3px 0;
  display: flex;
  gap: 20px;
}
.cart-item__count {
  display: flex;
  width: 120px;
  height: 25px;
  justify-content: space-between;
  align-items: center;
  padding: 0 12px;
  background: #e9edff;
  border-radius: 15px;
  cursor: pointer;
}
.cart-item__operation {
  font-size: 18px;
  margin: 0 0 3px 0;
  color: var(--button-background);
  font-weight: 800;
}
.minus {
  font-size: 22px;
  margin: 0 0 6px 0;
}
.cart-item__delete {
  position: absolute;
  top: 50%;
  right: 0;
  transform: translateY(-50%);
  display: flex;
  padding: 10px;
  justify-content: center;
  align-items: center;
  background: #ffe9e9;
  border-radius: 15px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 500;
}
.cart-item__delete img {
  width: 17px;
  height: 17px;
}
</style>
