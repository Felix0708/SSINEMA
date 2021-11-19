<template>
  <tr v-on:click="getArticleDetail()">
    <td>{{ getTitle }}</td>
    <td v-if="point > 600">
      <b style="color:gold;">{{ getUsername }}</b>
    </td>
    <td v-else-if="point > 300">
      <b style="color:silver;">{{ getUsername }}</b>
    </td>
    <td v-else>
      <b style="color:brown;">{{ getUsername }}</b>
    </td>
    <td>{{ getComments_cnt }}</td>
    <td>{{ getRead }}</td>
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
      point:0,
    }
  },
  props: {
    article: Object
  },
  methods: {
    getArticleDetail() {
      // this.$router.push({name: 'ArticleDetail', params: {article_pk: this.article.id, writer: this.getUsername}})
      this.$refs['detail'].show()
    },
  },
  computed: {
    getTitle() {
      return this.article.title
    },
    getRead() {
      return this.article.read
    },
    getComments_cnt(){
      return this.article.comments_cnt
    }
  },
  created() {
    const userid = this.article.user
    axios({
      url: `http://127.0.0.1:8000/api/v1/accounts/${userid}/`,
      method: 'GET',
    }).then((res)=>{
      // console.log(res)
      this.getUsername = res.data.username
    }).catch((err)=>{
      console.error(err)
    })
    axios({
      url: `http://127.0.0.1:8000/api/v1/accounts/${userid}/points/`,
      method: 'GET'
    }).then((res)=>{
      // console.log(res.data)
      this.point = res.data.point
    }).catch((err)=>{
      console.log(err)
    })
  }
}
</script>

<style>
  
</style>