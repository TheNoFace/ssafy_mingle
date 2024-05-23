import { createApp } from "vue"

// pinia
import { createPinia } from "pinia"
import piniaPluginPersistedstate from "pinia-plugin-persistedstate"

// bootstrap
import "bootstrap"
import "bootstrap/dist/css/bootstrap.min.css"

// fontawesome
import "@fortawesome/fontawesome-free/js/all.js"

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

// components
import App from "./App.vue"
import router from "./router"

const app = createApp(App)
const pinia = createPinia()
const vuetify = createVuetify({
  components,
  directives,
})

pinia.use(piniaPluginPersistedstate)
app
  .use(router)
  .use(pinia)
  .use(vuetify)
  .mount("#app")
