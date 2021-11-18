<template>
  <div>
    <img src="https://fontmeme.com/permalink/211118/6dfb6fa7875c07d34e39155bdbaf6638.png" alt="netflix-font" border="0">
    <br>
    <br>
    <br>
    <Sliders
      :movies="recommendmovies"
      :title="recommendTitle"
    />
    <Sliders
      :movies="nowmovies"
      :title="nowTitle"
    />
    <Sliders
      :movies="horrormovies"
      :title="horrorTitle"
    />
    <Sliders
      :movies="SFmovies"
      :title="SFTitle"
    />
    <Sliders
      :movies="Romancemovies"
      :title="RomanceTitle"
    />
    
    <div @mouseover = "btnOn" @mouseleave= "btnOff">
      <h4 v-if="forusermovies.length !== 0" class='text-left ml-3'>{{ username }}님의 취향저격 베스트 컨텐츠</h4>
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
    </div>
    
  </div>
  
</template>

<script>
// import RecommendMovieCard from '../components/RecommendMovieCard.vue'
import ForUserMovie from '../components/ForUserMovie.vue'
import Sliders from '../components/Sliders.vue'
import axios from 'axios'
import jwt_decode from 'jwt-decode'
export default {
  components: {
    // RecommendMovieCard,
    ForUserMovie,
    // 슬라이더
    Sliders,
  },
  data() {
    return {
      buttonOn : true,
      //얘는 특별관리
      forusermovies:[],
      //배열들
      recommendmovies:[],
      horrormovies:[],
      SFmovies:[],
      Romancemovies:[],
      similarmovies1:[],
      similarmovies2:[],
      nowmovies:[],
      //제목들
      recommendTitle:'평론가 호평을 받은 영화',
      horrorTitle:'호러 영화',
      SFTitle:'SF 영화',
      RomanceTitle:'로맨스 영화',
      nowTitle:'현재 상영중인 영화',
      //유저이름
      username:'',
      //스와이퍼옵션
      swiperOptions: {
        slidesPerView: 'auto',
        
        pagination: {
          el: '.swiper-pagination',
          dynamicBullets: true
        },
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
  
  created() {
    if (localStorage.getItem('jwt')) {
      // token에서 유저 상세 정보 뺴옴
      const token = localStorage.getItem('jwt')
      console.log(jwt_decode(token))
      const user = jwt_decode(token).user_id
      this.username=jwt_decode(token).username
      //끝

      //평점 높은 영화 : 차라리 toprated로 바꾸자.
      axios({
        url:'http://127.0.0.1:8000/movies/bestFive/',
        method:'GET',
      }).then((res)=>{
        
        const temp=[]
        res.data.forEach(function(element){
          temp.push(element)
        })
        this.recommendmovies=temp
      }).catch((err)=>{
        console.error(err)
      }),
      //끝

      // 유저가 평점 잘 준 영화와 비슷한 영화, DB에 저장까지
      axios({
        url:`http://127.0.0.1:8000/api/v1/accounts/${user}/recommend/`,
        method: 'GET',
      }).then((res)=> {
        console.log(res.data)
        const movieId = res.data.fav_movie
      axios({
        url:`https://api.themoviedb.org/3/movie/${movieId}/similar?api_key=4cdfc92c7474a643c4deb5c98ccbd73b&language=ko-KR&page=1`,
        method: 'GET'
      }).then((res)=>{
        const tmp = []
        console.log('resdata',res.data)
        res.data.results.forEach(function(element){
          tmp.push(element)
        })
        this.forusermovies = tmp
        axios({
          url: 'http://127.0.0.1:8000/movies/forUserMovieSave/ ',
          method: 'POST',
          data: {
            forusermovies:this.forusermovies,
          },
          headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`
          },
        }).then(()=>{
          console.log('취향저격','DB에 저장')
          })
          .catch((err)=>{
            console.error(err)
          })
        // console.log(this.forusermovies)
        })
      })
      //끝
      
      //호러
      axios({
        url:'https://api.themoviedb.org/3/discover/movie?api_key=4cdfc92c7474a643c4deb5c98ccbd73b&language=ko-KR&page=1&with_genres=27',
        method: 'GET',
        data: {
            with_genres: 27,
            page: 1,
            language:'ko-KR'
        }
      }).then((res)=>{
        const tmp = []
        console.log('호러',res.data)
        res.data.results.forEach(function(element){
          const e = element
          e['movie_id'] = element['id']
          tmp.push(e)
      })
      this.horrormovies = tmp
      axios({
          url: 'http://127.0.0.1:8000/movies/forUserMovieSave/ ',
          method: 'POST',
          data: {
            forusermovies:this.horrormovies,
          },
          headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`
          },
        }).then(()=>{
          console.log('호러 DB저장')
        }).catch((err)=>{
          console.error(err)
        })
      })
      //끝
      
      //SF
      axios({
        url:'https://api.themoviedb.org/3/discover/movie?api_key=4cdfc92c7474a643c4deb5c98ccbd73b&language=ko-KR&page=1&with_genres=878',
        method: 'GET',
        data: {
            with_genres: 878,
            page: 1,
            language:'ko-KR'
        }
      }).then(
        (res)=>{
        const tmp = []
        console.log('SF',res.data)
        res.data.results.forEach(
          function(element){
          const e = element
          e['movie_id'] = element['id']
          tmp.push(e)
      })
      this.SFmovies = tmp
      axios({
          url: 'http://127.0.0.1:8000/movies/forUserMovieSave/ ',
          method: 'POST',
          data: {
            forusermovies:this.SFmovies,
          },
          headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`
          },
        }).then(()=>{
          console.log('SF DB저장')
        }).catch((err)=>{
          console.error(err)
        })
      })
      //끝

      //Romance
      axios({
        url:'https://api.themoviedb.org/3/discover/movie?api_key=4cdfc92c7474a643c4deb5c98ccbd73b&language=ko-KR&page=1&with_genres=10749',
        method: 'GET',
        data: {
            with_genres: 12,
            page: 1,
            language:'ko-KR'
        }
      }).then((res)=>{
        const tmp = []
        console.log('로맨스',res.data)
        res.data.results.forEach(function(element){
          const e = element
          e['movie_id'] = element['id']
          tmp.push(e)
      })
      this.Romancemovies = tmp
      axios({
          url: 'http://127.0.0.1:8000/movies/forUserMovieSave/ ',
          method: 'POST',
          data: {
            forusermovies:this.Romancemovies,
          },
          headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`
          },
        }).then(()=>{
          console.log('로맨스 DB저장')
        }).catch((err)=>{
          console.error(err)
        })
      })
      //끝
      
      //상영중영화
      axios({
        url:'https://api.themoviedb.org/3/movie/now_playing?api_key=4cdfc92c7474a643c4deb5c98ccbd73b&language=ko-KR&page=1',
        method: 'GET',
        data: {
            page: 1,
            language:'ko-KR'
        }
      }).then((res)=>{
        const tmp = []
        console.log('상영중',res.data)
        res.data.results.forEach(function(element){
          const e = element
          e['movie_id'] = element['id']
          tmp.push(e)
      })
      this.nowmovies = tmp
      axios({
          url: 'http://127.0.0.1:8000/movies/forUserMovieSave/ ',
          method: 'POST',
          data: {
            forusermovies:this.nowmovies,
          },
          headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`
          },
        }).then(()=>{
          console.log('상영중 DB저장')
        }).catch((err)=>{
          console.error(err)
        })
      })
      
      //끝
    } else {
      this.$router.push({ name: 'Login' })
    }
  }  
}
</script>

<style>
  
  
</style>