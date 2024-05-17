import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import CategoryView from '@/views/CategoryView.vue'
import ReviewView from '@/views/ReviewView.vue'
import ProfileView from '@/views/ProfileView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path : '/',
      name : 'MainView',
      component : MainView,
    },
    {
      path : '/category',
      name : 'CategoryView',
      component : CategoryView
    },
    {
      path : '/review',
      name : 'ReviewView',
      component : ReviewView
    },
    {
      path : '/profile',
      name : 'ProfileView',
      component : ProfileView
    }
  ]
})

export default router
