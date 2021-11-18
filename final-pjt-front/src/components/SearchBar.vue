<template>
  <div>
    <v-text-field
      v-model="title"
      outlined
      clearable
      @keypress.enter="searchMovies"
    >

      <template v-slot:prepend-inner>
        <!-- google material icon 사용 -->
        <v-icon>search</v-icon>
      </template>
    
      <template v-slot:append>
        <v-progress-circular
        v-if="loading"
        size="24" indeterminate color="primary" />
      </template>
    </v-text-field>
    <v-btn
      color="primary"
      elevation="2"
      icon
      tile
      @click="searchMovies"
    >
      <v-icon>search</v-icon>
    </v-btn>
  </div>
</template>

<script>
// import axios from 'axios'
import { mapActions } from 'vuex'

// const API_KEY = process.env.VUE_APP_TMDB_API_KEY
// const API_URL = `https://api.themoviedb.org/3/search/movie?api_key=${ API_KEY }&language=ko&query=`

export default {
  name: 'SearchBar',
  // data () {
  //   return {
  //     title: '',
  //     loading: false,
  //   }
  // },
  computed: {
    title: {
      // 값을 양방향 바인딩을 통해서 input에서 직접 수정할때는 setter를 지정하여 store의 mutations를 통해 title이 수정되는 구조로 만들어야 한다.

      // Getter
      get () {
        return this.$store.state.movie.title
      },
      
      // Setter
      set(title) {
        this.$store.commit('movie/updateState', {
          title
        })
      }
    },
    loading () {
      return this.$store.state.movie.loading
    }
  },
  methods: {
    // movie라는 store안에 있는 searchMovies 라는 actions을 method에 바인딩 하겠다
    ...mapActions('movie',[
      'searchMovies'
    ])
    // searchMovies() {
    //   this.$store.dispatch('movie/searchMovies')
    // }
    // // async searchMovies () {
    // //   this.loading = true
    // //   const res = await axios.get(API_URL + this.title)
    // //   console.log(res.data.results)
    // //   this.loading = false

    // //   // axios.get(API_URL + this.title)
    // //   //   .then((response) => {
    // //   //     console.log(response)

      
    // // }
  }
}
</script>

<style>

</style>