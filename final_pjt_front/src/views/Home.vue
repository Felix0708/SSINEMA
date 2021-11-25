<template>
  <div class="bg-home" @mouseover = "btnOn" @mouseleave= "btnOff">
    <br>
    <br>
    <br>
    <img src="https://fontmeme.com/permalink/211118/6dfb6fa7875c07d34e39155bdbaf6638.png" alt="netflix-font" border="0">
    <br>
    <br>
    <!-- <iframe 
    v-if="videoURI" 
    :src="videoURI" 
    frameborder="0"
    style = "width: 99%; height: 990px; margin: auto;">
    </iframe> -->
    <br>
    <br>
    <Sliders
      v-show="foryoumovies"
      :movies="foryoumovies"
      :title="foryouTitle"
    />
    <br>
    <Sliders
      :movies="Todaymovies"
      :title="TodayTitle"
    />
    <br>
    <Sliders
      :movies="topRatedmovies"
      :title="topRatedTitle"
    />
    <br>
    <Sliders
      :movies="latestmovies"
      :title="latestTitle"
    />
    <br>
    <Sliders
      :movies="mostpopmovies"
      :title="mostpopTitle"
    />
  </div>
</template>

<script>
import Sliders from '../components/Sliders.vue'
import axios from 'axios'
import jwt_decode from 'jwt-decode'

export default {
  name: 'home',
  components: {
    Sliders,
  },
  data() {
    return {
      buttonOn : true,
      //배열들
      topRatedmovies:[],
      latestmovies:[],
      Todaymovies:[],
      mostpopmovies:[],
      foryoumovies:[],

      //제목들
      topRatedTitle: '평점이 높은 영화',
      latestTitle:'최근 개봉한 영화 (혹은 개봉 할 영화)',
      TodayTitle:'오늘 이런 영화는 어떠세요?',
      mostpopTitle:'스테디 셀러 영화',
      foryouTitle:'',

      //유저이름
      username:'',
      userId: '',

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

  // async created() {
  created() {
  if (localStorage.getItem('jwt')) {
    // token에서 유저 상세 정보 뺴옴
    const token = localStorage.getItem('jwt')
    // console.log(jwt_decode(token))
    // const user = jwt_decode(token).user_id
    this.username=jwt_decode(token).username
    this.foryouTitle = `${this.username}을 위한 취향저격 베스트 컨텐츠`
    //끝

    //foruser
    // await axios({
    axios({
      url:'https://ssinema.click/api/v1/movies/category/foryou/',
      method: 'GET',
    }).then((res)=>{
      // console.log('취향 저격',res.data)
      const tmp = []
      res.data.foruser_movies.forEach(function(element){
        tmp.push(element)
      })
      this.foryoumovies=tmp
    }).catch((err)=>{
      console.error(err)
    })
    //끝

    //Today
    // await axios({
    axios({
      url:'https://ssinema.click/api/v1/movies/category/weather/',
      method: 'GET',
    }).then((res)=>{
      // console.log('오늘의',res.data)
      const tmp = []
      res.data.weather_movies.forEach(function(element){
        tmp.push(element)
      })
      this.Todaymovies=tmp
    }).catch((err)=>{
      console.error(err)
    })
    //끝

    //최근 개봉한 영화
    // await axios({
    axios({
      url:'https://ssinema.click/api/v1/movies/category/latest/',
      method: 'GET',
    }).then((res)=>{
      // console.log('최근 개봉',res.data)
      const tmp = []
      res.data.latest_movies.forEach(function(element){
        tmp.push(element)
      })  
      this.latestmovies=tmp
    })
    .catch((err)=>{
      console.log(err)
    }),

    //평점 높은 영화  toprated
    // await axios({
    axios({
      url:'https://ssinema.click/api/v1/movies/category/toprate/',
      method:'GET',
    }).then((res)=>{
      // console.log('평점 높은',res.data)
      const tmp=[]
      res.data.toprate_movies.forEach(function(element){
        tmp.push(element)
        // console.log(temp)
      })
      this.topRatedmovies=tmp
    }).catch((err)=>{
      console.error(err)
    }),
    //끝

    //mostpop
    // await axios({
    axios({
      url:'https://ssinema.click/api/v1/movies/category/mostpop/',
      method: 'GET',
    }).then((res)=>{
      // console.log('스테디 셀러',res.data)
      const tmp = []
      res.data.mostpop_movies.forEach(function(element){
        tmp.push(element)
      })
      this.mostpopmovies=tmp
    }).catch((err)=>{
      console.error(err)
    })
    //끝


    // const token = localStorage.getItem('jwt')
    // this.userId = jwt_decode(token).user_id
    // axios({
    //     url:`http://127.0.0.1:8000/api/v1/accounts/${this.userId}/myMovie/`,
    //     method: 'GET',
    // }).then((res) => {
    //   console.log(res.data.title_list)
    //   const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
    //   const API_URL = 'https://www.googleapis.com/youtube/v3/search'
    //   const titleList = res.data.title_list
    //   const inputValue = titleList[Math.floor(Math.random()*titleList.length)] + ' trailer'
    //   console.log(inputValue)
    //   const params = {
    //     key: API_KEY,
    //     part: 'snippet',
    //     q: inputValue,
    //     type: 'video',
    //   }
    //   axios.get(API_URL, {
    //     params,
    //   })
    //   .then((res) => {
    //     console.log('이거',res.data.items)
    //     const videoId = res.data.items[0].id.videoId
    //     console.log('저거', videoId)
    //     this.videoURI = `https://www.youtube.com/embed/${videoId}?rel=0&mute=1&autoplay=1&controls=0&frameborder=0&cc_lang_pref=ko&modestbranding=1&loop=1`
    //     console.log('비디오주소', this.videoURI)
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
    // }).catch((err) => {
    //     console.log(err)
    //   })
    } else {
      this.$router.push({ name: 'Login' })
    }
  }  
}
</script>

<style>
  .bg-home{
    background-image: url('../assets/slider-bg2.jpg');
    background-repeat: repeat;
  }
</style>