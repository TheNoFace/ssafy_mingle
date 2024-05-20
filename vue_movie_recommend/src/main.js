import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import '@fortawesome/fontawesome-free/js/all.js'

import App from './App.vue'
import router from './router'

const pinia = createPinia()
const app = createApp(App)

pinia.use(piniaPluginPersistedstate)
app.use(router)
app.use(pinia)

app.mount('#app')
