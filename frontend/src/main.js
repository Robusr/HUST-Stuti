// Robusr 2026.2.3
// 前端全局配置

// import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

// 全局引入Vant组件库和全部样式
import Vant from 'vant'
import 'vant/lib/index.css'

// 创建Vue实例并注册Vant
const app = createApp(App)
app.use(Vant)

// 挂载Vant
app.mount('#app')

import App from './App.vue'
import router from './router'

// const app = createApp(App)

app.use(createPinia())
app.use(router)

// app.mount('#app')
