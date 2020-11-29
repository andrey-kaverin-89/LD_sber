<template>
  <div class="functions">
    <button class="menu"><img src="./icons/menu.svg" /></button>
    <div class="container">
      <Search />
      <button class="filter"><img src="./icons/filter.svg" /></button>
    </div>
  </div>
</template>

<script>
import Search from "../Inputs/Search/index";
export default {
  name: "Functions",
  components: { Search }
};
</script>

<style scoped lang="scss">
.functions {
  width: 100%;
  height: 55px;
  border-bottom: 1px solid $white_dark2;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
  -ms-flex-direction: row;
  flex-direction: row;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  padding: 15px;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  .container {
    display: flex;
    flex-direction: row;
    .filter {
      margin-left: 15px;
    }
  }
  .menu {
    margin: 0px;
    padding: 0px;
    background: none;
    border: none;
    img {
      width: 25px;
      height: 25px;
    }
  }
  .search {
  }
  .filter {
    margin: 0px;
    padding: 0px;
    background: none;
    border: none;
    img {
      width: 25px;
      height: 25px;
    }
  }
}
</style>
