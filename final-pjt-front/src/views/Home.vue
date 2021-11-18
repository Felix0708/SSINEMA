<template>
  <div>
    <img src="https://fontmeme.com/permalink/211118/6dfb6fa7875c07d34e39155bdbaf6638.png" alt="netflix-font" border="0">
    <br>
    <br>
    <br>
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

      //배열들
      nowmovies:[],
      horrormovies:[],
      SFmovies:[],
      Romancemovies:[],

      //제목들
      nowTitle:'현재 상영중인 영화',
      SFTitle:'SF 영화',
      RomanceTitle:'로맨스 영화',
      horrorTitle:'호러 영화',

      //유저이름
      username:'',
    }
  },
  methods: {
  },
  
  created() {
    if (localStorage.getItem('jwt')) {
      // token에서 유저 상세 정보 뺴옴
      // const token = localStorage.getItem('jwt')
      // console.log(jwt_decode(token))
      // const user = jwt_decode(token).user_id
      // this.username=jwt_decode(token).username
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
      
    } else {
      this.$router.push({ name: 'Login' })
    }
  }  
}
</script>

<style>
  
  
</style>