<template>
  <div class="container">
    <button @click="showMails(priority)" :disabled="this.amount===0"  class="folder">
      <img v-if="this.amount===0" class="frame" src="./icons/frame_grey.png" />
      <img v-else class="frame" src="./icons/frame_color.png" />
      <div class="icon">
        <img v-if="this.kind == 'fire'" src="./icons/fire.png" />
        <img v-else-if="this.kind == 'poop'" src="./icons/poop.png" />
        <img v-else-if="this.kind == 'robot'" src="./icons/robot.png" />
        <img v-else-if="this.kind == 'man'" src="./icons/man.png" />
      </div>
    </button>
    <div v-if="this.amount!==0" class="amount">{{this.amount}}</div>
    <div class="text">
      {{ this.text }}
    </div>
  </div>
</template>

<script>
export default {
  name: "Folder",
  props: {
    kind: String,
    text: String,
    amount: Number,
    priority: Number
  },
  data() {
    return {};
  },
  methods: {
    showMails(value) {
      console.log("value before push");
      console.log(value);
      this.$store.dispatch("updateCurrentPage", "Story");
      this.$router.push({ name: "Story", params: { priority: value } });
    }
  }
};
</script>

<style scoped lang="scss">
.container {
  width: 92px;
  position: relative;
  .text {
    font-size: 12px;
    margin-top: 5px;
    max-width: 90px;
    text-align: center;
  }
  .amount{
    position: absolute;
    font-size: 15px;
    font-family: Roboto Bold;
    color: $red;
    border: 2px solid $red;
    border-radius: 100%;
    background: $white;
    padding: 1px;
    top: 0;
    right: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 20px;
    height: 20px;
  }
  .folder {
    width: 90px;
    height: 90px;
    border-radius: 100%;
    box-sizing: border-box;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    border: none;
    background: none;
    .frame {
      position: absolute;
    }
    .icon {
      width: 78px;
      height: 78px;
      background: $white_dark2;
      border-radius: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      img {
        width: 60px;
        height: 60px;
      }
    }
  }
}
</style>
