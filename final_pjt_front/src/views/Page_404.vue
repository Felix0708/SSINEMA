<template>
  <div class="page404">
    <br>
    <br>
    <br>
    <img class="page404" src="../assets/err-img.png" alt="page404" width="500px" height="500px">
    <br>
    <br>
    <router-link :to="{ name: 'MainPage' }">
      <button class="back backtext">홈으로 돌아가기</button>  
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'Page_404'

}
</script>

<style scoped>
.page404 {
  margin: 0 auto;
  width: 80%;
  height: 80%;
}
</style>