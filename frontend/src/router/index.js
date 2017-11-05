import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import Index from '@/components/Index'
import Course from '@/components/course/Course'
import Resource from '@/components/course/resource'
import Personal from '@/components/Personal'
import PersonalData from '@/components/PersonalData'
import Courseinfo from '@/components/course/Course_info'
import Router from 'vue-router'

Vue.use(ElementUI)
Vue.use(Router)
/* eslint-disable camelcase */
export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/index',
      name: 'index',
      component: Index
    },
    {
      path: '/',
      component: Index
    },
    {
      path: '/course',
      name: 'course',
      component: Course
    },
    {
      path: '/courseinfo',
      name: 'course_info',
      component: Courseinfo
    },
    {
      path: '/resource',
      name: 'resource',
      component: Resource
    },
    {
      path: '/personal',
      name: 'personal',
      component: Personal,
      children: [
        {
          path: '/personalData',
          name: 'personalData',
          component: PersonalData
        }
      ]
    }
  ]
})
