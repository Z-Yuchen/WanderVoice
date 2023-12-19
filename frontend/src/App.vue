<template>
  <div>
    <!-- <router-link to="/function">Go to Function Page</router-link> -->
    <!-- <button @click="goToAnotherPage">Go to Another Page</button> -->
    <!-- <Login /> -->
    <router-view :key="$route.fullPath"></router-view>

  </div>
</template>

<script>
// import Login from './components/Login.vue';

export default {
  name: 'LoginPage',
  // components: {
  //   Login
  // },
  methods: {
    goToAnotherPage() {
      const currentRoute = this.$route.path; // 获取当前路由路径
      console.log(currentRoute)
      const targetRoute = '/function'; // 要跳转的目标路由路径

      // 如果当前路由不是目标路由，则执行路由切换
      if (currentRoute !== targetRoute) {
        this.$router.push(targetRoute);
        setTimeout(() => {
          }, 100); // 可以根据需要调整延迟时间
      }
    }
  }
}
</Script>