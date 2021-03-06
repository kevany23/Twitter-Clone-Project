import Vue from 'vue';
import VueRouter from 'vue-router';
import VueHome from '../views/VueHome.vue';
import Login from '../views/Login.vue';
import Home from '../views/Home.vue';
import SearchUser from '../views/SearchUser.vue';
import Profile from '../views/Profile.vue';
import DebugPage from '../views/Debug.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/vueHome',
    name: 'VueHome',
    component: VueHome,
  },
  {
    path: '/',
    redirect: '/login',
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
  },
  {
    path: '/searchUser',
    name: 'SearchUser',
    component: SearchUser,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
  },
  {
    path: '/debug',
    name: 'Debug',
    component: DebugPage,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
