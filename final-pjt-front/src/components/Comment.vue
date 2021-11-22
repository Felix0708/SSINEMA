<template>
  <div>
    <div class="comment row">
      <div class="col-2">
        <p><b>{{ getName }}</b></p>
      </div>

      <div class="col-8">
        <p class="text-left" style="color:white">{{ getComment }}</p>
      </div>

      <div class="col-2">
        <button v-if="getName == currentName" @click="deleteComment">댓글 삭제</button>
      </div>
    </div>
    <br>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'
export default {
  data() {
    return {
      getName: '',
      currentName: '',
    }
  },
  props: {
    comment: Object,
    article_pk: Number
  },
  computed: {
    getComment() {
      return this.comment.content
    }
  },
  methods: {
    deleteComment(event) {
      event.preventDefault()
      const comment_pk = this.comment.id
      axios({
        url: `http://127.0.0.1:8000/api/v1/articles/${this.article_pk}/comments/${comment_pk}/delete/`,
        method: 'DELETE',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      }).then(()=>{
        this.$emit('onParentDeleteComment')
      }).catch((err)=>{
        console.error(err)
      })
    }
  },
  created() {
    const userid = this.comment.user
    // console.log(this.comment)
    axios({
      url: `http://127.0.0.1:8000/api/v1/accounts/${userid}/`,
      method: 'GET',
      headers: {
        Authorization: `JWT ${localStorage.getItem('jwt')}`
      },
    }).then((res)=>{
      // console.log(res)
      this.getName = res.data.username
    }).catch((err)=>{
      console.error(err)
    })
    const token = localStorage.getItem('jwt')
    // console.log(jwt_decode(token))
    const username = jwt_decode(token).username
    this.currentName = username
  }
}
</script>

<style>
  .comment {
    background-color: black;
    
    
  }
</style>