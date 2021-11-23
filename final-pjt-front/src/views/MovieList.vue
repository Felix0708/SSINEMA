<template>
  <div>
    <ul>
      <v-row
        v-masonry
        item-selector=".item">
        <v-col
          v-for="movie in movies"
          :key="movie.id"
          v-masonry-tile
          class="item"
          cols="12"
          lg="3"
          md="3"
          sm="6">
          <v-card @click=getMovieDetail()>
            <v-img
              :src="posterSrc(movie.poster_path)"
              :alt="movie.title"
              :height="posterHeight(movie.poster_path)">
              <template v-slot:placeholder>
                <div style="background: lightgray; height: 100%;"></div>  
              </template>  
            </v-img>
            <v-card-title>
              {{ movie.title }}
            </v-card-title>
            <v-card-subtitle>
              {{ movie.release_date }}
            </v-card-subtitle>
          </v-card>

          <b-modal
          ref="detail"
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
    posterHeight (poster_path) {
      return poster_path === null ? 100 : 300
    },
    getMovieDetail() {
      this.$refs['detail'].show()
    },
  },
  created: function() {
    // const movies_list = this.$store.state.movies 
    // this.movies = movies_list
    // console.log(this.movies)

  },
}
</script>

<style>

</style>