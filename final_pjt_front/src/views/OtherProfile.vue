<template>
  <div class="container profilediv">
    <br>
    <br>
    <h2 style="color:white">{{ this.articlesUser }}의 프로필</h2>
    <br>
    <br>
    <div>
      <div id="follow-count" style="color: white;">팔로잉 수 &nbsp; : &nbsp; {{followings}} &nbsp; | &nbsp; 팔로워 수 &nbsp; : &nbsp; {{followers}}</div>
    </div>
    <br>
    <div>
      <form id="follow-form" @submit="followed">
        <button v-if="this.followerList.includes(this.userId)" class="btn btn-link p-0 m-0" style="box-shadow: none;">
          <i id="follow-btn" class="fas fa-user-minus" style="color:crimson;">
            <span id="follow-text" class="ms-1">Unfollow</span>
          </i>
        </button>
        <button v-else class="btn btn-link p-0 m-0" style="box-shadow: none;">
          <i id="follow-btn" class="fas fa-user-plus" style="color:primary;">
            <span id="follow-text" class="ms-1">Follow</span>
          </i>
        </button>
      </form>
    </div>
    <br>
    <hr style="background-color:white">
    <br>
    <h2 class="text-left" style="color:white">{{this.articlesUser}}가 찜한 영화</h2>
    <br>
    <div @mouseover = "btnOn" @mouseleave= "btnOff">
      <ProfileSliders
      v-show="articlesUserMovies"
      :movies="articlesUserMovies"
      />
    </div>
    <br>
    <hr style="background-color:white">
    <br>
    <h2 class="text-left" style="color:white">{{ this.articlesUser }}님이 작성하신 글</h2>
    <br>
    <span v-for= "(article,idx) in paginatedArticles" :key = "idx">
      <!-- <li class="text-left" style="list-style:none; color:white;" @click="getArticleDetail(idx)"> -->
        <button class="mx-5 my-2" @click="getArticleDetail(idx)" style="list-style:none; color:gold;">
          {{article.title}}
        </button>
        <br>
        <br>
        <b-modal
        :data-key="idx"
        ref="detail" 
        size="lg" 
        class="bg-black" 
        :header-bg-variant="black"
        :footer-bg-variant="black"
        hide-footer hide-header>
          <ArticleDetail
            :article_pk ="article.id"
            :writer ="articlesUser"
          />
      </b-modal>
      <!-- </li> -->
    </span>
    <div class="btn-cover">
      <button style="color:white" :disabled="pageNum === 0" @click="prevPage" class="page-btn">
        이전
      </button>
      <span style="color:white" class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
      <button style="color:white" :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">
        다음
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'
import ArticleDetail from '../components/ArticleDetail'
import ProfileSliders from '../components/ProfileSliders'

export default {
  name: 'OtherProfile',
  components:{
    ArticleDetail,
    ProfileSliders,
  },
  // props: {
  //   articleWriter: {
  //     type: String,
  //   },
  // },
  data: function () {
    return {
      buttonOn : true,
      username: '',
      articles: [],
      articlesUser: '',
      articlesUserId: '',
      articlesUserMovies: [],
      followings: 0,
      followers: 0,
      followerList: [],
      black: 'black',
      pageNum: 0,
      pageSize: 3,
      pageCommentNum: 0,
      pageCommentSize: 3,

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
  methods:{
    followed (event) {
      console.log(this.$route.query.articleWriter)
      event.preventDefault()
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/api/v1/accounts/follow/${this.$route.query.articleWriter}/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
        .then(response => {
          const followBtn = document.querySelector('#follow-btn')
          const followText = document.querySelector('#follow-text')
          const isFollowed = response.data.followed

          if (isFollowed === true) {
            followBtn.classList.add('fa-user-minus')
            followBtn.classList.remove('fa-user-plus')
            followBtn.style = 'color:crimson;'
            followText.innerText = 'Unfollow'
          } else {
            followBtn.classList.add('fa-user-plus')
            followBtn.classList.remove('fa-user-minus')
            followBtn.style = 'color:primary;'
            followText.innerText = 'Follow'
          }
        }).then(() => {
            axios({
              url:`http://127.0.0.1:8000/api/v1/accounts/${this.articlesUser}/`,
              method: 'GET',
              headers: {
                Authorization: `JWT ${localStorage.getItem('jwt')}`
              },
            }).then((res)=>{
              // console.log(res.data)
              // console.log(typeof(res.data.followings))
              this.followings = res.data.followings
              this.followers = res.data.followers
              this.followerList = res.data.follower_list
              // console.log(this.followerList)
            }).catch((err)=>{
              console.log(err)
            })
        }).catch((err) => {
          console.log(err)
        })
        .catch(error => {
          console.log(error)
        })
    },

    getArticleDetail(idx) {
      const detail = this.$refs['detail'].find(
        el => el.$attrs['data-key'] === idx
      );
      detail.show()
    },
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    },

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
  computed: {
    pageCount () {
      let listLeng = this.articles.length,
          listSize = this.pageSize,
          page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;
      
      return page;
    },
    paginatedArticles () {
      const start = this.pageNum * this.pageSize,
            end = start + this.pageSize;

      return this.articles.slice(start, end);
    },
  },
  update () {

  },
  created() {
    // if (localStorage.getItem('jwt')) {
    const token = localStorage.getItem('jwt')
    const decoded = jwt_decode(token)
    // console.log(decoded)
    this.username = decoded['username']
    // console.log(this.username)
    this.userId = decoded['user_id']
    // console.log(this.userId)
    // console.log(this.$route.query.articleWriter)
    this.articlesUser = this.$route.query.articleWriter
    // console.log(this.articlesUser)
    this.articlesUserId = this.$route.query.articleWriterId
    // console.log(this.articlesUserId)

    // 유저 articles
    axios({
      url: `http://127.0.0.1:8000/api/v1/accounts/${this.articlesUserId}/myArticle/`,
      method: 'GET',
      headers: {
        Authorization: `JWT ${localStorage.getItem('jwt')}`
      },
    }).then((res)=>{
      // console.log(res.data)
      this.articles = res.data
    }).catch((err)=>{
      console.log(err)
    })

    //유저 프로필 정보
    axios({
      url:`http://127.0.0.1:8000/api/v1/accounts/${this.articlesUser}/`,
      method: 'GET',
      headers: {
        Authorization: `JWT ${localStorage.getItem('jwt')}`
      },
    }).then((res)=>{
      // console.log(res.data)
      // console.log(typeof(res.data.followings))
      this.followings = res.data.followings
      this.followers = res.data.followers
      this.followerList = res.data.follower_list
      // console.log(this.followerList)
    }).catch((err)=>{
      console.log(err)
    })

    //유저 movies
    axios({
      url:`http://127.0.0.1:8000/api/v1/accounts/${this.articlesUserId}/myMovie/`,
      method: 'GET',
      headers: {
        Authorization: `JWT ${localStorage.getItem('jwt')}`
      },
    }).then((res)=>{
      // console.log('찜한 영화',res.data)
      const tmp = []
      res.data.serializer.forEach(function(element){
        tmp.push(element)
      })
      this.articlesUserMovies=tmp
      // console.log(this.myMovies)
    }).catch((err)=>{
      console.error(err)
    })

    // } else {
    //   this.$router.push({ name: 'Login' })
    // }
  }
}
</script>

<style scoped>

  .profilediv {
    margin-bottom: 500px;
  }
</style>