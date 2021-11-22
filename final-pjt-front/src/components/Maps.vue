<template>
  <div>
    <h3 style="color:white;">내 주변의 영화관은?</h3>
    <div class="controll">
      <button @click="zoom(-1)">
        <span class="material-icons">zoom_in</span>
      </button>
      <button @click="zoom(1)">
        <span class="material-icons">zoom_out</span>
      </button>
    </div>
    <KakaoMap class="kmap" :options="mapOption"/>
    <!-- <div class="kmap" ref="map"></div> -->
  </div>
</template>

<script>
import KakaoMap from "./KakaoMap.vue"
export default {
  components: {
    KakaoMap,
  },
  data () {
    return {
      mapOption: {
        center: {
          lat: 36.3553675622378,
          lng: 127.298408300646,
        },
        level: 8,
      }
    }
  },
  mounted () {
  },
  methods: {
    zoom(delta) {
      console.log("{delta}", delta)
      const level = Math.max(3, this.mapOption.level + delta)
      this.mapOption.level = level
    }
  },
}
</script>

<style lang="scss">
button {
  margin: 2px 2px 10px 2px;
  border: 1px solid transparent;
  padding: 6px 4px 0 3px;
  background-color: #efefefdd;
  border-radius: 6px;
  &:hover {
    background-color: #ddd;
    border-color: #ddd;
    cursor: pointer;
  }
  &:active {
    background-color: #aaa;
    border-color: #aaa;
  }
}
</style>