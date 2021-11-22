<template>
  <div ref="map"></div>
</template>

<script>
export default {
  data () {
    return {
      mapInstance: null
    }
  },
  props: [
    'options'
  ],
  mounted() {
    let kakao = window.kakao;
    console.log(this.$refs.map); //shuould be not null

    var container = this.$refs.map; //지도를 담을 영역의 DOM 레퍼런스
    // var options = { //지도를 생성할 때 필요한 기본 옵션
    //   center: new kakao.maps.LatLng(36.3553675622378, 127.298408300646), //지도의 중심좌표.
    //   level: 4 //지도의 레벨(확대, 축소 정도)
    // };
    const {center, level} = this.options
    this.mapInstance = new kakao.maps.Map(container, {
      center: new kakao.maps.LatLng(center.lat, center.lng),
      level,
    }); //지도 생성 및 객체 리턴
    // console.log(this.mapInstance)
  },
  watch: {
    'options.level'(cur, prev) {
      console.log(`[LEVEL CHANGED] ${prev} => ${cur}`); // for testing
      this.mapInstance.setLevel(cur);
    }
  }
}
</script>

<style>
.kmap {
  width: 100%;
  height: 600px;
}
</style>