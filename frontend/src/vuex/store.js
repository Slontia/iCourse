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
    course_code: ''
  },
  mutations: {
  }
})
export default store
