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
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
