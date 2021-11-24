import Vue from 'vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faSearch as fasSearch } from '@fortawesome/free-solid-svg-icons'
library.add(
  faUserSecret,
  fasSearch)

Vue.component('font-awesome-icon', FontAwesomeIcon)