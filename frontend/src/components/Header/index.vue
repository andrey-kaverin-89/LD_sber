<template>
  <div class="header">
    <div class="product" @click="getHome">
      <img class="logo" src="./icons/logo.svg" />
      <img class="assistant" src="./icons/ASSISTANT.svg" />
    </div>
    <div class="user">
      <span>Sergey</span>
      <img src="./icons/безурков.png" />
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
  methods: {
    getHome() {
      this.$router.push({name: "Main"});
    }
  }
};
</script>

<style lang="scss" scoped>
.header {
  background: $white_dark1;
  width: 100%;
  height: 70px;
  -webkit-box-shadow: 0 1px 4px 1px #e5e5e5;
  box-shadow: 0 1px 4px 1px #e5e5e5;
  padding-top: 37px;
  padding-left: 15px;
  padding-right: 15px;
  padding-bottom: 7px;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
  -ms-flex-direction: row;
  flex-direction: row;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  .product {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -ms-flex-direction: row;
    flex-direction: row;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    .logo {
      width: 26px;
      height: 26px;
    }
    .assistant {
      height: 20px;
      margin-left: 5px;
    }
  }
  .user {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -ms-flex-direction: row;
    flex-direction: row;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    span {
      color: $green;
      font-size: 18px;
    }
    img {
      height: 26px;
      width: 26px;
      margin-left: 5px;
    }
  }
}
</style>
