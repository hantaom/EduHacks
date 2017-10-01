import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import SearchStudent from '@/components/SearchStudent'
import ConnectStudent from '@/components/ConnectStudent'
import MainMentor from '@/components/MainMentor'
import ConnectMentor from '@/components/ConnectMentor'
import MainStudent from '@/components/MainStudent'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/MainStudent',
      name: 'MainStudent',
      component: MainStudent
    },
    {
      path: '/SearchStudent',
      name: 'SearchStudent',
      component: SearchStudent
    },
    {
      path: '/ConnectStudent',
      name: 'ConnectStudent',
      component: ConnectStudent
    },
    {
      path: '/MainMentor',
      name: 'MainMentor',
      component: MainMentor
    },
    {
      path: '/ConnectMentor',
      name: 'ConnectMentor',
      component: ConnectMentor
    },

  ]
})
