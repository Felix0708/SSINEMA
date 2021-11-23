<template>
  <div class="profile" style="background-color: white;">
    <v-row>
      <v-col
        cols="8"
      >
        <v-file-input
          label="터치하세요"
          outlined
          dense
          accept="image/png, image/jpeg, image/bmp"
          v-model="uploadFiles"
        ></v-file-input>
      </v-col>
      <v-col
        cols="4"
      >
        <v-btn
          rounded-lg
          color="red darken-4"
          class="white--text"
          width="20"
          height="40"
          :disabled="this.uploadFiles.length === 0"
          @click="imageUpload"
        >
          업로드
        </v-btn>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import jwt_decode from 'jwt-decode'
import axios from 'axios'

export default {
  data() {
    return {
      uploadFiles: [],
    }
  },
  methods: {
    async imageUpload() {
      let fd = new FormData();
      console.log(this.uploadFiles)
      fd.append('image', this.uploadFiles)
      console.log(fd)
      for (let key of fd.entries()) {
        console.log(`${key}`)
      }
      await axios.put(`http://127.0.0.1:8000/api/v1/accounts/${this.userName}/`,
            fd, {
              headers: {
                'Content-Type': 'multipart/form-data',
                Authorization: `JWT ${localStorage.getItem('jwt')}`
              }
            }
          ).then(res => {
            // console.log('전송 성공');
            console.log(res.data)
            alert("파일이 성공적으로 업로드 되었습니다.")
            this.selected.authExample = res.data.data
          }).catch(function () {
            console.log('전송 실패')
            alert("파일 업로드에 실패하였습니다.")
          })
        
    },
  },
  created () {
    const token = localStorage.getItem('jwt')
    const decoded = jwt_decode(token)
    console.log(decoded)
    this.userName = decoded['username']
    this.userId = decoded['user_id']
    console.log(this.userName)
    console.log(this.userId)
  }
}
</script>

<style>

</style>