<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'

const categories = ref(null)

const category_id = ref(null)
const name = ref(null)
const description = ref(null)
const image_url = ref(
  'https://sun9-56.userapi.com/s/v1/ig2/qjKu8xIISPVMc41J9l3pjpW3Zc9g7J0yAHcX-3W_9c1Ad7iDNkiUEqiqgRLM8btBJ_TkUsYAQ2kLTFGtl3F-AQI9.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,960x1280&from=bu&cs=960x0',
)
const price = ref(null)

const emit = defineEmits(['product-add-successfully'])

const createProduct = async () => {
  try {
    const { data } = await axios.post(`/api/products/add`, {
      name: name.value,
      description: description.value,
      image_url: image_url.value,
      price: price.value,
      category_id: category_id.value,
    })
    emit('product-add-successfully', data.product)
    name.value = description.value = category_id.value = price.value = null
  } catch (error) {
    console.log(error)
  }
}

onMounted(async () => {
  try {
    const { data } = await axios.get('/api/categories')
    categories.value = data
  } catch (error) {
    console.log(error)
  }
})
</script>

<template>
  <div class="create">
    <input v-model="name" type="text" class="create__input" placeholder="Название продукта" />
    <textarea
      v-model="description"
      type="text"
      class="create__input-desc"
      placeholder="Описание продукта"
    ></textarea>
    <div class="create__flex-design">
      <input v-model="price" type="text" class="create__input" placeholder="Цена продукта" />
      <select v-model="category_id" class="create__select-cat">
        <option v-for="cat in categories" :key="cat.id" :value="cat.id">{{ cat.name }}</option>
      </select>
    </div>
    <button @click="createProduct" class="create__button">Создать товар</button>
  </div>
</template>

<style scoped>
.create {
  width: 400px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 15px;
  border: 2px solid #000;
  border-radius: 10px;
}
.create__flex-design {
  display: flex;
  justify-content: space-between;
  gap: 10px;
}
.create__input {
  padding: 5px;
  border-radius: 5px;
  border: 1px solid #000;
}
.create__input-desc {
  resize: none;
  height: 100px;
  padding: 5px;
  font-size: 14px;
  border-radius: 5px;
  border: 1px solid #000;
}
.create__select-cat {
  flex: 1;
  border-radius: 5px;
  border: 1px solid #000;
}
.create__button {
  height: 30px;
  border-radius: 7px;
  background: #878787;
  color: #fff;
  border: none;
  transition: 0.05s;
}
.create__button:hover {
  background: #474747;
  font-size: 14px;
}
.create__button:active {
  background: #000;
  font-size: 14px;
}
</style>
