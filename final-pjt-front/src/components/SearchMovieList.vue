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
          <v-card>
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
        </v-col>
      </v-row>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'MovieList',
  computed: {
    movies() {
      return this.$store.state.movie.movies
    }
  },
  methods: {
    posterSrc (poster_path) {
      return poster_path === null ? '' : `https://image.tmdb.org/t/p/w500${poster_path}`
    },
    posterHeight (poster_path) {
      return poster_path === null ? 100 : 300

    },
  },
}
</script>

<style>

</style>