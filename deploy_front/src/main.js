import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import './plugins/vue-masonry'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import VueAwesomeSwiper from 'vue-awesome-swiper'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'swiper/css/swiper.css'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueAwesomeSwiper, /* { default options with global component } */)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
