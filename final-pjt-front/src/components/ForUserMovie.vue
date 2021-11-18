<template>
  <swiper-slide>
    <div v-on:click="getMovieDetail()" class="card bgblack" style="width: 18rem;">
      <div class="card-img"><img :src="getImage" class="card-img-top" alt=""></div>
      
      <div class="card-body">
        <h5 class="card-title" v-for="(item,idx) in getTitle" :key="idx"><b>{{ item }}</b></h5>
      </div>
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
          :movie_pk = this.forusermovie.id
        />
    </b-modal>
  </swiper-slide>
</template>

<script>
import MovieDetail from '../components/MovieDetail.vue'
export default {
  props: {
    forusermovie: Object,
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
      return 'http://image.tmdb.org/t/p/w185'+this.forusermovie.poster_path
    },
    getTitle: function() {
      const t = this.forusermovie.title

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
      return this.forusermovie.overview
    }
  },
  methods: {
    getMovieDetail() {
      console.log('눌렀을 때',this.forusermovie)
      this.$refs['detail'].show()
    },
  },
}
</script>

<style>
.bgblack {
  background-color: black;
  
  
}
.card-img:hover {
  transform: scale(1.2)
  
  
}
.card-img {
  z-index: 2;
  width: 288px;
  height: 380px;
  margin-bottom: 60px;
  cursor: pointer;
  transition-duration: 1s;
  
}
.card-img-top {
  background-size: cover;
  box-shadow: 5px 5px 5px rgb(167, 152, 152);
}
.card-body {
  z-index: 3;
}
</style>