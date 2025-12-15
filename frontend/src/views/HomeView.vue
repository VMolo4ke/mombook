<script setup>
import Item from '@/components/Item.vue'
import Cart from '@/components/Cart.vue'
import axios from 'axios'
import { onMounted, ref } from 'vue'

const items = ref(null)

onMounted(async () => {
  try {
    const { data } = await axios.get('/api/products')
    items.value = data.products
  } catch (error) {
    console.log(error)
  }
})
</script>

<template>
  <div class="container">
    <Cart />
    <div class="cart__btn">
      <img src="../assets/image/cart_icon.svg" alt="" /><span class="cart__btn-span">1</span>
    </div>
    <header class="header">
      <input type="text" placeholder="Искать товар" class="header__input" />
      <div class="header__category">
        <div class="category__item">Книжки</div>
        <div class="category__item">Игрушка</div>
      </div>
    </header>
    <main class="main">
      <Item
        v-for="item in items"
        :key="item.id"
        :price="item.price"
        :name="item.name"
        :image_url="item.image_url"
      />
    </main>
  </div>
</template>

<style scoped>
.header {
  width: 95%;
  padding: 10px 0 0 0;
  margin: 0 auto 20px;
}
.header__input {
  width: 100%;
  height: 30px;
  background: var(--color-background-mute);
  padding: 0 0 0 10px;
  border-radius: 5px;
  border: none;
  outline: none;
  margin: 0 0 7px 0;
}
.header__input:hover {
  border: 1px solid var(--color-border-hover);
}
.header__category {
  display: flex;
  gap: 10px;
}
.category__item {
  background: var(--color-background-mute);
  padding: 5px 10px;
  border-radius: 10px;
  font-size: 12px;
}
.main {
  background: var(--color-background-mute);
  padding: 5px 0 0 0;
  display: grid;
  grid-template-columns: 1fr 1fr; /* Две колонки, каждая занимает 50% доступной ширины */
  gap: 10px;
}
.cart__btn {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  bottom: 10px;
  right: 10px;
  background: rgba(0, 0, 0, 0.8);
}
.cart__btn img {
  width: 45%;
}
.cart__btn-span {
  font-weight: 700;
  font-size: 12px;
  border-radius: 50%;
  position: absolute;
  color: #fff;
  top: 5px;
  right: 8px;
}
</style>
