import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path:'/',
    name:'home',
    component:HomeView,
    meta:{
      title:"HUST Stuti"
    }
  },
]

// Vue3新特性，替换process.env.BASE_URL为import.meta.env.BASE_URL
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

router.beforeEach((to,from)=>{
  document.title = to.meta.title;
})

// title兜底
router.beforeEach((to, from) => {
  document.title = to.meta.title || 'HUST Stuti';
})

export default router
