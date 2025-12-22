import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { getSessionId } from '@/utils/session'

export const useCartStore = defineStore('cart', () => {
  const items = ref([])
  const total = ref(0)

  const getCartHeaders = () => ({
    headers: { 'x-session-id': getSessionId() },
  })

  const checkout = async (body) => {
    try {
      const { data } = await axios.post(
        'http://localhost:8000/payments/create',
        body,
        getCartHeaders(),
      )

      const paymentUrl = data.confirmation_url

      if (paymentUrl) {
        window.location.href = paymentUrl
      }
    } catch (error) {
      console.error('Ошибка при оформлении заказа:', error.response?.data || error)
      alert('Не удалось создать платеж.')
    }
  }

  const fetchCart = async () => {
    try {
      const { data } = await axios.get('http://localhost:8000/cart/', getCartHeaders())
      items.value = data.items
      total.value = data.total
    } catch (error) {
      console.log(error)
    }
  }

  const addToCart = async (productId, quantity = 1) => {
    try {
      const { data } = await axios.post(
        'http://localhost:8000/cart/items',
        { product_id: productId, quantity },
        getCartHeaders(),
      )
      items.value = data.items
      total.value = data.total
    } catch (error) {
      console.log(error)
    }
  }

  const updateQuantity = async (productId, quantity) => {
    try {
      const { data } = await axios.put(
        `http://localhost:8000/cart/items/${productId}?quantity=${quantity}`,
        {},
        getCartHeaders(),
      )
      items.value = data.items
      total.value = data.total
    } catch (error) {
      console.log(error)
    }
  }

  const removeItem = async (productId) => {
    try {
      const { data } = await axios.delete(
        `http://localhost:8000/cart/items/${productId}`,
        getCartHeaders(),
      )
      items.value = data.items
      total.value = data.total
    } catch (error) {
      console.log('Ошибка при удалении товара:', error)
    }
  }

  return { items, total, fetchCart, addToCart, updateQuantity, removeItem, checkout }
})
