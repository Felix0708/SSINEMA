<template>
  <div>
    <img src="https://fontmeme.com/permalink/211118/6dfb6fa7875c07d34e39155bdbaf6638.png" alt="netflix-font" border="0">
    <br>
    <br>
    <br>
    <Sliders
      :movies="topRatedmovies"
      :title="topRatedTitle"
    />
    <Sliders
      :movies="latestmovies"
      :title="latestTitle"
    />
    <!-- <Sliders
      :movies="SFmovies"
      :title="SFTitle"
    />
    <Sliders
      :movies="horrormovies"
      :title="horrorTitle"
    />
    <Sliders
      :movies="Romancemovies"
      :title="RomanceTitle"
    /> -->

    <!-- <div @mouseover = "btnOn" @mouseleave= "btnOff">
      <h4 
      v-if="forusermovies.length !== 0" 
      class='text-left ml-3'>
      {{ username }}님의 취향저격 베스트 컨텐츠
      </h4>
      <swiper :options = "swiperOptions" ref = "rec">
        <ForUserMovie
          v-for="(forusermovie, idx) in forusermovies"
          :key="idx"
          :forusermovie="forusermovie"
          class="col-lg-2 col-md-4 col-sm-6 col-xs-12"
        />
        <div class="swiper-pagination" slot="pagination"></div>
        <div 
          v-if="buttonOn"
          class="swiper-button-prev swiper-button-white" 
          slot="button-prev" 
          @click = "Recprev"
        >
        </div>
        <div 
        v-if="buttonOn"
        class="swiper-button-next swiper-button-white" 
        slot="button-next" 
        @click = "Recnext"
        >
        </div>
      </swiper>
    </div> -->
  </div>
</template>

<script>
import Sliders from '../components/Sliders.vue'
import axios from 'axios'
// import jwt_decode from 'jwt-decode'

export default {
  components: {
    Sliders,
  },
  data() {
    return {
      buttonOn : true,
      //얘는 특별관리
      forusermovies:[],
      //배열들
      topRatedmovies:[],
      latestmovies:[],
      horrormovies:[],
      SFmovies:[],
      Romancemovies:[],

      //제목들
      topRatedTitle: '평점이 높은 영화',
      latestTitle:'최근 개봉한 영화',
      SFTitle:'SF 영화',
      RomanceTitle:'로맨스 영화',
      horrorTitle:'호러 영화',

      //유저이름
      username:'',

      //스와이퍼 옵션
      swiperOptions: {
        slidesPerView: 5,
        spaceBetween: 100,
        loop: true,
        navigation: {
          nextEl: '#button-next-relacionados',
          prevEl: '#button-prev-relacionados'
        },
      }
    }
  },
  methods: {
    btnOn(){
      this.buttonOn = true
    },
    btnOff(){
      this.buttonOn = false
    },
    Recprev(){
      for (let i = 0; i < 5; i++){
        this.$refs.rec.$swiper.slidePrev()
      }
      this.$refs.rec.$swiper.slidePrev()
    },
    Recnext(){
      for (let i = 0; i < 5; i++){
        this.$refs.rec.$swiper.slideNext()
      }
      this.$refs.rec.$swiper.slideNext()
    },
  },
  
  async created() {
    if (localStorage.getItem('jwt')) {
      // token에서 유저 상세 정보 뺴옴
      // const token = localStorage.getItem('jwt')
      // console.log(jwt_decode(token))
      // const user = jwt_decode(token).user_id
      // this.username=jwt_decode(token).username
      //끝

      //평점 높은 영화  toprated
      await axios({
        url:'http://127.0.0.1:8000/api/v1/movies/',
        method:'GET',
      }).then((res)=>{
        console.log('평점 높은',res.data)
        const temp=[]
        res.data.toprate_movies.forEach(function(element){
          temp.push(element)
          // console.log(temp)
        })
        this.topRatedmovies=temp
      }).catch((err)=>{
        console.error(err)
      }),
      //끝

      // // 유저가 평점 잘 준 영화와 비슷한 영화, DB에 저장까지
      // axios({
      //   url:`http://127.0.0.1:8000/api/v1/accounts/${user}/recommend/`,
      //   method: 'GET',
      // }).then((res)=> {
      //   console.log(res.data)
      //   const movieId = res.data.fav_movie
      //   axios({
      //     url:`https://api.themoviedb.org/3/movie/${movieId}/similar?api_key=a03503b78be406a84d592df5327b4dbd&language=ko-KR&page=1`,
      //     method: 'GET'
      //   }).then((res)=>{
      //   const tmp = []
      //   console.log('resdata',res.data)
      //   res.data.results.forEach(function(element){
      //     tmp.push(element)
      //   })
      // this.forusermovies = tmp
      // axios({
      //   url: 'http://127.0.0.1:8000/movies/forUserMovieSave/ ',
      //   method: 'POST',
      //   data: {
      //     forusermovies:this.forusermovies,
      //   },
      //   headers: {
      //     Authorization: `JWT ${localStorage.getItem('jwt')}`
      //   },
      // }).then(()=>{
      //   console.log('취향저격','DB에 저장')
      // }).catch((err)=>{
      //   console.error(err)
      // })
      //   // console.log(this.forusermovies)
      // })
      // })
      // //끝

      //최근 개봉한 영화

      await axios({
        url:'http://127.0.0.1:8000/api/v1/movies/',
        method: 'GET',
        data: {
            page: 1,
            language:'ko-KR'
        }
      }).then((res)=>{
        console.log('최근 개봉',res.data)
        const tmp = []
        res.data.latest_movies.forEach(function(element){
          tmp.push(element)
        })  
        this.latestmovies=tmp
      })
      .catch((err)=>{
        console.log(err)
      })
      
      // this.latestmovies = tmp
      // axios({
      //     url: 'http://127.0.0.1:8000/api/v1/movies/',
      //     method: 'POST',
      //     data: {
      //       forusermovies:this.latestmovies,
      //     },
      //     headers: {
      //       Authorization: `JWT ${localStorage.getItem('jwt')}`
      //     },
      //   }).then(()=>{
      //     console.log('상영중 DB저장')
      //   }).catch((err)=>{
      //     console.error(err)
      //   })
      //끝

      // //SF
      // axios({
      //   url:'http://127.0.0.1:8000/api/v1/movies/',
      //   method: 'GET',
      //   data: {
      //       with_genres: 878,
      //       page: 1,
      //       language:'ko-KR'
      //   }
      // }).then(
      //   (res)=>{
      //   const tmp = []
      //   console.log('SF',res.data)
      //   res.data.results.forEach(
      //     function(element){
      //     const e = element
      //     e['movie_id'] = element['id']
      //     tmp.push(e)
      // })
      // this.SFmovies = tmp
      // axios({
      //     url: 'http://127.0.0.1:8000/api/v1/movies/',
      //     method: 'POST',
      //     data: {
      //       forusermovies:this.SFmovies,
      //     },
      //     headers: {
      //       Authorization: `JWT ${localStorage.getItem('jwt')}`
      //     },
      //   }).then(()=>{
      //     console.log('SF DB저장')
      //   }).catch((err)=>{
      //     console.error(err)
      //   })
      // })
      // //끝

      // //Romance
      // axios({
      //   url:'http://127.0.0.1:8000/api/v1/movies/',
      //   method: 'GET',
      //   data: {
      //       with_genres: 12,
      //       page: 1,
      //       language:'ko-KR'
      //   }
      // }).then((res)=>{
      //   const tmp = []
      //   console.log('로맨스',res.data)
      //   res.data.results.forEach(function(element){
      //     const e = element
      //     e['movie_id'] = element['id']
      //     tmp.push(e)
      // })
      // this.Romancemovies = tmp
      // axios({
      //     url: 'http://127.0.0.1:8000/api/v1/movies/',
      //     method: 'POST',
      //     data: {
      //       forusermovies:this.Romancemovies,
      //     },
      //     headers: {
      //       Authorization: `JWT ${localStorage.getItem('jwt')}`
      //     },
      //   }).then(()=>{
      //     console.log('로맨스 DB저장')
      //   }).catch((err)=>{
      //     console.error(err)
      //   })
      // })
      // //끝

      // //호러
      // axios({
      //   url:'http://127.0.0.1:8000/api/v1/movies/',
      //   method: 'GET',
      //   data: {
      //       with_genres: 27,
      //       page: 1,
      //       language:'ko-KR'
      //   }
      // }).then((res)=>{
      //   const tmp = []
      //   console.log('호러',res.data)
      //   res.data.results.forEach(function(element){
      //     const e = element
      //     e['movie_id'] = element['id']
      //     tmp.push(e)
      // })
      // this.horrormovies = tmp
      // axios({
      //     url: 'http://127.0.0.1:8000/api/v1/movies/',
      //     method: 'POST',
      //     data: {
      //       forusermovies:this.horrormovies,
      //     },
      //     headers: {
      //       Authorization: `JWT ${localStorage.getItem('jwt')}`
      //     },
      //   }).then(()=>{
      //     console.log('호러 DB저장')
      //   }).catch((err)=>{
      //     console.error(err)
      //   })
      // })
      // //끝
      
    } else {
      this.$router.push({ name: 'Login' })
    }
  }  
}
</script>

<style>
  
  
</style>