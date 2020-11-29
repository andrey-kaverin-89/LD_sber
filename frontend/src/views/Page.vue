<template>
  <div class="screen">
    <router-view />
  </div>
</template>

<script>
export default {
  name: "Page",
  components: {

  }
};
</script>

<style lang="scss" scoped>
.screen {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}
</style>
