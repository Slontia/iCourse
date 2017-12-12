import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    id: 0,
    name: '',
    size: '',
    intro: '',
    author: '',
    time: '',
    url: '',
    course_code: '',
    // state relating to login
    user_name: '',
    is_login: false,
    // state relating to debug
    dev: true
  },
  mutations: {
  }
})
export default store
