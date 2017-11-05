import Vue from 'vue'
// import axios from 'axios'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import App from './App'
import Vue from 'vuex'
import store from './vuex/store'

Vue.use(ElementUI)
Vue.use(Vuex)
// to index
// Vue.prototype.$ajax = axios
Vue.prototype.$goRoute = function (index) {
  this.$router.push(index)
}
Vue.prototype.$goRoute = function (personal) {
  this.$router.push(personal)
}
Vue.prototype.$goRoute = function (personalData) {
  this.$router.push(personalData)
}
/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  render: h => h(App)
})

new Vue({
  el: '#personal',
  router,
  render: h => h(App)
})

new Vue({
  el: '#personalData',
  router,
  render: h => h(App)
})
