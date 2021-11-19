<template>
  <div class="container">
    <h1><b>커뮤니티</b></h1>
    <br><br>
    <h3><b>베스트 조회수</b></h3>
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
    <h3><b>전체</b></h3>
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
          v-for="(article, idx) in paginatedData"
          :key="idx"
          :article="article"
        />
      </tbody> 
    </table>
    <div class="row">
      
      <button class="btn btn-primary ml-4" @click="sendToCreateArticle">글쓰기</button>
      <form @submit="searchSome" class="form-inline ml-auto mr-2">
        <select v-model="selected" name="kind" class='mx-1 custom-select'>
          <option value="title">제목</option>
          <option value="person">글쓴이</option>
        </select>
        <input class="form-control mr-sm-2" v-model="search" type="text" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </form>
      <form>
        <button class="btn btn-primary ml-auto mr-4" onClick="history.go(0)">Refresh</button>
      </form>
    </div>
    <p></p>
    <div class="btn-cover">
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
            url: `http://127.0.0.1:8000/api/v1/accounts/${userid}/`,
            method: 'GET',
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
        // console.log(element.read)
        if (bestArticles.length < 3) {
          bestArticles.push(element)
        } else {
          bestArticles.sort(function(a, b) {
            return b.read - a.read
          })
          if (bestArticles[2].read < element.read) {
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
      axios.get('http://127.0.0.1:8000/api/v1/articles/', config)
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
  .table {
    color: lightgray;
    
  }
  thead {
    background-color: lightgray;
  }
  tbody {
    cursor: pointer;
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