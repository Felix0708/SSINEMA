<template>
  <div v-on:click="getMovieDetail()" class="card bg-black" style="width: 18rem;">
    <div class="card-img"><img :src="getImage" class="card-img-top" alt=""></div>
    
    <div class="card-body ml-4" >
      <h5 class="card-title" v-for="(item,idx) in getTitle" 
      :key="idx"><b>{{ item }}</b></h5>
      <!-- <p class="card-text">{{ getOverview }}</p> -->
    </div>
    <b-modal 
      ref="detail" 
      size="lg" 
      class="bg-black" 
      :header-bg-variant="black"
      :body-bg-variant="black"
      :footer-bg-variant="black"
      hide-footer hide-header>
        <MovieDetail
          :movie_pk = this.movie.movie_id
        />
      </b-modal>
  </div>
</template>

<script>
// import axios from 'axios'
import MovieDetail from '../components/MovieDetail.vue'
export default {
  props: {
    movie: Object
  },
  components: {
    MovieDetail
  },
  data(){
    return {
      black : 'black'
    }
  },
  computed: {
    getImage: function() {
      return 'http://image.tmdb.org/t/p/w185'+this.movie.poster_path
    },
    getTitle: function() {
      const t = this.movie.title
      // const len = length(t)
      const temp = t.split(' ')
      
      let res = []
      let tp = ''
      for(let i = 0; i < temp.length; i++){
        if(tp.length + temp[i].length < 12 ){ 
          tp += ' ' + temp[i]
        }else{
          res.push(tp)
          tp = temp[i]
        }
      }
      res.push(tp)
      return res
    },
    getOverview: function() {
      return this.movie.overview
    }
  },
  methods: {
    getMovieDetail() {
      // console.log(this.movie.title)
      console.log(this.movie)
      // this.$bvModal.show('detail')
      this.$refs['detail'].show()
      // console.log(this.movie)
      // this.$router.push({name: 'MovieDetail', params: {movie_pk: this.movie.movie_id}})
    },
  },
}
</script>

<style>
.bg-black{
  background-color: black;
  margin: 3%;
}
</style>