<template>
  <div class="home">
    <img src="https://fontmeme.com/permalink/211117/18c046fa6dc1dff4a68fda564614a5dd.png" alt="netflix-font" border="0">
    <div class="homeText">
      <h1>당신이 원하는 그 모든 영화 정보를 언제나</h1>
      <h3>커뮤니티로 정보 공유도 할 수 있어요.</h3>
      <div class="loginBtn">
        <button>
          <router-link :to="{ name: 'Login' }">
            지금 바로 이용 시작
          </router-link>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
      return {
        
      }
    },
}
</script>

<style scoped>
.home {
  width: 100vw;
  height: 100vh;
  text-align: center;
  position: relative;
  z-index: 1;
}
.home::after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  content: "";
  background-image: url("../../img_folder/movie-black-rotate.png");
  background-position: center;
  background-position-y: 25%;
  opacity: 0.5;
  z-index: -1;
}

img {
  margin-top: 30px;
  margin-right: 50px;
}

.homeText {
  opacity: 100;
  color: white;
  text-align: center;
  position: absolute;
  top: 30%;
  left: 20%;
}

h1 {
  margin-bottom: 20px;
}

h3 {
  margin-bottom: 20px;
}

.loginBtn {
  margin: 10px auto;
  width: 30%;
  height: 100%;
  padding: 8px;
  border: 1px solid rgb(185, 35, 85);
  background-color: rgb(185, 35, 85);
  border-radius: 18px;
  text-align: center;
  font-weight: bold;
}

.loginBtn > button > a {
  text-decoration: none;
  color: white;
}
</style>