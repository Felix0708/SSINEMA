<template>
  <div class="container articledetail" style="width: auto;">
    <div class="card" style="background-color: black">
      <div class="card-header">
        <div class='d-flex'>
          <!-- params로 보내면 데이터 유지가 안된다.  -->
          <router-link
            v-if="this.currentName != writer"
            :to="{
              name: 'OtherProfile',
              query: {
                articleWriter: `${ this.articleWriter }`,
                articleWriterId: `${ this.articleWriterId }`,
              }
            }"
            class="my-auto"
            >
            <p><b>{{writer}}</b></p>
          </router-link>
          <router-link
            v-else
            to="/profile"
            class="my-auto"
          >
            <p><b>{{writer}}</b></p>
          </router-link>
          <p class="mt-2 me-5 ml-4 my-auto"><b>님의 글</b></p>
          <p class="mt-2 ms-5 ml-auto mr-4" style="display: inline;">{{getDate}} {{ getTime }}</p>
        </div>
        <p class="card-title mt-2" style="text-align: left;"><b>{{ title }}</b></p>
      </div>
      <hr style="margin: 0;">
      <div class="card-body">
        <br>
        <p class="card-text" style="text-align: left; margin: 0;">{{ content }}</p>
        <br>
        <div>
          <form @submit="like" class="d-inline like-form">
            <!-- {% if user in article.like_users.all %} -->
              <button v-if="this.articleLikeusers.includes(this.userId)" class="btn btn-link p-0 m-0" style="box-shadow: none;">
                <i id="like" class="fas fa-heart" style="color:crimson;"></i>
              </button>
            <!-- {% else %} -->
              <button v-else class="btn btn-link p-0 m-0" style="box-shadow: none;">
                <i id="like" class="far fa-heart" style="color:crimson;"></i>
              </button>
            <!-- {% endif %} -->
          </form>
          <span id="like-count"> &nbsp; {{ this.articleLike }} 명이 이 글을 좋아합니다.</span>
        </div>
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
      articleId: '',
      articleWriterId: '',
      articleWriter: '',
      articleLike: 0,
      articleLikeusers: [],
      title: '',
      content: '',
      created_at: '',
      updated_at: '',
      mycomment: '',
      comments: [],
      currentId: '',
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
    like (event) {
      event.preventDefault()
        const token = localStorage.getItem('jwt')
        // console.log(jwt_decode(token))
        const userid = jwt_decode(token).user_id
        this.userId = userid
        console.log(this.userId)
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/api/v1/articles/${this.article_pk}/like/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
        .then(function (response) {
          console.log(response)
          const liked = response.data.liked
          const likeBtn = document.querySelector(`#like`)
          if (liked === true) {
            likeBtn.classList.add('fas')
            likeBtn.classList.remove('far')
          } else {
            likeBtn.classList.add('far')
            likeBtn.classList.remove('fas')
          }
        }) .then(() => {
            const article_pk = this.article_pk
            axios({
              url: `http://127.0.0.1:8000/api/v1/articles/${article_pk}/`,
              method: 'GET',
              headers: {
                Authorization: `JWT ${localStorage.getItem('jwt')}`
              },
            }).then((res)=>{
              console.log(res.data)
              this.articleWriterId = res.data.serializer.user
              this.articleLikeusers = res.data.like_people
              this.articleLike = res.data.serializer.like_users_count
              this.title = res.data.serializer.title
              this.content = res.data.serializer.content
              this.created_at = res.data.serializer.created_at
              this.updated_at = res.data.serializer.updated_at
              console.log(this.articleWriterId)
              console.log(this.articleLikeusers)
            }).catch((err)=>{
              console.error(err)
            })
        }).catch((err) => {
          console.log(err)
        }).catch((err) => {
          console.log(err)
        })
    },

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
            article: article_pk,
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
        const temp = []
        this.comments = temp
        console.error(err)
      })
    },
    deleteArticle(event) {
      event.preventDefault()
      const article_pk = this.article_pk
      this.articleId = article_pk
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
      // console.log(this.article_pk)
      // console.log(this.title)
      // console.log(this.content)
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
    this.articleWriter = this.writer
    // console.log(this.articleWriter)
    const article_pk = this.article_pk
    console.log(this.articleLikeusers)
    axios({
      url: `http://127.0.0.1:8000/api/v1/articles/${article_pk}/`,
      method: 'GET',
      headers: {
        Authorization: `JWT ${localStorage.getItem('jwt')}`
      },
    }).then((res)=>{
      console.log(res.data)
      this.articleWriterId = res.data.serializer.user
      this.articleLikeusers = res.data.like_people
      this.articleLike = res.data.serializer.like_users_count
      this.title = res.data.serializer.title
      this.content = res.data.serializer.content
      this.created_at = res.data.serializer.created_at
      this.updated_at = res.data.serializer.updated_at
      // console.log(this.articleWriterId)
      console.log(this.articleLikeusers)
    }).catch((err)=>{
      console.error(err)
    })

    axios({
      url: `http://127.0.0.1:8000/api/v1/articles/${article_pk}/comments/`,
      method: 'GET',
      headers: {
        Authorization: `JWT ${localStorage.getItem('jwt')}`
      },
    }).then((res)=>{
        // console.log(res)
        const temp = []
        res.data.forEach((element)=>{
          temp.push(element)
        })
        this.comments = temp
    }).catch((err)=>{
      console.error(err)
    })

    const token = localStorage.getItem('jwt')
    console.log(jwt_decode(token))
    const userid = jwt_decode(token).user_id
    const username = jwt_decode(token).username
    this.userId = userid
    console.log(this.userId)
    this.currentName = username

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

<style scoped>
  a {
    text-decoration: none;
  }
  a > p {
    color: gold;
    margin-top: 3px;
    margin-right: 3px;
  }
</style>