<template>
  <div class="container">
    <br><br><br><br>
    <form @submit="onSubmit">
      <div class="form-group">
        <label for="title">TITLE</label>
        <textarea class="form-control" id="title" rows="1" v-model="title"></textarea>
      </div>
      <div class="form-group">
        <label for="content">CONTENT</label>
        <textarea class="form-control" id="content" rows="10" v-model="content"></textarea>
      </div>
      <button class="btn btn-primary">Submit</button>
    </form>
    <br><br><br><br><br><br><br><br><br><br>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'UpdateArticle',
  data: function () {
    return {
      title: '',
      content: '',
    }
  },
  props: {
    article_pk: { 
      type: Number,
    },
    currentTitle: {
      type: String,
    },
    currentContent: {
      type: String,
    },
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      if (this.title.length <= 100) {
        const article_pk = this.article_pk
        axios({
          url: `http://127.0.0.1:8000/api/v1/articles/${article_pk}/`,
          method: 'PUT',
          data: {
            title: this.title,
            content: this.content,
          },
          headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`
          },
        }).then(()=>{
          this.$router.push('/community')
        }).catch(err=>{
          console.error(err)
        })
      } else {
        alert("제목은 100자 이하로 입력하세요.")
      }  
    },
  },
  created() {
    // console.log(this.$route.params.data)
    this.title = this.currentTitle
    this.content = this.currentContent
  },
}
</script>

<style scoped>
  label {
    font-size: 20px;
    font-weight: bold;
    color: white;
    margin-bottom: 10px;
  }

  button {
    margin-top: 10px;
  }

  textarea {
    margin-bottom: 10px;
  }
</style>