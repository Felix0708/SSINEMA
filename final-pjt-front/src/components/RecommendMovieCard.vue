<template>
  <swiper-slide>
    <div class="card bgblack card-box" style="width: 15rem;" @click=getMovieDetail()>
      <div class="card-img">
        <img  :src="getImage" class="card-img-top cardImg" alt="poster">
      </div>
      
      <div class="card-body">
        <div class="card-title" v-for="(item,idx) in getTitle" :key="idx">{{ item }}</div>
      </div>
      
      <b-modal
      ref="detail" 
      size="lg" 
      class="bg-black"
      :header-bg-variant="black"
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
      return 'http://image.tmdb.org/t/p/w500' + this.movie.poster_path
    },
    getTitle: function() {
      const t = this.movie.title
      const temp = t.split(' ')

      let res = []
      let tp = ''
      for(let i = 0; i < temp.length; i++){
        if(tp.length + temp[i].length < 28 ){ 
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
      // console.log('영화 정보',this.movie.title)
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

.card-box {
  /* position: absolute; */
  height: 400px;
  transition: all 0.8s linear;
}

.card-box:hover {
  /* position: absolute; */
  /* top: 50%; */
  /* z-index: 10; */
  height: 100%;
  transform:scale(1.4);
}

</style>

<style scoped>
.card-body {
  display: grid;
  justify-content: center;
  /* padding: 0; */
}

.card-body > div {
  font-weight: bold;
  margin: auto 3px;
  text-align: center;
  color: white;
  font-size: 14px;
}

.cardImg {
  width: 235px;
  height: 300px;
  margin: 0;
}
</style>