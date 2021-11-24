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
          <search-bar></search-bar>
          <router-link class="communityLink me-3" to="/community">
            <svg style="margin-top: 2px;" width="1.5em" height="1.5em" viewBox="0 0 21 21" class="bi bi-chat-square-text" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" d="M14 1H2a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h2.5a2 2 0 0 1 1.6.8L8 14.333 9.9 11.8a2 2 0 0 1 1.6-.8H14a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 0a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2.5a1 1 0 0 1 .8.4l1.9 2.533a1 1 0 0 0 1.6 0l1.9-2.533a1 1 0 0 1 .8-.4H14a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>
              <path fill-rule="evenodd" d="M3 3.5a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5zM3 6a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9A.5.5 0 0 1 3 6zm0 2.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5z"/>
            </svg>
            <b>커뮤니티</b>
          </router-link>
          <router-link class="profileLink me-3" to="/profile">
            <svg style="margin-top: 2px;" width="1.5em" height="1.5em" viewBox="0 0 21 21" class="bi bi-person-square" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
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
import SearchBar from '@/components/SearchBar.vue'

export default {
  name: 'App',
  components: {
    SearchBar,
  },
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
    },
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
  font-family: 'Hahmlet', sans-serif, Avenir, Helvetica, Arial;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /* color: #2c3e50; */
}
/* #nav { */
  /* padding: 30px; */
  /* background-color: rgb(39, 37, 37); */
  /* background-image: url('./assets/user-hero-bg4.jpg'); */
  /* margin-bottom: 50px; */
/* } */
#nav a {
  font-weight: bold;
  /* color: #2c3e50; */
}
/* #nav a.router-link-exact-active {
  color: #42b983;
} */
</style>

<style scoped>

#nav {
  /* padding: 30px; */
  background-color: rgb(22, 21, 21);
  /* background-image: url('./assets/user-hero-bg4.jpg'); */
  /* margin-bottom: 50px; */
}

.isLogin {
  display: flex;
  justify-content: space-between;
}

.isLogout {
  display: flex;
  justify-content: space-between;
}

.logoutLink {
  margin: auto 0;
  padding: 2px 10px 2px 10px;
  text-decoration: none;
  border: 1px solid #FF0558;
  border-radius: 16px;
  color:#dcddd8;
  background:#FF0558;
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

.communityLink {
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
  padding-bottom: 3px;
}

.loginText {
  margin: 1.5px 0 0 0 ;
}

img {
  margin: 5px 0 0 2px;
}

/* search */



</style>
