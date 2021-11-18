<template>
  <div id="app">
    <div id="nav">
      <div class="isLogin" v-if="login">
        <router-link :to="{ name: 'MainPage' }">
          <a href="/">
            <img src="https://fontmeme.com/permalink/211118/422000f0de99430e1e601da94a274ec4.png" alt="netflix-font" border="0">
          </a>
        </router-link>
        <router-link class="loginLink" @click.native="logout" to="#">
          <div class="loginText">로그아웃</div>
        </router-link>
      </div>
      <div class="isLogout" v-else>
        <router-link to="/">
          <a href="/">
            <img src="https://fontmeme.com/permalink/211118/422000f0de99430e1e601da94a274ec4.png" alt="netflix-font" border="0">
          </a>
        </router-link>
        <router-link class="loginLink" :to="{ name: 'Login' }">
          <div class="loginText">로그인</div>
        </router-link>
      </div>
    </div>
    <router-view @login="login = true"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      login: false,
    }
  },
  methods: {
    logout: function () {
      localStorage.removeItem('jwt')
      this.login = false
      this.$router.push({ name: 'MainPage' })
    }
  },
  created() {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.login = true
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
nav {
  padding: 30px;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
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

.loginLink {
  margin: auto 20px;
  padding: 2px 10px 2px 10px;
  text-decoration: none;
  border: 1px solid white;
  border-radius: 16px;
  background-color: white;
}

a {
  text-decoration: none;
  color: black;
  font-weight: bold;
  margin: auto 0;
  text-align: center;
}

.loginText {
  margin: 1.5px 0 0 0 ;
}

img {
  margin: 5px 0 0 2px;
}

</style>
