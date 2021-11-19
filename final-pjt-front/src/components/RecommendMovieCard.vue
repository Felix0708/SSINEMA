<template>
  <swiper-slide>
    <div class="card bgblack" style="width: 15rem;" @click=getMovieDetail()>
      <div class="card-img"><img  :src="getImage" class="card-img-top" alt=""></div>
      
      <div class="card-body">
        <span class="card-title" v-for="(item,idx) in getTitle" :key="idx"><b>{{ item }}</b></span>
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
  </swiper-slide>
  
</template>

<script>
import MovieDetail from '../components/MovieDetail.vue'
export default {
  props: {
    movie:Object
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
    },
    
  },
  methods: {
    getMovieDetail() {
      console.log('TQ',this.movie.title)
      this.$refs['detail'].show()
    },
  },
}
</script>

<style>
.bgblack {
  background-color: black !important;
}

.modal_content
.modal_header
.modal_body {
  background-color: black;
}
</style>

<style scoped>
span {
  color: white;
  font-size: 14px;
}

img {
  width: 100%;
  height: 120%;
}
</style>