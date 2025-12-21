<script setup>
import Item from '@/components/Item.vue'
import Cart from '@/components/Cart.vue'
import ItemCard from '@/components/ItemCard.vue'
import Tooltip from '@/components/Tooltip.vue'
import axios from 'axios'
import { onMounted, ref, watch } from 'vue'
import { debounce } from 'lodash'
import { useCartStore } from '@/stores/cart'

const cartStore = useCartStore()
const items = ref(null)
const inputSearch = ref('')
const categories = ref(null)
const activeCategoryId = ref(4) // 4 - ID для "Все товары"

const isOpenCard = ref(false)
const infoOpenCard = ref(null)

const isOpenCart = ref(false)

const fetchItems = debounce(async () => {
  let url = ''

  if (inputSearch.value.trim().length > 0) {
    url = `/api/products/search?query=${inputSearch.value.trim()}`
    activeCategoryId.value = 4
  } else if (activeCategoryId.value === 4) {
    url = '/api/products'
  } else {
    url = `/api/products/category/${activeCategoryId.value}`
  }

  try {
    const { data } = await axios.get(url)
    items.value = data.products
  } catch (error) {
    console.error('Error fetching items:', error)
    items.value = []
  }
}, 300)

watch(inputSearch, () => {
  fetchItems()
})

const selectedCategory = (cat_id) => {
  activeCategoryId.value = cat_id
  inputSearch.value = ''
  fetchItems()
}

onMounted(async () => {
  try {
    const { data } = await axios.get('/api/categories')
    categories.value = data
  } catch (error) {
    console.log(error)
  }
})

onMounted(() => {
  fetchItems()
})

onMounted(() => {
  cartStore.fetchCart()
})

watch(isOpenCard, (newValue) => {
  if (newValue) {
    document.body.style.overflow = 'hidden'
  } else {
    document.body.style.overflow = ''
  }
})

watch(isOpenCart, (newValue) => {
  if (newValue) {
    document.body.style.overflow = 'hidden'
  } else {
    document.body.style.overflow = ''
  }
})

const openCart = () => {
  isOpenCart.value = true
}

const openCard = (item) => {
  isOpenCard.value = true
  infoOpenCard.value = item
}

const handleDragEnd = () => {
  isOpenCard.value = false
  infoOpenCard.value = null
}

const handleCloseCart = () => {
  isOpenCart.value = false
}
</script>

<template>
  <div class="container">
    <Cart :style="{ display: isOpenCart ? 'block' : 'none' }" @close="handleCloseCart" />
    <ItemCard
      v-if="isOpenCard"
      :image_url="infoOpenCard.image_url"
      :name="infoOpenCard.name"
      :description="infoOpenCard.description"
      :price="infoOpenCard.price"
      :product_id="infoOpenCard.id"
      @drag-end="handleDragEnd"
    />
    <div class="cart__btn" @click="openCart">
      <Tooltip text="Открыть корзину"></Tooltip>
      <img src="../assets/image/cart_icon.svg" alt="" /><span class="cart__btn-span">{{
        cartStore.items.length
      }}</span>
    </div>
    <header class="header">
      <input type="text" placeholder="Искать товар" class="header__input" v-model="inputSearch" />
      <div class="header__category">
        <div
          class="category__item"
          v-for="cat in categories"
          :key="cat.id"
          @click="selectedCategory(cat.id)"
          :class="{ 'category__item-active': cat.id === activeCategoryId }"
        >
          {{ cat.name }}
        </div>
      </div>
    </header>
    <main class="main">
      <Item
        v-for="item in items"
        :key="item.id"
        :price="item.price"
        :name="item.name"
        :image_url="item.image_url"
        :product_id="item.id"
        @click="openCard(item)"
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
  transition: 0.2s;
  cursor: pointer;
}
.main {
  background: var(--color-background-mute);
  display: grid;
  gap: 10px;
  grid-template-columns: repeat(6, 1fr);
  padding: 10px 20px;
}
@media screen and (max-width: 1440px) {
  .main {
    grid-template-columns: repeat(5, 1fr);
  }
}
@media screen and (max-width: 1070px) {
  .main {
    grid-template-columns: repeat(4, 1fr);
  }
}
@media screen and (max-width: 865px) {
  .main {
    grid-template-columns: repeat(3, 1fr);
  }
}
@media screen and (max-width: 665px) {
  .main {
    padding: 7px;
    grid-template-columns: repeat(2, 1fr);
  }
}
@media screen and (max-width: 420px) {
  .main {
    grid-template-columns: 1fr;
  }
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
  cursor: pointer;
}
@media screen and (min-width: 500px) {
  .cart__btn {
    width: 85px;
    height: 85px;
    bottom: 30px;
    right: 30px;
  }
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
@media screen and (min-width: 500px) {
  .cart__btn-span {
    right: 15px;
    top: 10px;
    font-size: 14px;
  }
}
.category__item-active {
  background: #ffb62f;
  color: #fff;
  font-size: 13px;
  font-weight: 700;
}
</style>
