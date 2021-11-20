<template>
  <tr v-on:click="getArticleDetail()">
    <td style="color: white;">{{ getTitle }}</td>
    <td style="color: white;">{{ getUsername }}</td>
    <td style="color: white;">{{ getComments_cnt }}</td>
    <td style="color: white;">{{ getRead }}</td>
    <b-modal 
      ref="detail" 
      size="lg" 
      class="bg-black"
      :header-bg-variant="black"
      :footer-bg-variant="black"
      hide-footer hide-header>
        <ArticleDetail
          :article_pk ="article.id"
          :writer ="getUsername"
        />
      </b-modal>
  </tr>   
</template>

<script>
import axios from 'axios'
import ArticleDetail from '../components/ArticleDetail.vue'
export default {
  name: 'Article',
  components:{
    ArticleDetail
  },
  data() {
    return {
      getUsername: '',
      black:'black',
    }
  },
  props: {
    article: Object
  },
  methods: {
    getArticleDetail() {
      this.$refs['detail'].show()
    },
  },
  computed: {
    getTitle() {
      return this.article.title
    },
    getRead() {
      return this.article.view_count
    },
    getComments_cnt(){
      return this.article.comment_count
    }
  },
  created() {
    console.log(this.article)
    const userid = this.article.user

    axios({
      url: `http://127.0.0.1:8000/api/v1/accounts/${userid}/`,
      method: 'GET',
      headers: {
        Authorization: `JWT ${localStorage.getItem('jwt')}`
      },
    }).then((res)=>{
      // console.log(res)
      this.getUsername = res.data.username
    }).catch((err)=>{
      console.error(err)
    })
  }
}
</script>

<style>

</style>