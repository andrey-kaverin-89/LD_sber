<template>
  <div class="main">
    <div class="circles">
      <Folder
        @click="showMails('fire')"
        class="folder"
        kind="fire"
        text="Личное участие"
        :amount="this.priority3Amount"
        :priority="3"
        id="priority_3"
      />
      <Folder
        @click="showMails('fire')"
        class="folder"
        kind="man"
        text="Делегировать"
        :amount="this.priority2Amount"
        :priority="2"
        id="priority_2"
      />
      <Folder
        @click="showMails('fire')"
        class="folder"
        kind="robot"
        text="Автоответ"
        :amount="this.priority1Amount"
        :priority="1"
        id="priority_1"
      />
      <Folder
        @click="showMails('fire')"
        class="folder"
        kind="poop"
        text="Ничего не делать"
        :amount="this.priority0Amount"
        :priority="0"
        id="priority_0"
      />
    </div>
  </div>
</template>

<script>
import Folder from "../../components/Folder/index";
import {url} from '../../url.js';
import axios from "axios";
export default {
  name: "Main",
  components: { Folder },
  data() {
    return {
      dict: {},
      priority0Amount: 0,
      priority1Amount: 0,
      priority2Amount: 0,
      priority3Amount: 0,
    }
  },
  methods: {
    showMails(value) {
      console.log(value);
    },
    onMount() {
      this.$store.dispatch("updateCurrentPage", "Main");
      let new_url = url +'/update'
      axios
              .get(new_url)
              .then(response => {
      // alert('success');
              })
              .catch(error => {
                // alert('failure');
                console.log(error);
              });
      new_url = url + "/mails";
      axios
              .get(new_url)
              .then(response => {
      // alert('success');
                let dict = {"0": 0, "1": 0, "2":0, "3":0};
                for (let i in response.data) {
                  dict[res[i].priority] ++;
                }
                this.priority0Amount = dict[0];
                this.priority1Amount = dict[1];
                this.priority2Amount = dict[2];
                this.priority3Amount = dict[3];
              })
              .catch(error => {
                // alert('failure');
                console.log(error);
              });
      // let dict = {"0": 0, "1": 0, "2":0, "3":0};
      // let res = [{"id": 1, "priority": "2"}, {"id": 2, "priority": "3"}];
      // console.log(res)
      // for (let i in res) {
      //   dict[res[i].priority] ++;
      // }
      // this.priority0Amount = dict[0];
      // this.priority1Amount = dict[1];
      // this.priority2Amount = dict[2];
      // this.priority3Amount = dict[3];
      // this.dict = dict;
      // console.log(dict);
    }
  },
  mounted() {
    this.onMount();
  }
};
</script>

<style scoped lang="scss">
.main {
  width: 100%;
  height: 100%;
  padding: 25px;
  box-sizing: border-box;
  .circles {
    width: 100%;
    display: grid;
    grid-template-columns: repeat(3, 92px);
    grid-column-gap: 25px;
    grid-row-gap: 25px;
    .folder {
      margin-right: 25px;
      &:last-child {
        margin-right: 0;
      }
    }
  }
}
</style>
