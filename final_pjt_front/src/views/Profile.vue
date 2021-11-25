<template>
  <div class="container profilediv">
    <br>
    <br>
    <h2 style="color:white">{{ username }}의 프로필</h2>
    <br>
    <br>
    <div>
      <div id="follow-count" style="color: white;">팔로잉 수 &nbsp; : &nbsp; {{followings}} &nbsp; | &nbsp; 팔로워 수 &nbsp; : &nbsp; {{followers}}</div>
    </div>
    <br>
    <hr style="background-color:white">
    <br>
    <h2 class="text-left" style="color:white">내가 찜한 영화</h2>
    <br>
    <div @mouseover = "btnOn" @mouseleave= "btnOff">
      <ProfileSliders
      v-show="myMovies"
      :movies="myMovies"
      />
    </div>
    <br>
    <hr style="background-color:white">
    <br>
    <h2 class="text-left" style="color:white">내가 작성한 글</h2>
    <br>
    <span v-for= "(article,idx) in paginatedArticles" :key = "idx">
      <!-- <li class="text-left" style="list-style:none; color:white;" @click="getArticleDetail(idx)"> -->
        <button class="mx-5 my-2" @click="getArticleDetail(idx)" style="list-style:none; color: gold;">
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
            :writer ="username"
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
    <br>
    <hr style="background-color:white">
    <br>
    <h2 class="text-left row" >
      <div class="col-5" style="color:white">내가 작성한 댓글</div>
      <div class="col-7 text-right" style="color:white"> 원문</div>
    </h2>
    <br>
    <span v-for= "(comment,idx) in paginatedComments" :key = "idx">
      <li class="text-left row" style="list-style:none">
        <div class="col-3" style="color: gold; margin-left: -10px;">
          댓글: 
        </div>
        <div class="col-2" style="color: gold; margin-left: -30px">
          {{comment.content}}
        </div>
        <div class="col-3 text-right" style="color:gold; margin-left: 120px">
          {{comment.article.user.username}}님의
        </div>
        <div class="col-1 text-right" style="color:gold; margin-left: -80px">
          제목:
        </div>
        <div class="col-2 text-right" style="color:gold; margin-left: -40px">
          {{comment.article.title}}
        </div>
      </li>
    </span>
    <br>
    <div class="btn-cover">
      <button style="color:white" :disabled="pageCommentNum === 0" @click="prevCommentPage" class="page-btn">
        이전
      </button>
      <span style="color:white" class="page-count">{{ pageCommentNum + 1 }} / {{ pageCommentCount }} 페이지</span>
      <button style="color:white" :disabled="pageCommentNum >= pageCommentCount - 1" @click="nextCommentPage" class="page-btn">
        다음
      </button>
    </div>
    <br>
    <hr style="background-color:white">
    <br>
    <br>
    <div>
      <button class="deleteAccount btn btn-danger" @click="deleteAccount">회원탈퇴</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'
import ArticleDetail from '../components/ArticleDetail'
import ProfileSliders from '../components/ProfileSliders'

export default {
  name: 'Profile',
  components:{
    ArticleDetail,
    ProfileSliders,
  },
  props: {

  },
  data: function () {
    
    return {
      // login: false,
      buttonOn : true,
      userId: '',
      username: '',
      articles: [],
      comments: [],
      article_set: [],
      articleName: '',
      myMovies: [],
      followings: 0,
      followers: 0,
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
    // logout: function () {
    //   localStorage.removeItem('jwt')
    //   this.login = false
    //   this.$router.push({ name: 'MainPage' })
    // },
    deleteAccount () {
      if (confirm('정말 탈퇴하시겠습니까?') == true) {
        
        axios({
          method: 'delete',
          url: `https://ssinema.click/api/v1/accounts/${this.username}/`,
          headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`
          },
        })
          .then(() => {
            // console.log(res)
            // this.logout()
            localStorage.removeItem('jwt')
            // history.go(0)
            location.href="/"
          })
          .catch(err => {
            console.log(err)
          })
      }else{
        return false;
      }
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
    nextCommentPage () {
      this.pageCommentNum += 1;
    },
    prevCommentPage () {
      this.pageCommentNum -= 1;
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
    pageCommentCount () {
      let listLeng = this.comments.length,
          listSize = this.pageCommentSize,
          page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;

      return page;
    },
    paginatedComments () {
      const start = this.pageCommentNum * this.pageCommentSize,
            end = start + this.pageCommentSize;
      return this.comments.slice(start, end);
    },
  },
  created() {
    const token = localStorage.getItem('jwt')
    const decoded = jwt_decode(token)
    // console.log(decoded)
    this.username = decoded['username']
    this.userId = decoded['user_id']
    // console.log(userId)

    // 유저 articles
    axios({
      url: 'https://ssinema.click/api/v1/accounts/' + this.userId+ '/myArticle/',
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
    
    // 유저 comments
    axios({
      url: 'https://ssinema.click/api/v1/accounts/' + this.userId + '/myComment/',
      method: 'GET',
      headers: {
        Authorization: `JWT ${localStorage.getItem('jwt')}`
      },
    }).then((res)=>{
      // console.log(res.data)
      this.comments = res.data
    }).catch((err)=>{
      console.log(err)
    })

    //유저 movies
    axios({
      url:`https://ssinema.click/api/v1/accounts/${this.userId}/myMovie/`,
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
      this.myMovies=tmp
      // console.log(this.myMovies)
    }).catch((err)=>{
      console.error(err)
    })

    //유저 프로필
    axios({
      url:`https://ssinema.click/api/v1/accounts/${this.username}/`,
      method: 'GET',
      headers: {
        Authorization: `JWT ${localStorage.getItem('jwt')}`
      },
    }).then((res)=>{
      // console.log(res.data)
      // console.log(typeof(res.data.followings))
      this.followings = res.data.followings
      this.followers = res.data.followers
    }).catch((err)=>{
      console.log(err)
    })
  }
}
</script>

<style scoped>

  .profilediv {
    margin-bottom: 500px;
  }
</style>