<template>
  <div class="container">
    <br>
    <br>
    <h1 style="color:white; margin-top:20px"><b>커뮤니티</b></h1>
    <br><br>
    <p>베스트 조회수</p>
    <br>
    <table class="table table-hover table-striped text-center" style="border: 2px solid">
      <thead>
        <tr style="color:black">
          <th>제목</th>
          <th>글쓴이</th>
          <th>댓글수</th>
          <th>조회수</th>
        </tr>
      </thead>
      <tbody>
        <Article 
          v-for="(article, idx) in bestData"
          :key="idx"
          :article="article"
        />
      </tbody> 
    </table>
    <br><br><br>
    <p>전체</p>
    <br>
    <form @submit="searchSome" class="form-inline ml-auto mr-2 d-flex mb-1">
      <select v-model="selected" name="kind" class='form-select bg-light' style="margin: 0 2px; width: auto;">
        <option value="title" selected>제목</option>
        <option value="person">글쓴이</option>
      </select>
      <input class="form-control mr-sm-2 me-1" v-model="search" type="text" placeholder="Search" aria-label="Search">
      <button class="btn btn-success my-2 my-sm-0" type="submit">Search</button>
    </form>
    <table class="table table-hover table-striped text-center" style="border: 2px solid">
      <thead>
        <tr style="color:black">
          <th>제목</th>
          <th>글쓴이</th>
          <th>댓글수</th>
          <th>조회수</th>
        </tr>
      </thead>
      <tbody>
        <Article 
          v-for="(article, idx) in paginatedData"
          :key="idx"
          :article="article"
        />
      </tbody> 
    </table>
    <div class="d-flex justify-content-center">
      <button style="margin:0 10px 0 10px" class="btn btn-primary ml-4" @click="sendToCreateArticle">글쓰기</button>
      <form>
        <button class="btn btn-primary ml-auto mr-4" onClick="history.go(0)">Refresh</button>
      </form>
    </div>
    <p></p>
    <div class="btn-cover" style="color:white;">
      <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
        이전
      </button>
      <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
      <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">
        다음
      </button>
    </div>
    <p></p>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import Article from '../components/Article.vue'

export default {
  name: 'Community',
  components: {
    Article,
  },
  data() {
    return {
      articles: [],
      pageNum: 0,
      pageSize: 10,
      selected: '',
      search: '',
    }
  },
  methods: {
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    sendToCreateArticle() {
      this.$router.push({name: 'CreateArticle'})
    },
    searchSome(event) {
      event.preventDefault()
      const keyword = this.search
      const temp = []
      if (this.selected === 'title') {
        this.articles.forEach((element)=>{
          // console.log(element.title)
          const title = element.title
          if (title.indexOf(keyword) !== -1) {
            temp.push(element)   
          }
          this.articles = temp  
        })
      } else {
        this.articles.forEach((element)=>{
          // console.log(element.title)
          const userid = element.user
          axios({
            url: `https://ssinema.click/api/v1/accounts/${userid}/`,
            method: 'GET',
            headers: {
              Authorization: `JWT ${localStorage.getItem('jwt')}`
            },
          }).then((res)=>{
            // console.log(res)
            const username = res.data.username
            if (username.indexOf(keyword) !== -1) {
              temp.push(element)       
            }
            this.articles = temp
          }).catch((err)=>{
            console.error(err)
          }) 
        })
      }
      this.selected = ''
      this.search = ''
    }
  },
  computed: {
    pageCount () {
      let listLeng = this.articles.length,
          listSize = this.pageSize,
          page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;
      
      return page;
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize,
            end = start + this.pageSize;
      const sortedArticles = _.sortBy(this.articles, 'id').reverse()
      return sortedArticles.slice(start, end);
    },
    bestData () {
      // console.log(this.articles)
      let bestArticles = []
      this.articles.forEach((element)=>{
        // console.log(element)
        if (bestArticles.length < 3) {
          bestArticles.push(element)
          // console.log(bestArticles)
        } else {
          bestArticles.sort(function(a, b) {
            // console.log(b.view_count)
            // console.log(a)
            return b.view_count - a.view_count
          })
          if (bestArticles[2].view_count < element.view_count) {
            bestArticles.pop()
            bestArticles.push(element)
          }
        }
      })
      return bestArticles
    }
  },
  created() {
    if (localStorage.getItem('jwt')) {
      const config = this.setToken()
      axios.get('https://ssinema.click/api/v1/articles/', config)
        .then((res)=> {
          const temp = []
          res.data.forEach((element)=>{
            temp.push(element)
          })
          this.articles = temp
          // console.log(this.articles)
      }).catch((err)=>{
        console.error(err)
      })
    } else {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style>
  p {
    font-size: 20px;
    font-weight: bold;
    color: white;
    margin-bottom: 0px;
  }
  .table {
    color: lightgray;
    
  }
  thead {
    background-color: lightgray;
  }
  tbody {
    cursor: pointer;
  }

  select {
    text-align: center;
  }

  .btn-cover {
    margin-top: 1.5rem;
    text-align: center;
  }
  .btn-cover .page-btn {
    width: 5rem;
    height: 2rem;
    letter-spacing: 0.5px;
  }
  .btn-cover .page-count {
    padding: 0 1rem;
  }
</style>