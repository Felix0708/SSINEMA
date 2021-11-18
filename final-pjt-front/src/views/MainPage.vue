<template>
  <div class="bg-main">
    <a href="/">
      <img src="https://fontmeme.com/permalink/211118/6dfb6fa7875c07d34e39155bdbaf6638.png" alt="netflix-font" border="0">
    </a>
    <div class="mainText">
      <h1>당신이 원하는 그 모든 영화 정보를 언제나</h1>
      <h3>커뮤니티로 정보 공유도 할 수 있어요.</h3>
    </div>
    <div class="loginBtn">
      <button>
        <router-link :to="{ name: 'Login' }">
          지금 바로 이용 시작
        </router-link>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MainPage',
  created() {
    if (localStorage.getItem('jwt')) {
      this.$router.push({ name: 'Home' })
    }
  }
}
</script>

<style scoped>
.bg-main {
  width: 100%;
  /* height: 800px; */
  position: relative;
  /* margin-bottom: 250px; */
  z-index: 1;
}
.bg-main::after {
  position: absolute;
  top: 20px;
  left: 0;
  width: 100%;
  height: 70vh;
  content: "";
  background-image: url("../assets/main.png");
  background-position: center;
  background-size: auto;
  background-repeat: no-repeat;
  z-index: -1;
  opacity: 0.5;
}

img {
  margin-top: 30px;
  margin-right: 50px;
}

.mainText {
  opacity: 100;
  color: white;
  text-align: center;
  margin: 10% 0 0 0;
}

h1 {
  margin-bottom: 20px;
}

h3 {
  margin-bottom: 20px;
}

.loginBtn {
  margin: 10px auto;
  width: 20%;
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
