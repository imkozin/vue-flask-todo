import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { SnackbarService } from 'vue3-snackbar'
import 'vue3-snackbar/styles'

const app = createApp(App)

app.use(router)
app.use(SnackbarService)
app.mount('#app')
