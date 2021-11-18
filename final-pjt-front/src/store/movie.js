import axios from 'axios'

export default {
  // namespace가 없으면 결과적으로 모듈에서 정상적으로 사용하는 것이 불가능하다
  namespaced: true,

    // state는 일종의 데이터이다.
    // 데이터는 참조관계가 발생하기 때문에 함수로 생성해야한다.
    // arrow function을 사용하여 객체 데이터를 반환할 수 있게 한다 
  state: () => ({
    title: '',
    loading: false,
    movies: [],
  }),
  getters: {},

  // mutations와 actions의 가장 큰 차이는 비동기처리 가능 유무이다
  mutations: {
    // updateTitle(state, title) {
    //   state.title = title
    // },
    // updateLoading() {

    // },

    // 범용화된 mutations
    updateState (state, payload) {
      Object.keys(payload).forEach(key => {
        state[key] = payload[key]
      })
    },
    pushIntoMovies (state, movies) {
      // ...: 전개연산자, item단위로 끊어준다
      state.movies.push(...movies)
    }
  },
  actions: {
    async searchMovies ({ state, commit }) {
      // actions에서 state, 즉 데이터부분에 바로 값을 할당하는 것은 불가능하다
      // 따라서 state의 값을 갱신하려면 mutations를 사용해야한다
      // state.loading = true
      commit('updateState', {
        loading: true,
      })

      const API_KEY = process.env.VUE_APP_TMDB_API_KEY
      const API_URL = `https://api.themoviedb.org/3/search/movie?api_key=${ API_KEY }&language=ko&query=`
      const res = await axios.get(API_URL + state.title + '&page=1')
      console.log(res.data)
      commit('updateState', {
        movies: res.data.results,
      })

      const pageLength = res.data.total_pages
      if(pageLength > 1) {
        for (let i = 2; i <= pageLength; i++) {
          // 4페이지 까지
          if (i > 4) break

          // for문 안에 await가 있기때문에 한번 반복하다 await에 걸리면 잠시 기다리고 await요청이 끝나서 마무리 되면 다시 반복한다
          const resMore = await axios.get(API_URL + state.title + `&page=${i}`)
          commit('pushIntoMovies', resMore.data.results) 
        }
      }

      commit('updateState', {
        loading: false,
      })
    }
  },
}