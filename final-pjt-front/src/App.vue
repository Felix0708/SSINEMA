<template>
  <div id="app">
    <div id="nav">
      <div class="isLogin" v-if="isLogin">
        <router-link :to="{ name: 'MainPage' }">
          <a href="/mainpage">
            <img src="../img_folder/SSINEMA.png" alt="logo">
          </a>
        </router-link>
        <router-link class="loginLink" @click.native="logout" to="#">
          <div class="loginText">로그아웃</div>
        </router-link>
      </div>
      <div class="isLogout" v-else>
        <router-link to="/">
          <a href="/">
            <img src="../img_folder/SSINEMA.png" alt="logo">
          </a>
        </router-link>
        <router-link class="loginLink" :to="{ name: 'Login' }">
          <div class="loginText">로그인</div>
        </router-link>
      </div>
    </div>
    <router-view @login="isLogin = true"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Home' })
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')

    if (token) {
      this.isLogin = true
    }
  },
}
</script>

<style>

#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  height: 100vh;
}

/* #nav {
  padding: 30px;
  display: flex;
  justify-content: space-between;
} */

#nav a {
  font-weight: bold;
  color: black;
}

/* #nav a.router-link-exact-active {
  color: #42b983; 
} */

</style>

<style scoped>

.isLogin {
  display: flex;
  justify-content: space-between;
}

.isLogout {
  display: flex;
  justify-content: space-between;
}

img {
  margin: -1px 0 0 3px;
  width: auto; 
  height: auto;
  max-width: 18%;
  max-height: 100%;
}

.loginLink {
  /* size: 1rem; */
  margin: auto 20px;
  padding: 6px 10px 6px 10px;
  text-decoration: none;
  border: 1px solid white;
  border-radius: 16px;
  background-color: white;
}

.loginText {
  font-size: 13px;
  text-align: center;
  /* font-weight: bold; */
}
</style>
