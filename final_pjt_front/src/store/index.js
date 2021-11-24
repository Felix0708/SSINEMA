import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
    // state는 일종의 데이터이다.
    // 데이터는 참조관계가 발생하기 때문에 함수로 생성해야한다.
    // arrow function을 사용하여 객체 데이터를 반환할 수 있게 한다 
  state: {
    title: '',
    movies: [],
  },
  getters: {},

  // mutations와 actions의 가장 큰 차이는 비동기처리 가능 유무이다
  mutations: {
    // updateTitle(state, title) {
    //   state.title = title
    // },
    // updateLoading() {

    // },

    // 범용화된 mutations
    // updateState (state, payload) {
    //   Object.keys(payload).forEach(key => {
    //     state[key] = payload[key]
    //   })
    //   console.log(state.movies)
    // },
    pushIntoMovies (state, movies) {
      // ...: 전개연산자, item단위로 끊어준다
      state.movies = movies
    },
    searchMovie (state, title) {
      state.title = title
      console.log(state.title)
    },
  },
  actions: {
    searchMovie({ commit }, title) {
      commit('searchMovie', title)
    },
    searchMovies ({ state, commit }) {
      // actions에서 state, 즉 데이터부분에 바로 값을 할당하는 것은 불가능하다
      // 따라서 state의 값을 갱신하려면 mutations를 사용해야한다
      // state.loading = true

      const back_url = 'http://127.0.0.1:8000/api/v1/movies/all/'
      // const res = await axios.get(back_url + state.title + '/')
      axios.get(back_url + state.title + '/')
      .then((res) => {
        if (res.data.length != 0) {
          commit('pushIntoMovies', res.data,)
        //   this.$router.push({ name: 'MovieList' })
        } else {
          commit('pushIntoMovies', [])
        //   console.log(res.data.length)
        //   alert('검색한 결과가 없습니다.')
        //   this.$router.push({ name: 'Home' })
        }
      })
      .catch((err) => {
        console.log(err)
      })
      
      

      // const pageLength = res.data.total_pages
      // if(pageLength > 1) {
      //   for (let i = 2; i <= pageLength; i++) {
      //     // 4페이지 까지
      //     if (i > 4) break

      //     // for문 안에 await가 있기때문에 한번 반복하다 await에 걸리면 잠시 기다리고 await요청이 끝나서 마무리 되면 다시 반복한다
      //     const resMore = await axios.get(API_URL + state.title + `&page=${i}`)
      //     commit('pushIntoMovies', resMore.data.results) 
      //   }
      // }
    }
  },
})