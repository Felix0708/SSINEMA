<template>
  <div class="search-container">
    <form class="searchbox">
      <input type="search" placeholder="Search......" name="search" class="searchbox-input" 
      v-model="title"
      @keyup="buttonUp"
      @keypress.enter="searchMovies"
      required>
      <input type="submit" @click="searchMovies" class="searchbox-submit" value="GO">
      <span class="searchbox-icon" @click="submitClick" @mouseup="submitMouse"><i class="fa fa-search"></i></span>
    </form>
  </div>
</template>

<script>
// import { mapActions } from 'vuex'
// const API_KEY = process.env.VUE_APP_TMDB_API_KEY
// const API_URL = `https://api.themoviedb.org/3/search/movie?api_key=${ API_KEY }&language=ko&query=`
import { mapState } from "vuex";

export default {
  name: 'SearchBar',
  data: function() {
    return {
      title: '',
      isOpen: false,
    }
  },
  // computed 는 vue에서 직접 조작할 수 없다
  // computed: {
  //   title: {
  //     // 값을 양방향 바인딩을 통해서 input에서 직접 수정할때는 setter를 지정하여 store의 mutations를 통해 title이 수정되는 구조로 만들어야 한다.

  //     // Getter
  //     get () {
  //       return this.$store.state.movie.title
  //     },
      
  //     // Setter
  //     set(title) {
  //       this.$store.commit('movie/updateState', {
  //         title
  //       })
  //     },
  //   },
  // },
  computed: {
    ...mapState(["movies"])
  },
  methods:{
    searchMovies() {
      this.$store.dispatch('searchMovie', this.title)
      this.$store.dispatch('searchMovies')
      console.log(this.$store.state.movies)
      this.$router.push({ name: 'MovieList' })
    },
    // async searchMovies() {
    //   await this.$store.dispatch('searchMovie', this.title)
    //   await this.$store.dispatch('searchMovies')
    //   console.log(this.$store.state.movies)
    //   if (this.$store.state.movies.length > 0) {
    //   await this.$router.push({ name: 'MovieList' })
    //   //   event.preventDefault()
    //   } else {
    //     this.$router.push({ name: 'Page_404' })
    //   }
    // },

    buttonUp: function() {
      var inputVal = document.querySelector('.searchbox-input').value;
      inputVal = inputVal.trim().length;
      if(inputVal !== 0){
        document.querySelector('.searchbox-icon').style.display="none";
      } else {
        document.querySelector('.searchbox-input').value = '';
        document.querySelector('.searchbox-icon').style.display="none";
      }
    },

    submitClick: function() {
      if(this.isOpen == false) {
        document.querySelector('.searchbox').classList.add('searchbox-open');
        document.querySelector('.searchbox-input').focus();
        this.isOpen = true;
      } else {
        document.querySelector('.searchbox').classList.remove('searchbox-open');
        this.isOpen = false;
      }
      
    },

    submitMouse: function() {
      document.querySelector('.searchbox-icon')
      
    },
    docMouseUp: function() {
      if (this.isOpen == true) {
        document.querySelector('.searchbox-icon').style.display="none";
        this.submitClick()
      }
    },

    created: function() {
      document.addEventListener("mouseup", this.docMouseUp)
    },
  },
} 


</script>

<style>
.search-container{
    width:600px;
    margin: auto 30px auto 0;
    padding: 0;
}

.searchbox{
    position:relative;
    min-width:50px;
    width:0%;
    height:50px;
    float:right;
    overflow:hidden;    
    -webkit-transition: width 0.3s;
    -moz-transition: width 0.3s;
    -ms-transition: width 0.3s;
    -o-transition: width 0.3s;
    transition: width 0.3s;
}

.searchbox-input{
    top:0;
    right:0;
    border:0;
    outline:0;
    background:#dcddd8;
    width:100%;
    height:50px;
    margin:0;
    padding:0px 55px 0px 20px;
    font-size:20px;
    color: #000;
}
.searchbox-input::-webkit-input-placeholder {
    color: #000;
    opacity:0.8;
}
.searchbox-input:-moz-placeholder {
        color: #000;
    opacity:0.8;
}
.searchbox-input::-moz-placeholder {
        color: #000;
    opacity:0.8;
}
.searchbox-input:-ms-input-placeholder {
        color: #000;
    opacity:0.8;
}

.searchbox-icon,
.searchbox-submit{
    width:50px;
    height:50px;
    display:block;
    position:absolute;
    top:0;
    font-family:verdana;
    font-size:22px;
    right:0;
    padding:0;
    margin:0;
    border:0;
    outline:0;
    line-height:50px;
    text-align:center;
    cursor:pointer;
    color:#dcddd8 !important;
    background:#FF0558;
}



.searchbox-open{
    width:100%;
}
.center {

  text-align: center;
  margin: 0 auto;
  float: none;
  margin-top: 40px;
}

</style>
  
  