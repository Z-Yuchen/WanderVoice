import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './App.vue';
import Login from './components/Login.vue';
import SignUp from './components/SignUp.vue';
import Support from './components/Support.vue';
import About from './components/About.vue';
import TourGuide from './components/TourGuide.vue'
import RecommPage from './components/RecommPage.vue'
import FunctionsPage from './components/FunctionsPage.vue'
// import AudioRecorder from "vue-audio-recorder";


Vue.use(VueRouter);
// Vue.use(AudioRecorder);

const routes = [
  { path: '/', component: Login },
  { path: '/login', component: Login },
  { path: '/signup', component: SignUp },
  { path: '/support', component: Support },
  { path: '/app', component: App },
  { path: '/about', component: About },
  { path: '/functions', component: FunctionsPage },
  { path: '/tourguide', component: TourGuide },
  { path: '/recomm', component: RecommPage },
  
];
// eslint-disable-next-line
const router = new VueRouter({
  routes
});

new Vue({
    router,
    render: (h) => h(App)
  }).$mount('#app');