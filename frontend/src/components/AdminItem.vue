<script setup>
import axios from 'axios'

const props = defineProps({
  id: Number,
  price: Number,
  name: String,
  description: String,
  image_url: String,
  category_name: String,
})

const emit = defineEmits(['product-deleted-successfully'])

const removeProduct = async () => {
  try {
    const { data } = await axios.delete(`/api/products/delete/${props.id}`)
    emit('product-deleted-successfully', props.id)
  } catch (error) {
    console.log(error)
  }
}
</script>

<template>
  <div class="item">
    <img class="item_image" :src="image_url" alt="" />
    <div class="item__info">
      <div class="item__price">
        {{ props.price }} ₽
        <div class="cat-info">{{ props.category_name }}</div>
      </div>
      <h3 class="item__name">{{ props.name }}</h3>
      <p class="item__desc">{{ props.description }}</p>
      <button @click="removeProduct" class="item__button">Удалить товар</button>
    </div>
  </div>
</template>

<style scoped>
.item {
  display: flex;
  flex-direction: column;
  overflow: hidden;
  background: var(--color-background-soft);
  border-radius: 15px;
  padding: 0 0 10px 0;
}
.item__info {
  display: flex;
  flex-direction: column;
  width: 92%;
  margin: 0 auto;
  flex: 1;
}
.item__price {
  position: relative;
  color: #ff4294;
  font-size: 16px;
  font-weight: 700;
}
.cat-info {
  position: absolute;
  right: 0px;
  top: 3px;
  color: #767676;
  font-size: 12px;
}
.item__name {
  font-size: 16px;
  line-height: 1.4;
  margin: 0 0 10px;
}
.item__desc {
  line-height: 1.1;
  font-size: 13px;
  margin: 0 0 10px 0;
  flex: 1;
  max-height: 100px;
  width: 100%;
  word-break: break-all;
  overflow: hidden;
}
.item__button {
  background: #ff4294;
  color: #fff;
  font-weight: 600;
  border: none;
  width: 100%;
  height: 30px;
  border-radius: 5px;
}
.item__button:hover {
  background: #dc2474;
}
.item__button:active {
  background: rgb(142, 0, 83);
}
.item_image {
  width: 100%;
  height: 200px;
}
</style>
