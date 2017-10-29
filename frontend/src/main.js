import Vue from 'vue'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import App from './App'

Vue.use(ElementUI)
// to index
Vue.prototype.$goRoute = function (index) {
  this.$router.push(index)
}
Vue.prototype.$goRoute = function (personal) {
  this.$router.push(personal)
}
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})

new Vue({
  el: '#personal',
  router,
  render: h => h(App)
})
