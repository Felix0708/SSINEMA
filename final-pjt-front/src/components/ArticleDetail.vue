<template>
  <div class="container articledetail" style="width: auto;">
    <div class="card" style="background-color: black">
      <div class="card-header">
        <div class='d-flex'>
          <p class="mt-2 me-5 ml-4"><b>{{ writer }}</b>님의 글</p>
          <p class="mt-2 ms-5 ml-auto mr-4" style="display: inline;">{{getDate}} {{ getTime }}</p>
        </div>
        <p class="card-title mt-2" style="text-align: left;"><b>{{ title }}</b></p>
      </div>
      <hr style="margin: 0;">
      <div class="card-body">
        <br>
        <p class="card-text" style="text-align: left; margin: 0;">{{ content }}</p>
        <br>
      </div>
      <div class="card-footer text-muted">
        <div v-if="writer == currentName">
          <button class="btn btn-success me-3" @click="updateArticle">Update</button>
          <button class="btn btn-danger ml-4" style="display: inline-block;" @click="deleteArticle">Delete</button>
        </div>
      </div>
    </div>
    <hr>
    <form @submit="commentSubmit">
      <div class="form-group" style="margin-bottom:10px;">
        <label style="margin-bottom:5px;" for="comment">댓글을 입력하세요.</label>
        <textarea class="form-control" style="background-color: black color:white" id="comment" rows="2" v-model="mycomment" @keypress.enter="commentSubmit"></textarea>
      </div>
      <button class="btn btn-primary">Submit</button>
    </form>
    <hr>
    <h3><b>Comments</b></h3>
    <Comment 
      v-for="(comment, idx) in paginatedData"
      :key="idx"
      :comment="comment"
      :article_pk="article_pk"
      @onParentDeleteComment="onParentDeleteComment"
    />
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
import Comment from '../components/Comment.vue'
export default {
  name: 'ArticleDetail',
  components: {
    Comment
  },
  data() {
    return {
      title: '',
      content: '',
      created_at: '',
      updated_at: '',
      mycomment: '',
      comments: [],
      currentName: '',
      pageNum: 0,
      pageSize: 3,
    }
  },
  props: {
    article_pk: {
      type: Number,
    },
    writer: {
      type: String,
    },
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
        // console.log(this.article_pk)
        const article_pk = this.article_pk
        const token = localStorage.getItem('jwt')
        // console.log(jwt_decode(token))
        const user = jwt_decode(token).user_id
        // console.log(user)
        axios({
          url: `http://127.0.0.1:8000/api/v1/articles/${article_pk}/comments/`,
          method: 'POST',
          data: {
            user: user,
            content: this.mycomment
          },
          headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`
          },
        }).then((res)=>{
          console.log(res.data)
          axios({
            url: `http://127.0.0.1:8000/api/v1/articles/${article_pk}/comments/`,
            method: 'GET',
            headers: {
              Authorization: `JWT ${localStorage.getItem('jwt')}`
            },
          }).then((res)=>{
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
      const article_pk = this.article_pk
      axios({
        url: `http://127.0.0.1:8000/api/v1/articles/${article_pk}/comments/`,
        method: 'GET',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      }).then((res)=>{
          const temp = []
          res.data.forEach((element)=>{
            temp.push(element)
          })
          this.comments = temp
      }).catch((err)=>{
        console.error(err)
      })
    },
    deleteArticle(event) {
      event.preventDefault()
      const article_pk = this.article_pk
      axios({
        url: `http://127.0.0.1:8000/api/v1/articles/${article_pk}/`,
        method: 'DELETE',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      }).then(()=>{
        // this.$router.push({name: 'Community'})
        this.$router.go(this.$router.currentRoute)
      }).catch((err)=>{
        console.error(err)
      })
    },
    updateArticle() {
      console.log(this.article_pk)
      console.log(this.title)
      console.log(this.content)
      this.$router.push({
        name: 'UpdateArticle',
        params: {
          article_pk: this.article_pk, 
          currentTitle: this.title, 
          currentContent: this.content,
        },
      })
    }
  },
  computed: {
    getDate() {
      return this.updated_at.slice(0,10)
    },
    getTime() {
      return this.updated_at.slice(11,16)
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
  created() {
    const article_pk = this.article_pk
    axios({
      url: `http://127.0.0.1:8000/api/v1/articles/${article_pk}/`,
      method: 'GET',
      headers: {
        Authorization: `JWT ${localStorage.getItem('jwt')}`
      },
    }).then((res)=>{
      console.log(res.data)
      this.title = res.data.title
      this.content = res.data.content
      this.created_at = res.data.created_at
      this.updated_at = res.data.updated_at
    }).catch((err)=>{
      console.error(err)
    }),
    axios({
      url: `http://127.0.0.1:8000/api/v1/articles/${article_pk}/comments/`,
      method: 'GET',
      headers: {
        Authorization: `JWT ${localStorage.getItem('jwt')}`
      },
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
    const token = localStorage.getItem('jwt')
    // console.log(jwt_decode(token))
    const username = jwt_decode(token).username
    this.currentName = username
    // //조회수 추가
    // axios({
    //   url: `http://127.0.0.1:8000/api/v1/articles/${article_pk}/read/`,
    //   method: 'POST',
    //   headers: {
    //     Authorization: `JWT ${localStorage.getItem('jwt')}`
    //   },
    // }).then((res)=>{
    //   console.log(res)
    // }).catch((err)=>{
    //   console.error(err)
    // })
  },
}
</script>

<style>
  .articledetail {
    background-color: black;
    height: 800px;
    color: white;
    border: 1px solid white;
    border-radius: 10px;
  }
</style>