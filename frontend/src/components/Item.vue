<script setup>
import { useCartStore } from '@/stores/cart'
import { computed, ref } from 'vue'

const cartStore = useCartStore()

const props = defineProps({
  product_id: Number,
  price: Number,
  name: String,
  image_url: String,
})

const isAddedItems = computed(() =>
  cartStore.items.some((item) => item.product_id === props.product_id),
)

const addItemToCart = async () => {
  cartStore.addToCart(props.product_id)
}

const delItemFromCart = async () => {
  cartStore.removeItem(props.product_id)
}
</script>

<template>
  <div class="item">
    <img class="item_image" :src="image_url" alt="" />
    <div class="item__info">
      <p class="item__price">{{ props.price }} ₽</p>
      <h3 class="item__name">{{ props.name }}</h3>
      <button v-if="!isAddedItems" class="item__button" @click.stop="addItemToCart">
        В корзину
      </button>
      <button v-else @click.stop="delItemFromCart" class="item__button-added">Добавлено</button>
    </div>
  </div>
</template>

<style scoped>
.item {
  overflow: hidden;
  background: var(--color-background-soft);
  border-radius: 15px;
  padding: 0 0 10px 0;
  width: 100%;
  min-width: 200px;
  max-width: 240px;
  margin: 0 auto;
  cursor: pointer;
}
.item__info {
  width: 92%;
  margin: 0 auto;
}
.item__price {
  color: #ff4294;
  font-size: 16px;
  font-weight: 700;
}
.item__name {
  font-size: 15px;
  line-height: 1.4;
  flex: 1;
  margin: 0 0 10px;
  width: 100%;
  overflow: hidden;
}
.item__button {
  background: var(--button-background);
  color: #fff;
  font-weight: 600;
  border: none;
  width: 100%;
  height: 30px;
  border-radius: 5px;
  cursor: pointer;
  transition: 0.2s;
}
.item__button:hover {
  transform: translate3d(-2px, -2px, 0);
  box-shadow: 3px 3px #000862;
}
.item__button:active {
  transform: translate3d(-1px, -1px, 0);
  box-shadow: 2px 2px #000862;
}
.item__button-added {
  background: #ff4294;
  color: #fff;
  font-weight: 600;
  border: none;
  width: 100%;
  height: 30px;
  border-radius: 5px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
.item__button-added:hover {
  transform: translate3d(-2px, -2px, 0);
  box-shadow: 3px 3px #770033;
}
.item__button-added:active {
  transform: translate3d(-1px, -1px, 0);
  box-shadow: 2px 2px #770033;
}
.item_image {
  width: 100%;
  height: 200px;
}
</style>
