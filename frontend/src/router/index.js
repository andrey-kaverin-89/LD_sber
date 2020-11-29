import Vue from "vue";
import VueRouter from "vue-router";
// import Home from "../views/Page.vue";
import Vuex from "vuex";

Vue.use(Vuex);

Vue.use(VueRouter);

const router = new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/",
      component: () => import("../views/Page"),
      children: [
        {
          path: "/main",
          name: "Main",
          component: () => import("../views/Main/index")
        },
        {
          path: "/story",
          name: "Story",
          component: () => import("../views/Story/index"),
          params: true
        }
      ]
    }
  ]
});

export default router;
