<template>
  <div class="search">
<!--    <input class="text" placeholder="Search" />-->
    <img src="./icons/loupe_blue.svg" />
  </div>
</template>

<script>
export default {
  name: "Search"
};
</script>

<style scoped lang="scss">
.search {
  height: 25px;
  display: flex;
  flex-direction: row;
  input {
    width: 232px;
    height: 25px;
    border: none;
    border-bottom: 1px solid #e5e5e5;
    font-size: 18px;
  }
}
</style>
