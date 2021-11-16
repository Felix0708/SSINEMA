<template>
  <div id="app">
    <div id="nav">
      <a href="/">
        <img src="../img_folder/movie-black.png" alt="logo">
      </a>
      <router-link class="link" :to="{ name: 'Login' }">
        <div class="loginText">로그인</div>
      </router-link>
    </div>
    <router-view/>
  </div>
</template>

<style scoped>
#app {
  color: black
}
#nav {
  position: fixed;
  width: 100%;
  z-index: 1;
  top: 0px;
  display: flex;
  background-color: black;
  justify-content: space-between;
  height: auto;
  max-height: 70px;
}

img {
  margin-left: 3px;
  width: auto; 
  height: auto;
  max-width: 80px;
  max-height: 700px;
}

.link {
  margin: auto 10px;
  color: black;
  text-decoration: none;
  width: 75px;
  height: 30px;
  border: 1px solid white;
  background-color: white;
  border-radius: 20px;
}

.link .loginText {
  margin-top: 2px;
  text-align: center;
}

</style>
