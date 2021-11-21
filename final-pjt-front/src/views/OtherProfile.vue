<template>
  <div class="container profilediv" style="height: auto">
    <br>
    <h2 style="color:white">{{ this.articlesUser }}의 프로필</h2>
    <br>
    <div>
      <div id="follow-count" style="color: white;">팔로잉 수 &nbsp; : &nbsp; {{followings}} &nbsp; | &nbsp; 팔로워 수 &nbsp; : &nbsp; {{followers}}</div>
    </div>
    <br>
    <div>
      <form id="follow-form" @submit="followed">
        <button   class="btn btn-link p-0 m-0" style="box-shadow: none;">
          <i id="follow-btn" class="fas fa-user-minus" style="color:crimson;">
            <span id="follow-text" class="ms-1">Unfollow</span>
          </i>
        </button>
        <button class="btn btn-link p-0 m-0" style="box-shadow: none;">
          <i id="follow-btn" class="fas fa-user-plus" style="color:primary;">
            <span id="follow-text" class="ms-1">Follow</span>
          </i>
        </button>
      </form>
    </div>
    <hr style="background-color:white">
    <h2 class="text-left" style="color:white">{{ this.articlesUser }}님이 작성하신 글</h2>
    <span v-for= "(article,idx) in paginatedArticles" :key = "idx">
      <!-- <li class="text-left" style="list-style:none; color:white;" @click="getArticleDetail(idx)"> -->
        <button class="mt-3" @click="getArticleDetail(idx)" style="list-style:none; color:white;">
          {{article.title}}
        </button>
        <br>
        <b-modal 
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

export default {
  name: 'OtherProfile',
  components:{
    ArticleDetail,
  },
  // props: {
  //   articleWriter: {
  //     type: String,
  //   },
  // },
  data: function () {
    return {
      username: '',
      articles: [],
      articlesUser: '',
      articlesUserId: '',
      followings: 0,
      followers: 0,
      black: 'black',
      pageNum: 0,
      pageSize: 3,
      pageCommentNum: 0,
      pageCommentSize: 3,
    }
  },
  methods:{
    followed (event) {
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
          const isFollowed = response.data.isFollowed

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
        })
        .catch(error => {
          console.log(error)
        })
    },

    getArticleDetail(idx) {
      this.$refs.detail[idx].show()
    },
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
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
    // console.log(this.$route.query.articleWriter)
    this.articlesUser = this.$route.query.articleWriter
    // console.log(this.articlesUser)
    this.articlesUserId = this.$route.query.articleWriterId
    console.log(this.articlesUserId)

    // 유저 articles
    axios({
      url: `http://127.0.0.1:8000/api/v1/accounts/${this.articlesUserId}/myArticle/`,
      method: 'GET',
      headers: {
        Authorization: `JWT ${localStorage.getItem('jwt')}`
      },
    }).then((res)=>{
      console.log(res.data)
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
    }).catch((err)=>{
      console.log(err)
    })

    const token = localStorage.getItem('jwt')
    const decoded = jwt_decode(token)
    // console.log(decoded)
    this.username = decoded['username']
    // console.log(this.username)
    // this.userId = decoded['user_id']
    // console.log(this.userId)
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