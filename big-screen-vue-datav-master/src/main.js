import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import dataV from '@jiaminghi/data-view'
import $http from '@/api/index.js'
// 这里修复！！！！！！！！！！！！！！！
import './assets/scss/style.scss'

import Icon from 'vue-awesome/components/Icon'
import 'vue-awesome/icons/chart-bar.js'
import 'vue-awesome/icons/chart-area.js'
import 'vue-awesome/icons/chart-pie.js'
import 'vue-awesome/icons/chart-line.js'
import 'vue-awesome/icons/align-left.js'

import echarts from 'echarts'

Vue.config.productionTip = false
Vue.component('icon', Icon)
Vue.use(dataV)
Vue.prototype.$echarts = echarts
Vue.prototype.$http = $http

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})