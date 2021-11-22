<template>
  <span>
    <star-rating 
      v-bind:increment="0.5"
      v-bind:max-rating="5"
      v-bind:rating="getRating"
      v-bind:show-rating="false"
      v-bind:read-only="true"
      inactive-color="#000"
      active-color="#ff0"
      border-color="#ff0"
      v-bind:padding="8"
      v-bind:border-width="2"
      v-bind:star-size="10"
      @rating-selected="setRating">
    </star-rating>
    <div class="row">
      <div class="col-2">
        <router-link
        v-if="this.currentName != this.articleWriter"
        :to="{
          name: 'OtherProfile',
          query: {
            articleWriter: `${ this.articleWriter }`,
            articleWriterId: `${ this.articleWriterId }`,
          }
        }"
        >
          <p class="my-auto" style="color: gold;"><b>{{ getName }}</b></p>
        </router-link>
        <router-link
        v-else
        @click="refresh"
        to="/profile"
        >
          <p class="my-auto"><b>{{ getName }}</b></p>
        </router-link>
      </div>
      <div class="col-8"><p>{{ getComment }}</p></div>
      <div class="col-2"><b><a href="" @click="deleteComment">삭제</a></b></div>
      
    </div>
    <hr style="background-color:white"> 
    
  </span>
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'
import jwt_decode from 'jwt-decode'

export default {
  components: {
    StarRating
  },
  data() {
    return {
      getName: '',
      currentId: '',
      currentName: '',
      articleWriterId: '',
      articleWriter: '',
    }
  },
  props: {
    comment: Object,
    movie_pk: Number
  },
  computed: {
    getComment() {
      return this.comment.content
    },
    getRating() {
      return this.comment.rank / 2
    },
  },
  methods: {
    deleteComment(event) {
      event.preventDefault()
    
      const review_pk = this.comment.id
      axios({
        url: `http://127.0.0.1:8000/api/v1/movies/${this.movie_pk}/review/${review_pk}/` ,
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
    console.log(this.comment)
    const userid = this.comment.user.username
    this.getName = userid

    this.articleWriter = this.comment.user.username
    this.articleWriterId = this.comment.user.id
    // axios({
    //   url: `http://127.0.0.1:8000/api/v1/accounts/${userid}/`,
    //   method: 'GET',
    // }).then((res)=>{
    //   // console.log(res)
    //   this.getName = res.data.username
    // }).catch((err)=>{
    //   console.error(err)
    // })
    const token = localStorage.getItem('jwt')
    console.log(jwt_decode(token))
    // const userid = jwt_decode(token).user_id
    const username = jwt_decode(token).username
    // this.currentId = userid
    this.currentName = username
  }
}
</script>

<style>
a {
  text-decoration: none;
}
</style>