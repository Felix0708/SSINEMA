<template>
  <div>
    <div v-if="this.$store.state.movies.length > 0" id="movieContainer">
      <ul id="movieUi">
        <v-row
          id="movieRow"
          v-masonry
          item-selector=".item">
          <v-col
            v-for="(movie, index) in movies"
            :key="movie.id"
            v-masonry-tile
            id="movieCol"
            class="item"
            cols="12"
            lg="3"
            md="3"
            sm="6">
            <v-card @click=getMovieDetail(index) id="movieBox">
              <v-img
                id="movieImg"
                :src="posterSrc(movie.poster_path)"
                :alt="movie.title"
                >
                <template v-slot:placeholder>
                  <div style="background: lightgray; height: 100%;"></div>  
                </template>  
              </v-img>
              <v-card-title id="movieTitle">
                {{ movie.title }}
              </v-card-title>
              <v-card-subtitle id="movieDate">
                {{ movie.release_date }}
              </v-card-subtitle>
            </v-card>

            <b-modal
            ref="detail"
            :data-key="index"
            size="lg" 
            class="bg-black"
            :header-bg-variant="black"
            :footer-bg-variant="black"
            hide-footer hide-header>
              <MovieDetail
                :movie_pk = movie.movie_id
              />
            </b-modal>

          </v-col>
        </v-row>
      </ul>
    </div>
    <div v-else class="nosearch">
      <img src="@/assets/nosearchresult.jpg" alt="noresult">
      <h2 class="backtext">검색하신 키워드에 대한 영화 정보가 없습니다</h2>
      <br><br><br>
      <router-link :to="{ name: 'MainPage' }">
        <button class="back backtext">홈으로 돌아가기</button>  
      </router-link>
    </div>
  </div>
</template>

<script>
import MovieDetail from '../components/MovieDetail.vue'
import { mapState } from "vuex";
export default {
  name: 'MovieList',
  components: {
    MovieDetail
  },
  computed: {
    ...mapState(["movies"])
  },
  data(){
    return {
      black : 'black'
    }
  },
  methods: {
    posterSrc (poster_path) {
      return poster_path === null ? '' : `https://image.tmdb.org/t/p/w500${poster_path}`
    },
    getMovieDetail(index) {
      const detail = this.$refs['detail'].find(
        el => el.$attrs['data-key'] === index
      );
      detail.show()
    },
  },
  created: function() {
    // const movies_list = this.$store.state.movies 
    // this.movies = movies_list
    // console.log(this.$store.state.movies.length)

  },
}
</script>

<style>
#movieUi {
  margin: auto 0;
  padding: 10px;
}
/* #movieRow{
  padding: auto 5px;;
} */
/* #movieCol {
  padding: auto 10px;
} */
#movieBox {
  display: block;
  margin: 0px auto;
  padding: auto 10px;
  height: auto;
  width: 230px;
  border: 1px solid white;
  border-radius: 10px;
  transition: all 0.8s linear;
}
#movieBox:hover {
  /* position: absolute;
  left: 25%;
  top: 50%;
  z-index: 10; */
  height: 100%;
  transform:scale(1.3);
}

#movieImg {
  /* width: 200px; */
  height: auto;
  object-fit:cover;
  /* margin: auto 0; */
  /* display: block;  */
  margin: 0px auto;
}
#movieTitle {
  font-size: 15px;
  font-weight: bold;
  padding: auto 3px 0;
  display: block; 
  margin: 0px auto;
}

.back {
  margin: auto 0;
  padding: 2px 10px 2px 10px;
  text-decoration: none;
  border: 1px solid #FF0558;
  border-radius: 16px;
  background-color: #FF0558;
  color: white;
  font-size: 20px;
}

.backtext {
  margin: 1.5px 0 0 0 ;
  color: white;
}

.nosearch{
  margin-top: 150px;
}
</style>