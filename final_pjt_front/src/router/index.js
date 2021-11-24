import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '@/views/Login'
import Signup from '@/views/Signup'
import MainPage from '@/views/MainPage'
import Profile from '@/views/Profile'
import Community from '@/views/Community'
import CreateArticle from '@/views/CreateArticle'
import UpdateArticle from '@/views/UpdateArticle'
import OtherProfile from '@/views/OtherProfile'
import MovieList from '@/views/MovieList'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MainPage',
    component: MainPage
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
  },
  {
    path: '/community',
    name: 'Community',
    component: Community,
  },
  {
    path: '/createarticle',
    name: 'CreateArticle',
    component: CreateArticle,
  },
  {
    path: '/updatearticle',
    name: 'UpdateArticle',
    component: UpdateArticle,
    props: true,
  },
  {
    path: '/otherprofile',
    name: 'OtherProfile',
    component: OtherProfile,
    // props: true,
  },
  {
    path: '/movieList',
    name: 'MovieList',
    component: MovieList,
    props: true,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
