<template>
  <!-- 특정영역이 화면 중앙에 몰려있다 ==> container 생성
  컨테이너 안에서 내용(검색바와 결과목록)이 구성되게 된다 -->
  <v-container style="background: #000000;">
    <!-- 컴포넌트1. 검색바 -->
    <search-bar />
    <!-- 컴포넌트2. 영화목록 -->
    <search-movie-list />
  </v-container>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue'
import SearchMovieList from '@/components/SearchMovieList.vue'

export default {
  name: 'Search',
  components: {
    SearchBar,
    SearchMovieList,
  }  

};
</script>

<style scoped>
::v-deep .v-application--wrap {
  min-height: fit-content;
}
</style>
