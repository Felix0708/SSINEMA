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
      <div class="col-2"><p><b>{{ getName }}</b></p></div>
      <div class="col-8"><p>{{ getComment }}</p></div>
      <div class="col-2"> <b><a href="" v-if="getName == currentName" @click="deleteComment">삭제</a></b></div>
      
    </div>
    <hr style="background-color:white"> 
    
  </span>
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'
// import jwt_decode from 'jwt-decode'
export default {
  components: {
    StarRating
  },
  data() {
    return {
      getName: '',
      currentName: '',
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
        url: `http://127.0.0.1:8000/api/v1/movies/${review_pk}/review_delete/` ,
        method: 'DELETE'
      }).then(()=>{
        this.$emit('onParentDeleteComment')
      }).catch((err)=>{
        console.error(err)
      })
    }
  },
  created() {
    console.log(this.comment)
    const userid = this.comment.username
    this.getName = userid
    // axios({
    //   url: `http://127.0.0.1:8000/api/v1/accounts/${userid}/`,
    //   method: 'GET',
    // }).then((res)=>{
    //   // console.log(res)
    //   this.getName = res.data.username
    // }).catch((err)=>{
    //   console.error(err)
    // })
    // const token = localStorage.getItem('jwt')
    // // console.log(jwt_decode(token))
    // const username = jwt_decode(token).username
    // this.currentName = username
  }
}
</script>

<style>
</style>