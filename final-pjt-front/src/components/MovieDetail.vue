<template>
  <div class="mb-3 bgblack text-white" style=" width: auto; height:auto; border-radius: 10px; padding:10px">
    <div class="col-md-4 col-sm-6 col-xs-12" >
      <br>
      <img :src="getImage" alt="poster"
      style = "margin: 1px 130px; width: auto;">
    </div>
    <hr>
    <iframe 
    v-if="videoURI" 
    :src="videoURI" 
    frameborder="0" 
    style = "width: 700px; height: 350px; margin: 1px 25px;">
    </iframe>
    <div class="row no-gutters" style="display: inline-block;">
      <div class="card-body">
        <br>
        <h1 class="card-title" style="font-size: 37px; font-weight: bold;">{{ title }}</h1>
        <br>
        <h5>개봉일: {{ release_date }} / 평점: {{ vote_average }}</h5>
        <br>
        <p class="card-text">{{ overview }}</p>
        <br>
      </div> 
    </div>
    <hr>
    <form @submit="commentSubmit">
      <div class="form-group">
        <label for="star">별점</label>
        <br>
        <br>
        <star-rating
          id="star" 
          v-bind:increment="0.5"
          v-bind:max-rating="5"
          v-bind:show-rating="false"
          inactive-color="#000"
          active-color="#ff0"
          border-color="#ff0"
          v-bind:padding="8"
          v-bind:border-width="1"
          v-bind:star-size="30"
          @rating-selected="setRating">
        </star-rating>
        <br>
        <label for="comment">댓글을 입력하세요.</label>
        <textarea class="form-control" id="comment" rows="2" v-model="mycomment" @keypress.enter="commentSubmit"></textarea>
      </div>
      <br>
      <button class="btn btn-primary">제출</button>
    </form>
    <hr>
    <MovieComment 
      v-for="(comment, idx) in paginatedData"
      :key="idx"
      :comment="comment"
      :movie_pk="movie_pk"
      @onParentDeleteComment="onParentDeleteComment"
    />
    <br>
    <div class="btn-cover">
      <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
        이전
      </button>
      <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
      <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">
        다음
      </button>
    </div>
  </div>
  
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'
import StarRating from 'vue-star-rating'

import MovieComment from '../components/MovieComment.vue'
export default {
  components: {
    MovieComment,
    StarRating
  },
  data() {
    return {
      id:'',
      poster_path:'',
      title:'',
      vote_average:'',
      overview:'',
      release_date:'',
      mycomment:'',
      myrating:'',
      comments:[],
      videoURI:'',
      pageNum: 0,
      pageSize: 5,
    }
  },
  props: {
    movie_pk: Number,
  },
  methods: {
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    },
    commentSubmit(event) {
      event.preventDefault()
      if (this.mycomment.length !== 0) {
        const movie_pk = this.movie_pk
        // console.log("무비 피케이",movie_pk)
        const token = localStorage.getItem('jwt')
        // console.log(jwt_decode(token))
        const user = jwt_decode(token).user_id

        axios({
          url: `http://127.0.0.1:8000/api/v1/movies/${movie_pk}/review/`,
          method: 'POST',
          data: {
            user: user,
            content: this.mycomment,
            rank: this.myrating,
          },
          headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`
          },
        }).then(()=>{
          axios({
            url: `http://127.0.0.1:8000/api/v1/movies/${movie_pk}/review/`,
            method: 'GET',
          }).then((res)=>{
            console.log(res)
              const temp = []
              res.data.forEach((element)=>{
                temp.push(element)
              })
              this.comments = temp
          }).catch((err)=>{
            console.error(err)
          })
        }).catch((err)=>{
          console.error(err)
        })
        this.mycomment = ''
      } else {
        alert("댓글을 입력하세요.")
      }
    },
    onParentDeleteComment: function() {
      const movie_pk = this.movie_pk
      axios({
        url: `http://127.0.0.1:8000/api/v1/movies/${movie_pk}/review/`,
        method: 'GET',
      }).then((res)=>{
          const temp = []
          res.data.forEach((element)=>{
            temp.push(element)
          })
          this.comments = temp
      }).catch((err)=>{
        const temp = []
        this.comments = temp
        console.error(err)
      })
    },
    setRating(rank) {
      this.myrating = rank * 2
    }
  },
  computed: {
    getImage: function() {
      return 'http://image.tmdb.org/t/p/w500/'+this.poster_path
    },
    pageCount () {
      let listLeng = this.comments.length,
          listSize = this.pageSize,
          page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;
      
      return page;
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize,
            end = start + this.pageSize;
      return this.comments.slice(start, end);
    },
  },
  beforeUpdate(){
    const API_KEY = 'AIzaSyCPB-2OMju1VEyuzhwArA773ig4Ln0EgfE'
    const API_URL = 'https://www.googleapis.com/youtube/v3/search'
    const inputValue = `${this.title} trailer`
    console.log(inputValue)
    const params = {
      key: API_KEY,
      part: 'snippet',
      q: inputValue,
      type: 'video',
    }
    axios.get(API_URL, {
      params,
    })
    .then((res) => {
      console.log('이거',res.data.items)
      const videoId = res.data.items[0].id.videoId
      console.log('저거', videoId)
      this.videoURI = `https://www.youtube.com/embed/${videoId}?rel=0&mute=1&autoplay=1&controls=0&frameborder=0`
      console.log('비디오주소', this.videoURI)
    })
    .catch((err) => {
      console.log(err)
    })
  },
  created() {

    console.log(this.movie_pk)
    const movie_pk = this.movie_pk
    axios({
      url: `http://127.0.0.1:8000/api/v1/movies/${movie_pk}/`,
      method: 'GET',
    }).then((res)=>{
      console.log(res.data)  
      this.id = res.data.id
      this.poster_path = res.data.poster_path
      this.title = res.data.title
      this.vote_average = res.data.vote_average
      this.overview = res.data.overview
      this.release_date = res.data.release_date
    }).catch((err)=>{
      console.error(err)
    })
    axios({
      url: `http://127.0.0.1:8000/api/v1/movies/${movie_pk}/review/`,
      method: 'GET',
    }).then((res)=>{
        const temp = []
        res.data.forEach((element)=>{
          temp.push(element)
        })
        this.comments = temp
    }).catch((err)=>{
      console.error(err)
    })
    const token = localStorage.getItem('jwt')
    const username = jwt_decode(token).username
    this.currentName = username

  },     
}
  
</script>

<style scoped>

</style>
