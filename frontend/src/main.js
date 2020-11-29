import Vue from 'vue'
import App from './App.vue'
import store from "./store";
import router from "./router";
import "./style/variables.scss";
import "./style/fonts.scss";
import "./style/main.scss";

Vue.config.productionTip = false

window.history.pushState("", "Main", "/main");

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
