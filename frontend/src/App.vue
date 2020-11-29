<template>
  <div id="app">
    <Header/>
    <Functions v-if="getCurrentPage === 'Main'"/>
    <router-view />
  </div>
</template>

<script>
import Header from "@/components/Header/index";
import Functions from "@/components/Functions/index";

export default {
  name: 'App',
  components: {
    Functions,
    Header
  },
  computed: {
    getCurrentPage: function () {
      console.log(this.$store.getters.currentPage);
      return this.$store.getters.currentPage;
    }
  }
}
</script>

<style>
#app {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}
</style>
