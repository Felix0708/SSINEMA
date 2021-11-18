<template>
  <div id="app">
    <div id="nav">
      <div class="isLogin" v-if="login">
        <router-link :to="{ name: 'MainPage' }">
          <a href="/">
            <img src="https://fontmeme.com/permalink/211118/422000f0de99430e1e601da94a274ec4.png" alt="netflix-font" border="0">
          </a>
        </router-link>
        <div class="d-flex">
          <router-link class="profileLink me-2" to="/profile">
            <svg width="1.5em" height="1.5em" viewBox="0 0 21 21" class="bi bi-person-square" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" d="M14 1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>
              <path fill-rule="evenodd" d="M2 15v-1c0-1 1-4 6-4s6 3 6 4v1H2zm6-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
            </svg>
            <div class="profileText">내 프로필</div> 
          </router-link>
          <router-link class="logoutLink me-2" @click.native="logout" to="#">
            <div class="logoutText">로그아웃</div>
          </router-link>
        </div>
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
  /* color: #2c3e50; */
}
nav {
  padding: 30px;
}
#nav a {
  font-weight: bold;
  /* color: #2c3e50; */
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

.logoutLink {
  margin: auto 20px;
  padding: 2px 10px 2px 10px;
  text-decoration: none;
  border: 1px solid white;
  border-radius: 16px;
  background-color: white;
  color: black;
}

.loginLink {
  margin: auto 20px;
  padding: 2px 10px 2px 10px;
  text-decoration: none;
  border: 1px solid white;
  border-radius: 16px;
  background-color: white;
  color: black;
}
.profileLink {
  display: flex;
  color: white;
}

a {
  text-decoration: none;
  color: black;
  font-weight: bold;
  margin: auto 0;
  text-align: center;
}

.logoutText {
  margin: 1.5px 0 0 0 ;
}

.loginText {
  margin: 1.5px 0 0 0 ;
}

img {
  margin: 5px 0 0 2px;
}

</style>
