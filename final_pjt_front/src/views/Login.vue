<template>
  <div class="Login">
    <div>
    <div class="loginText">로그인</div>
    <div class="container">
      <div class="username">
        <label for="username"></label>
        <input 
          type="text" 
          id="username"
          v-model="credentials.username"
          placeholder="  아이디"
        >
      </div>
      <p style="border: 0.1px solid black; margin: auto"></p>
      <div class="password">
        <label for="password"></label>
        <input 
          type="password" 
          id="password"
          v-model="credentials.password"
          @keyup.enter="login"
          placeholder="  비밀번호"
        >
      </div>
    </div>
    </div>
    <div class="loginBtn">
      <button @click="login">로그인</button>
    </div>
    <div class="signupBtn">
      <button>
        <router-link :to="{ name: 'Signup' }">
          아직 회원이 아니신가요?
        </router-link>
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/api/v1/accounts/login/',
        data: this.credentials,
      })
        .then(res => {
          // console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push({ name: 'Home' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
.Login {
  margin: 25vh 0 0 0;
  width: 100%;
  height: auto;
  color: white;
}

.loginText {
  text-align: center;
  margin-bottom: 5px;
}

.container {
  width: 30%;
  height: 100%;
  padding: 0;
  border: 1px solid grey;
  border-radius: 10px;
  background-color: white;
}

input {
  width:100%;
  padding : 0 0 0 10px; 
}

input:focus {
  outline:none;
}

.username {
  padding: 8px 0 8px 0;
}

.password {
  padding: 8px 0 8px 0;
}

.loginBtn {
  margin: 10px auto;
  width: 30%;
  height: 100%;
  padding: 8px;
  border: 1px solid #FF0558;
  background-color: #FF0558;
  border-radius: 18px;
  text-align: center;
  font-weight: bold;
}

.signupBtn {
  margin: auto 0;
  text-align: center;
}

.signupBtn > button > a {
  text-decoration: none;
  color: white;
}

</style>
