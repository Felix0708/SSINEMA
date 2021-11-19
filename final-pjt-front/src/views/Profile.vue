<template>
  <div class="container profilediv" style="height: 800px">
    <br>
    <hr style="background-color:white">
    <h2 class="text-left" style="color:gold">내가 작성한 글</h2>
    <span v-for= "(article,idx) in paginatedArticles" :key = "idx">
      <li class="text-left" style="list-style:none" @click="getArticleDetail(idx)">
        {{article.title}}
        <b-modal 
      ref="detail" 
      size="lg" 
      class="bg-black" 
      :header-bg-variant="black"
      :body-bg-variant="black"
      :footer-bg-variant="black"
      hide-footer hide-header>
        <ArticleDetail
          :article_pk ="article.id"
          :writer ="username"
        />
      </b-modal>
      </li>
    </span>
    <div class="btn-cover">
      <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
        이전
      </button>
      <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
      <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">
        다음
      </button>
    </div>
    <br><br>
    <hr style="background-color:white">
    <h2 class="text-left row" >
      <div class="col-5" style="color:gold">내가 작성한 댓글</div>
      <div class="col-7 text-right" style="color:gold"> 원문</div>
    </h2>
    <span v-for= "(comment,idx) in paginatedComments" :key = "idx">
      <li class="text-left row" style="list-style:none">
        <div class="col-8">{{comment.content}}</div>
        <div class="col-4 text-right">{{comment.article}}</div>
      </li>
    </span>
    <div class="btn-cover">
      <button :disabled="pageCommentNum === 0" @click="prevCommentPage" class="page-btn">
        이전
      </button>
      <span class="page-count">{{ pageCommentNum + 1 }} / {{ pageCommentCount }} 페이지</span>
      <button :disabled="pageCommentNum >= pageCommentCount - 1" @click="nextCommentPage" class="page-btn">
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
  components:{
    ArticleDetail
  },
  data: function () {
    
    return {
      username: '',
      articles: [],
      comments: [],
      black: 'black',
      pageNum: 0,
      pageSize: 3,
      pageCommentNum: 0,
      pageCommentSize: 3,
    }
  },
  methods:{
    getArticleDetail(idx) {
      this.$refs.detail[idx].show()
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
    console.log(decoded)
    this.username = decoded['username']
    const userId = decoded['user_id']
    // console.log(userId)

    // 유저 articles
    axios({
      url: 'http://127.0.0.1:8000/api/v1/articles/' + String(userId) + '/profile_articles/',
      method: 'GET'
    }).then((res)=>{
      console.log(res)
      this.articles = res.data
    }).catch((err)=>{
      console.log(err)
    })
    
    // 유저 comments
    axios({
      url: 'http://127.0.0.1:8000/api/v1/articles/' + String(userId) + '/profile_comments/',
      method: 'GET'
    }).then((res)=>{
      console.log(res)
      this.comments = res.data
    }).catch((err)=>{
      console.log(err)
    })
  }
}
</script>

<style scoped>
  .rank-img {
    
    width: auto; height: auto;
    max-width: 500px;
    max-height: 500px;
    border-radius: 50%;
  }
  .profilediv {
    margin-bottom: 500px;
  }
</style>