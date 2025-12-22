import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AdminView from '@/views/AdminView.vue'
import AdminLoginView from '@/views/AdminLoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/admin',
      name: 'admin',
      component: AdminView,
    },
    {
      path: '/order-status',
      name: 'order-status',
      component: () => import('@/views/OrderStatusView.vue'),
    },
    {
      path: '/admin-login',
      name: 'admin-login',
      component: AdminLoginView,
    },
  ],
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('admin_token')

  const isAuthRequired = to.path === '/admin' || to.meta.requiresAuth
  const isLoginPage = to.name === 'admin-login'

  if (isAuthRequired && !token) {
    next({ name: 'admin-login' })
  } else if (isLoginPage && token) {
    next({ name: 'admin' })
  } else {
    next()
  }
})

export default router
