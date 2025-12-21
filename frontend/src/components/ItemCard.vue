<script setup>
import { ref, onUnmounted, computed } from 'vue'
import { useCartStore } from '@/stores/cart'

const cartStore = useCartStore()

const props = defineProps({
  product_id: Number,
  image_url: String,
  name: String,
  description: String,
  price: Number,
})

const emit = defineEmits(['drag-end'])

const stick = ref(null)
const isDragging = ref(false)
const translateY = ref(0)
const isAddedItems = computed(() =>
  cartStore.items.some((item) => item.product_id === props.product_id),
)

const delItemFromCart = async () => {
  cartStore.removeItem(props.product_id)
}

const addItemToCart = async () => {
  console.log(props.image_url)
  cartStore.addToCart(props.product_id)
}

const closeCard = () => {
  emit('drag-end')
}

const onPointerMove = (event) => {
  if (translateY.value > -10) translateY.value += event.movementY
}

const onPointerUp = (event) => {
  isDragging.value = true
  const rect = stick.value.getBoundingClientRect()
  const distanceToWindowBottom = window.innerHeight - rect.bottom
  if (distanceToWindowBottom < 100) {
    emit('drag-end')
  }
  translateY.value = 0

  window.removeEventListener('pointermove', onPointerMove)
  window.removeEventListener('pointerup', onPointerUp)
}

const onPointerDown = (event) => {
  isDragging.value = false
  event.target.setPointerCapture(event.pointerId)

  window.addEventListener('pointermove', onPointerMove)
  window.addEventListener('pointerup', onPointerUp)
}

onUnmounted(() => {
  window.removeEventListener('pointermove', onPointerMove)
  window.removeEventListener('pointerup', onPointerUp)
})
</script>

<template>
  <div class="card__container">
    <div class="card__overlay" @click="closeCard"></div>
    <div
      class="card"
      :class="{ 'card-dragging': isDragging }"
      ref="card"
      :style="{ transform: `translateY(${translateY}px)` }"
    >
      <img class="card__close" src="../assets/image/close-icon.svg" @click="closeCard" />
      <div class="card__stick" ref="stick" @pointerdown="onPointerDown">
        <div class="card__stick-real"></div>
      </div>
      <img :src="image_url" class="card__img" alt="" />
      <h3 class="card__name">{{ name }}</h3>
      <p class="card__desc">{{ description }}</p>
      <button v-if="!isAddedItems" class="card__button" @click.stop="addItemToCart">
        В корзину за {{ price }}
      </button>
      <button v-else @click.stop="delItemFromCart" class="item__button-added">Добавлено</button>
    </div>
  </div>
</template>

<style scoped>
.card__container {
  display: flex;
  justify-content: center;
}
.card {
  display: flex;
  flex-direction: column;
  z-index: 20;
  background: var(--color-background);
  width: 100%;
  height: 100vh;
  position: fixed;
  bottom: -20px;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
  touch-action: none;
}
@media screen and (min-width: 500px) {
  .card {
    padding: 10px 0 0 0;
    width: 500px;
    height: 90vh;
    bottom: 5%;
    border-radius: 15px;
  }
}
.card-dragging {
  transition: 0.8s;
}
.card__stick {
  margin: 0 auto;
  width: 150px;
  height: 22px;
  display: flex;
  align-items: center;
}
@media screen and (min-width: 500px) {
  .card__stick {
    display: none;
  }
}
.card__stick-real {
  width: 100%;
  height: 2px;
  background: var(--color-border-hover);
}
.card__overlay {
  position: fixed;
  z-index: 15;
  background: #000;
  opacity: 0.7;
  height: 100vh;
  width: 100%;
  top: 0;
}
.card__img {
  width: 80%;
  max-width: 300px;
  height: 300px;
  border-radius: 20px;
  display: block;
  margin: 0 auto;
}
.card__name {
  margin: 20px 0 0 10px;
  font-size: 24px;
  color: var(--color-text);
  font-weight: 600;
}
.card__desc {
  font-size: 14px;
  color: #676767;
  margin: 10px 0 0 10px;
  flex: 1;
}
.card__button {
  margin: 0 auto 40px;
  width: 90%;
  height: 40px;
  background: var(--button-background);
  color: #fff;
  font-weight: 600;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: 0.2s;
}
.card__button:hover {
  scale: 1.02;
}
.card__button:active {
  scale: 1.01;
}
@media screen and (min-width: 500px) {
  .card__button {
    margin: 0 auto 15px;
  }
}
.item__button-added {
  background: #ff4294;
  color: #fff;
  font-weight: 600;
  border: none;
  width: 90%;
  height: 40px;
  margin: 0 auto 40px;
  border-radius: 5px;
  cursor: pointer;
  transition: 0.2s;
}
.item__button-added:hover {
  scale: 1.02;
}
.item__button-added:active {
  scale: 1.01;
}
@media screen and (min-width: 500px) {
  .item__button-added {
    margin: 0 auto 15px;
  }
}
.card__close {
  position: absolute;
  width: 30px;
  height: 30px;
  right: 3px;
  top: 3px;
  cursor: pointer;
}
@media screen and (max-width: 500px) {
  .card__close {
    display: none;
  }
}
</style>
