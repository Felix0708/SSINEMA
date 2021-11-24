<template>
  <div class="Signup">
    <div class="signupText">회원가입</div>
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
          placeholder="  비밀번호"
        >
      </div>
      <p style="border: 0.1px solid black; margin: auto"></p>
      <div class="passwordConfirmation">
        <label for="passwordConfirmation"></label>
        <input 
          type="password" 
          id="passwordConfirmation"
          v-model="credentials.passwordConfirmation"
          @keyup.enter="signup"
          placeholder="  비밀번호 확인"
        >
      </div>
    </div>
    <div class="signupBtn">
      <button @click="signup">계정 생성하기</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/api/v1/accounts/signup/',
        data: this.credentials
      })
        .then(() => {
          this.$router.push({ name: 'Login'})
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
.Signup {
  margin: 25vh 0 0 0;
  width: 100%;
  height: auto;
  color: white;
}

.signupText {
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

.passwordConfirmation {
  padding: 8px 0 8px 0;
}

.signupBtn {
  margin: 10px auto;
  width: 30vw;
  height: 100%;
  padding: 8px;
  border: 1px solid #FF0558;
  background-color: #FF0558;
  border-radius: 18px;
  text-align: center;
  font-weight: bold;
}

.signupBtn > button > a {
  text-decoration: none;
  color: white;
}
</style>