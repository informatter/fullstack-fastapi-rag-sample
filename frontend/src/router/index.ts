import { createRouter, createWebHistory } from 'vue-router'
import { authGuard } from "@auth0/auth0-vue";

// lazy load components
const HomeView = () => import('../views/HomeView.vue');
const AuthCallbackPage = () => import ('@/components/AuthCallbackPage.vue')
const RagView = () => import ('@/views/RagView.vue')

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/callback',
      name: 'callback',
      component: AuthCallbackPage
    },
    {
      path: '/app',
      name: 'app',
      component: RagView,
      beforeEnter:authGuard
    }
  ]
})

export default router
