import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import Index from '@/components/Index'
import Course from '@/components/course/Course'
import Resource from '@/components/course/resource'
import Personal from '@/components/Personal'
import PersonalData from '@/components/PersonalData'
import Courseinfo from '@/components/course/Course_info'
import Thread from '@/components/forum/Thread'
import Forum from '@/components/forum/Forum'
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
      path: '/resource',
      name: 'resource',
      component: Resource
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
      path: '/course/page/:course_id',
      name: 'course_info',
      component: Courseinfo
    },
    {
      path: '/course/page/:course_id/resource',
      name: 'resource',
      component: Resource
    },
    {
      path: '/course/page/:course_id/forum',
      name: 'forum',
      component: Forum
    },
    {
      path: '/course/page/:course_id/forum/:thread_id',
      name: 'thread',
      component: Thread
    },
    {
      path: '/user/home/:username',
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
