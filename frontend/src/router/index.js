import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import LoginComponent from '../components/Login.vue'
import RegisterComponent from '../components/Register.vue'
import SupportComponent from '../components/Support.vue'
import ResultsComponent from '../components/Results.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginComponent
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterComponent
  },
  {
    path: '/support',
    name: 'Support',
    component: SupportComponent
  },
  {
    path: '/results',
    name: 'Results',
    component: ResultsComponent
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
