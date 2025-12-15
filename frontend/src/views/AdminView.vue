<script setup>
import AdminCreate from '@/components/AdminCreate.vue'
import AdminItem from '@/components/AdminItem.vue'
import { onMounted, ref } from 'vue'
import axios from 'axios'

const items = ref(null)

const handleDeleteSuccess = (deletedProductId) => {
  items.value = items.value.filter((item) => item.id !== deletedProductId)
}

const handleAddProduct = (dataProduct) => {
  items.value.push(dataProduct)
}

onMounted(async () => {
  try {
    const { data } = await axios.get(`/api/products`)
    items.value = data.products
  } catch (error) {
    console.log(error)
  }
})
</script>

<template>
  <div class="admin">
    <div class="admin__header">
      <AdminCreate @product-add-successfully="handleAddProduct" />
    </div>
    <div class="admin__main" v-auto-animate>
      <AdminItem
        v-for="item in items"
        :key="item.id"
        :id="item.id"
        :price="item.price"
        :name="item.name"
        :image_url="item.image_url"
        :description="item.description"
        :category_name="item.category.name"
        @product-deleted-successfully="handleDeleteSuccess"
      />
    </div>
  </div>
</template>

<style scoped>
.admin {
  display: flex;
  width: 100%;
  padding: 30px;
  gap: 30px;
}
.admin__main {
  width: 90%;
  display: grid;
  gap: 10px;
  grid-template-columns: 1fr 1fr 1fr 1fr;
}
</style>
