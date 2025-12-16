<script setup>
const props = defineProps({
  price: Number,
  name: String,
  image_url: String,
})
</script>

<template>
  <div class="item">
    <img class="item_image" :src="image_url" alt="" />
    <div class="item__info">
      <p class="item__price">{{ props.price }} ₽</p>
      <h3 class="item__name">{{ props.name }}</h3>
      <button class="item__button">В корзину</button>
    </div>
  </div>
</template>

<style scoped>
.item {
  overflow: hidden;
  background: var(--color-background-soft);
  border-radius: 15px;
  padding: 0 0 10px 0;
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
}
.item_image {
  width: 100%;
  height: 200px;
}
</style>
