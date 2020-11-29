<template>
  <div class="story">
    <div>
      <div class="rects">
        <div
          v-for="i in mails"
          class="rect"
          :style="'width: calc(100%/' + mails.length + ')'"
          :key="i.id"
          :class="id === i.id ? 'active' : 'inactive'"
        ></div>
      </div>
 <div class="mail">
      <div class="sender">
        <img src="./icons/user.png" />
        <span>{{this.mail["mail"]}}</span>
      </div>
      <div class="date">{{getDate(this.mail["date"])}}</div>
    <div class="tag" v-for="(i, key) in getTags(this.mail.tags)" :key="key">{{i}}</div>
      <div class="subject">{{this.mail.subject}}</div>
      <div class="text">
        {{ this.fullText ? this.mail.text : this.mail.short_text}}
      </div>
   <div @click="nextMail()" class="click"></div>
 </div>
    </div>
    <div>
      <div class="more">
        <img @click="showText()" src="./icons/more.svg"/>
      </div>
      <input id="input_answer" type="text" v-model="input"/>
      <div class="answers">
        <div
                @click="selectAnswer(i)"
          class="answer"
          v-for="(i, key) in [
            'Ок, спасибо!',
            'Принято, буду.',
            'Участие подтверждаю'
          ]"
          :key="key"
        >
          {{ i }}
        </div>
      </div>

      <div class="menu">
        <button @click="goHome" class="back">
          <img src="./icons/arrow.svg" />
        </button>
        <div class="helper">
          <button @click="showForward" class="forward">
            <img src="./icons/forward.svg" />
          </button>
          <button @click="seeAgain(id)" class="unsee">
            <img src="./icons/unsee.svg" />
          </button>
          <button @click="getMicrophone" class="micro">
            <img src="./icons/mic.svg" />
          </button>
          <button @click="getVoice(id)" class="voice">
            <img src="./icons/voice.svg" />
          </button>
          <button @click="reply(mail)" class="reply">
            <img src="./icons/reply.svg" />
          </button>
        </div>
      </div>
    </div>
    <div v-if="this.forward" class="forwardWindow">
      <div @click="closeForward" class="shadow">
      </div>
        <div class="forward">
            <div @click="addForward(i, key)" :id="'user_'+key" class="item" v-for="(i, key) in getForwardList(this.id)" :key="key" >
                <img src="./icons/forward0.png">
                <span> {{i}}</span>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
  import axios from "axios";
  import {url} from '../../url.js';
export default {
  name: "Story",
  data() {
    return {
      kind: String,
      id: Number,
      index: Number,
      forward: false,
      priority: Number,
      mails: Array,
      mail: Object,
      fullText: false,
      input: "",
        forwardList: Array
    };
  },
  methods: {
    getMail: function (id) {
      for (let i in this.mails) {
        console.log(this.mails[i]);
        if (this.mails[i].id === id) {
          this.mail = this.mails[i];
        }
      }
    },
    onMount() {
      this.$store.dispatch('updateCurrentPage', "Story");
      this.priority = this.$route.params.priority;
      const new_url = url+'/mails/'+this.priority;
      axios
              .get(new_url)
              .then(response => {
                this.mails = response.data;
                this.id = response.data[0].id;
                this.index = 0;
                this.mail = this.mails[this.index];
            // alert('success');
              })
              .catch(error => {
                // alert('failure');
                console.log(error);
              });
      // let res = [{"id": 1,
      //   "date": "Sat, 28 Nov 2020 11:07:08 +0300",
      //   "mail": "andrey.kaverin.89@mail.ru",
      //   "subject": "Re: Hello",
      //   "text": "\u041c\u0430\u0440\u0438\u043d\u0430, \u043f\u0440\u0438\u0432\u0435\u0442!\n\u042f \u043f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u043b\u0430 \u043f\u043e \u0444\u0430\u0439\u043b\u0443 \u043e\u043f\u0442. \u0441\u043f\u043b\u0438\u0442 \u043d\u0430 \u043d\u0430\u0448 \u0431\u044e\u0434\u0436\u0435\u0442 2021, \u0435\u0441\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441\u044b:\n- \u043f\u043e \u043e\u043f\u0446\u0438\u0438, \u043a\u043e\u0442. \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u0442 \u043c\u043e\u0434\u0435\u043b\u044c \u2013 \u043f\u043e\u0447\u0435\u043c\u0443 \u0442\u0430\u043a \u043c\u0430\u043b\u043e \u043e\u0442 \u043f\u0435\u0440\u0444\u043e\u043c\u0430\u043d\u0441\u0430 \u0437\u0430\u043a\u0430\u0437\u043e\u0432? \u042d\u0442\u043e \u0435\u0434\u0438\u043d\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u043a\u0430\u043d\u0430\u043b, \u043d\u0430\u043f\u0440\u044f\u043c\u0443\u044e \u043d\u0430 \u043d\u0438\u0445 \u0440\u0430\u0431\u043e\u0442\u0430\u044e\u0449\u0438\u0439.\n- \u0443 \u043d\u0430\u0441 \u0443\u0447\u0438\u0442\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f \u043d\u0430 \u0435\u043c\u043a\u043e\u0441\u0442\u044c \u043d\u0430 \u043f\u0435\u0440\u0444. \u043a\u0430\u043d\u0430\u043b\u043e\u0432? \u041a\u0430\u043a\u0438\u0435?\n- \u043c\u043e\u0436\u043d\u043e \u043b\u0438 \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0440\u0430\u0441\u0447\u0435\u0442 \u2013 \u0434\u043b\u044f \u0435\u0449\u0435 2\u0445 \u0441\u043f\u043b\u0438\u0442\u043e\u0432 \u0441 \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u0438\u0435\u043c \u0440\u0430\u0434\u0438\u043e \u0438 \u041e\u041e\u041d (\u0444\u0430\u0439\u043b \u0441\u043f\u043b\u0438\u0442 2021) \u2013 \u043a\u0430\u043a \u043e\u043f\u0442\u0438\u043c\u0430\u043b\u044c\u043d\u043e \u043f\u043e \u0434\u0440\u0443\u0433\u0438\u043c \u043c\u0435\u0434\u0438\u0430 \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u0431\u044e\u0434\u0436\u0435\u0442 \u0438 \u043d\u0430\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043c\u0435\u043d\u044c\u0448\u0435 \u0431\u0443\u0434\u0435\u0442 \u0437\u0430\u044f\u0432\u043e\u043a?\n\u00a0\n\u00a0\n\u00a0\n\u00a0\n\u00a0 \n>\u0427\u0435\u0442\u0432\u0435\u0440\u0433, 26 \u043d\u043e\u044f\u0431\u0440\u044f 2020, 23:22 +03:00 \u043e\u0442 adva.mailer.pub@gmail.com:\n>\u00a0\n>Hello World",
      //   "short_text": "\u0441\u043f\u043b\u0438\u0442 \u043d\u0430 \u043d\u0430\u0448 \u0431\u044e\u0434\u0436\u0435\u0442 2021, \u0435\u0441\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441\u044b:\n- \u043c\u043e\u0436\u043d\u043e \u043b\u0438 \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0440\u0430\u0441\u0447\u0435\u0442 \u2013 \u0434\u043b\u044f \u0435\u0449\u0435 2\u0445 \u0441\u043f\u043b\u0438\u0442\u043e\u0432 \u0441 \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u0438\u0435\u043c \u0440\u0430\u0434\u0438\u043e \u0438 \u041e\u041e\u041d (\u0444\u0430\u0439\u043b \u0441\u043f\u043b\u0438\u0442 2021) \u2013 \u043a\u0430\u043a \u043e\u043f\u0442\u0438\u043c\u0430\u043b\u044c\u043d\u043e \u043f\u043e \u0434\u0440\u0443\u0433\u0438\u043c \u043c\u0435\u0434\u0438\u0430 \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u0431\u044e\u0434\u0436\u0435\u0442 \u0438 \u043d\u0430\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043c\u0435\u043d\u044c\u0448\u0435 \u0431\u0443\u0434\u0435\u0442 \u0437\u0430\u044f\u0432\u043e\u043a?",
      //   "tags": "#\u043d\u0430 #\u043f\u043e #\u2013 #\u0441\u043f\u043b\u0438\u0442 #\u0431\u044e\u0434\u0436\u0435\u0442",
      //   "priority": "2"},
      //   {"id": 2,
      //     "date": "Sat, 28 Nov 2020 11:07:08 +0300",
      //     "mail": "andrey.kaverin.89@mail.ru",
      //     "subject": "Re: Hello!!!",
      //     "text": "ЕЩЕ ОДИН ТЕКСТ \u041c\u0430\u0440\u0438\u043d\u0430, \u043f\u0440\u0438\u0432\u0435\u0442!\n\u042f \u043f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u043b\u0430 \u043f\u043e \u0444\u0430\u0439\u043b\u0443 \u043e\u043f\u0442. \u0441\u043f\u043b\u0438\u0442 \u043d\u0430 \u043d\u0430\u0448 \u0431\u044e\u0434\u0436\u0435\u0442 2021, \u0435\u0441\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441\u044b:\n- \u043f\u043e \u043e\u043f\u0446\u0438\u0438, \u043a\u043e\u0442. \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u0442 \u043c\u043e\u0434\u0435\u043b\u044c \u2013 \u043f\u043e\u0447\u0435\u043c\u0443 \u0442\u0430\u043a \u043c\u0430\u043b\u043e \u043e\u0442 \u043f\u0435\u0440\u0444\u043e\u043c\u0430\u043d\u0441\u0430 \u0437\u0430\u043a\u0430\u0437\u043e\u0432? \u042d\u0442\u043e \u0435\u0434\u0438\u043d\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u043a\u0430\u043d\u0430\u043b, \u043d\u0430\u043f\u0440\u044f\u043c\u0443\u044e \u043d\u0430 \u043d\u0438\u0445 \u0440\u0430\u0431\u043e\u0442\u0430\u044e\u0449\u0438\u0439.\n- \u0443 \u043d\u0430\u0441 \u0443\u0447\u0438\u0442\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f \u043d\u0430 \u0435\u043c\u043a\u043e\u0441\u0442\u044c \u043d\u0430 \u043f\u0435\u0440\u0444. \u043a\u0430\u043d\u0430\u043b\u043e\u0432? \u041a\u0430\u043a\u0438\u0435?\n- \u043c\u043e\u0436\u043d\u043e \u043b\u0438 \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0440\u0430\u0441\u0447\u0435\u0442 \u2013 \u0434\u043b\u044f \u0435\u0449\u0435 2\u0445 \u0441\u043f\u043b\u0438\u0442\u043e\u0432 \u0441 \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u0438\u0435\u043c \u0440\u0430\u0434\u0438\u043e \u0438 \u041e\u041e\u041d (\u0444\u0430\u0439\u043b \u0441\u043f\u043b\u0438\u0442 2021) \u2013 \u043a\u0430\u043a \u043e\u043f\u0442\u0438\u043c\u0430\u043b\u044c\u043d\u043e \u043f\u043e \u0434\u0440\u0443\u0433\u0438\u043c \u043c\u0435\u0434\u0438\u0430 \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u0431\u044e\u0434\u0436\u0435\u0442 \u0438 \u043d\u0430\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043c\u0435\u043d\u044c\u0448\u0435 \u0431\u0443\u0434\u0435\u0442 \u0437\u0430\u044f\u0432\u043e\u043a?\n\u00a0\n\u00a0\n\u00a0\n\u00a0\n\u00a0 \n>\u0427\u0435\u0442\u0432\u0435\u0440\u0433, 26 \u043d\u043e\u044f\u0431\u0440\u044f 2020, 23:22 +03:00 \u043e\u0442 adva.mailer.pub@gmail.com:\n>\u00a0\n>Hello World",
      //     "short_text": "ЕЩЕ ОДИН ТЕКСТ \u0441\u043f\u043b\u0438\u0442 \u043d\u0430 \u043d\u0430\u0448 \u0431\u044e\u0434\u0436\u0435\u0442 2021, \u0435\u0441\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441\u044b:\n- \u043c\u043e\u0436\u043d\u043e \u043b\u0438 \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0440\u0430\u0441\u0447\u0435\u0442 \u2013 \u0434\u043b\u044f \u0435\u0449\u0435 2\u0445 \u0441\u043f\u043b\u0438\u0442\u043e\u0432 \u0441 \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u0438\u0435\u043c \u0440\u0430\u0434\u0438\u043e \u0438 \u041e\u041e\u041d (\u0444\u0430\u0439\u043b \u0441\u043f\u043b\u0438\u0442 2021) \u2013 \u043a\u0430\u043a \u043e\u043f\u0442\u0438\u043c\u0430\u043b\u044c\u043d\u043e \u043f\u043e \u0434\u0440\u0443\u0433\u0438\u043c \u043c\u0435\u0434\u0438\u0430 \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u0431\u044e\u0434\u0436\u0435\u0442 \u0438 \u043d\u0430\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043c\u0435\u043d\u044c\u0448\u0435 \u0431\u0443\u0434\u0435\u0442 \u0437\u0430\u044f\u0432\u043e\u043a?",
      //     "tags": "#\u043d\u0430 #\u043f\u043e #\u2013 #\u0441\u043f\u043b\u0438\u0442 #\u0431\u044e\u0434\u0436\u0435\u0442",
      //     "priority": "2"},
      //   {"id": 3,
      //     "date": "Sat, 28 Nov 2020 11:07:08 +0300",
      //     "mail": "andrey.kaverin.89@mail.ru",
      //     "subject": "Re: Hello hello",
      //     "text": "НОВЫЙ ТЕКСТ \u041c\u0430\u0440\u0438\u043d\u0430, \u043f\u0440\u0438\u0432\u0435\u0442!\n\u042f \u043f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u043b\u0430 \u043f\u043e \u0444\u0430\u0439\u043b\u0443 \u043e\u043f\u0442. \u0441\u043f\u043b\u0438\u0442 \u043d\u0430 \u043d\u0430\u0448 \u0431\u044e\u0434\u0436\u0435\u0442 2021, \u0435\u0441\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441\u044b:\n- \u043f\u043e \u043e\u043f\u0446\u0438\u0438, \u043a\u043e\u0442. \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u0442 \u043c\u043e\u0434\u0435\u043b\u044c \u2013 \u043f\u043e\u0447\u0435\u043c\u0443 \u0442\u0430\u043a \u043c\u0430\u043b\u043e \u043e\u0442 \u043f\u0435\u0440\u0444\u043e\u043c\u0430\u043d\u0441\u0430 \u0437\u0430\u043a\u0430\u0437\u043e\u0432? \u042d\u0442\u043e \u0435\u0434\u0438\u043d\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u043a\u0430\u043d\u0430\u043b, \u043d\u0430\u043f\u0440\u044f\u043c\u0443\u044e \u043d\u0430 \u043d\u0438\u0445 \u0440\u0430\u0431\u043e\u0442\u0430\u044e\u0449\u0438\u0439.\n- \u0443 \u043d\u0430\u0441 \u0443\u0447\u0438\u0442\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f \u043d\u0430 \u0435\u043c\u043a\u043e\u0441\u0442\u044c \u043d\u0430 \u043f\u0435\u0440\u0444. \u043a\u0430\u043d\u0430\u043b\u043e\u0432? \u041a\u0430\u043a\u0438\u0435?\n- \u043c\u043e\u0436\u043d\u043e \u043b\u0438 \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0440\u0430\u0441\u0447\u0435\u0442 \u2013 \u0434\u043b\u044f \u0435\u0449\u0435 2\u0445 \u0441\u043f\u043b\u0438\u0442\u043e\u0432 \u0441 \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u0438\u0435\u043c \u0440\u0430\u0434\u0438\u043e \u0438 \u041e\u041e\u041d (\u0444\u0430\u0439\u043b \u0441\u043f\u043b\u0438\u0442 2021) \u2013 \u043a\u0430\u043a \u043e\u043f\u0442\u0438\u043c\u0430\u043b\u044c\u043d\u043e \u043f\u043e \u0434\u0440\u0443\u0433\u0438\u043c \u043c\u0435\u0434\u0438\u0430 \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u0431\u044e\u0434\u0436\u0435\u0442 \u0438 \u043d\u0430\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043c\u0435\u043d\u044c\u0448\u0435 \u0431\u0443\u0434\u0435\u0442 \u0437\u0430\u044f\u0432\u043e\u043a?\n\u00a0\n\u00a0\n\u00a0\n\u00a0\n\u00a0 \n>\u0427\u0435\u0442\u0432\u0435\u0440\u0433, 26 \u043d\u043e\u044f\u0431\u0440\u044f 2020, 23:22 +03:00 \u043e\u0442 adva.mailer.pub@gmail.com:\n>\u00a0\n>Hello World",
      //     "short_text": "НОВЫЙ ТЕКСТ \u0441\u043f\u043b\u0438\u0442 \u043d\u0430 \u043d\u0430\u0448 \u0431\u044e\u0434\u0436\u0435\u0442 2021, \u0435\u0441\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441\u044b:\n- \u043c\u043e\u0436\u043d\u043e \u043b\u0438 \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0440\u0430\u0441\u0447\u0435\u0442 \u2013 \u0434\u043b\u044f \u0435\u0449\u0435 2\u0445 \u0441\u043f\u043b\u0438\u0442\u043e\u0432 \u0441 \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u0438\u0435\u043c \u0440\u0430\u0434\u0438\u043e \u0438 \u041e\u041e\u041d (\u0444\u0430\u0439\u043b \u0441\u043f\u043b\u0438\u0442 2021) \u2013 \u043a\u0430\u043a \u043e\u043f\u0442\u0438\u043c\u0430\u043b\u044c\u043d\u043e \u043f\u043e \u0434\u0440\u0443\u0433\u0438\u043c \u043c\u0435\u0434\u0438\u0430 \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u0431\u044e\u0434\u0436\u0435\u0442 \u0438 \u043d\u0430\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043c\u0435\u043d\u044c\u0448\u0435 \u0431\u0443\u0434\u0435\u0442 \u0437\u0430\u044f\u0432\u043e\u043a?",
      //     "tags": "#\u043d\u0430 #\u043f\u043e #\u2013 #\u0441\u043f\u043b\u0438\u0442 #\u0431\u044e\u0434\u0436\u0435\u0442",
      //     "priority": "2"}]
      // this.mails = res;
      // console.log("this.mails");
      // console.log(this.mails);
      // this.id = res[0].id;
      // this.index = 0;
      // this.mail = this.mails[this.index];
      // console.log("first this.mail");
      // console.log(this.mail);

    },
    getDate: function (date) {
      let index = date.indexOf(" ");
      let index2 = date.indexOf(" ", index+4);
      return date.substring(index, index2+1)
    },
    showText: function () {
        this.fullText = !this.fullText;
    },
    selectAnswer: function(value) {
      document.getElementById('input_answer').value = value;
      this.input = value;
    },
    range: function(start, end) {
        let ans = [];
        for (let i = start; i <= end; i++) {
          ans.push(i);
        }
        return ans;
    },
    goHome() {
      this.$router.push({ name: "Main" });
    },
    showForward() {
      this.forward = !this.forward;
    },
    nextMail: function() {
      if (this.index<this.mails.length-1) {
        this.index++;
        this.id = this.mails[this.index].id;
        this.mail = this.mails[this.index];
      }
      else if (this.priority<3) {
        this.priority = this.priority+1;
        const new_url = url+'/mails/'+this.priority;
        axios
                .get(new_url)
                .then(response => {
                  if (response.data.length){
                    this.mails = response.data;
                    this.id = response.data[0].id;
                    this.index = 0;
                    this.mail = this.mails[this.index];
                  }
                  else {
                    this.$router.push({name:"Main"});
                  }
                })
                .catch(error => {
                  console.log(error);
                  this.$router.push({name:"Main"});
                });
      }
      else {
        this.$router.push({name:"Main"});
      }
    },
      getForwardList: function(id) {
          const new_url = url+'/forwardList/'+id;
          axios
              .get(new_url)
              .then(response => {
                    return response.data;
              })
              .catch(error => {
                  console.log(error);
              });
          let res = ["Matvey Orlov","Petr Filatov","Irina Smirnova","Igor Makaronkin","Nikolay Sokolov"]
          return res
      },
    seeAgain(id) {
      const new_url = url+'/unsee/'+id;
      axios
              .post(new_url)
              .then(response => {
              })
              .catch(error => {
                console.log(error);
              });
    },
    changeId(value) {
      this.id = value;
    },
    getTags: function(tags) {
      return tags.split(/[ ,]+/)
    },
    getVoice(id) {
      //todo: запрос на text to voice
      // const new_url = url+'/voice/'+id;
      // axios
      //         .get(new_url, {headers: {
      //             'Transfer-Encoding': 'chunked',
      //             'Content-Type': 'audio/mp4'
      //           }})
      //         .then(response => {
      //           this.play(response.data);F
      //         })
      //         .catch(error => {
      //           console.log(error);
      //         });
      // this.play();
      // var audio = new Audio(); // Создаём новый элемент Audio
      // audio.src = 'click.mp3'; // Указываем путь к звуку "клика"
      // audio.autoplay = true; // Автоматически запускаем
    },
    reply(mail) {
      console.log('trying reply');
      if (this.input !== "") {
        const new_url = url+'/send/';
        axios({
          method: 'post',
          url: new_url,
          data: {'to_addrs': mail["mail"], 'subject': mail.subject, 'text': this.input}
        })
                .then(response => {
                    document.getElementById("input_answer").value = "";
                    this.nextMail();
                })
                .catch(error => {
                  console.log(error);
                });
          document.getElementById("input_answer").value = "";
          this.input = "";
          this.nextMail();
      }
    },
    play: function (data) {
    let audio = new Audio("");
    audio.play();
  },
      addForward(name, id) {
        // console.log(this.forwardList);
        // if (this.forwardList.includes( name )) {
        //     let ind = this.forwardList;
        //     this.forwardList = this.forwardList.splice(ind, 1);
        //     console.log(this.forwardList);
        //   }
        // else {
        //     this.forwardList.push(name);
        //     console.log(this.forwardList);
        // }
          if (document.getElementById('user_'+id).classList.contains("selected")) {
              document.getElementById('user_'+id).classList.remove('selected');
          }
          else {
              document.getElementById('user_'+id).classList.add('selected');
          }

      },
    closeForward() {
      this.forward = false;
    },
    getMicrophone: function () {

    }
  },
  computed: {},
  mounted() {
    this.onMount();
  },
  watch:{
    id: function () {
      this.getMail(this.id);
    }
  }
};
</script>

<style scoped lang="scss">
.story {
  width: 100%;
  height: 100%;
  position: relative;
  padding: 15px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  .rects {
    display: flex;
    flex-direction: row;
    margin-bottom: 15px;
    .rect {
      height: 3px;
      margin-left: 2px;
      border-radius: 3px;
      &.active {
        background: $green;
      }
      &.inactive {
        background: $grey;
      }
    }
  }
  .mail {
    overflow-y: auto;
    height: 530px;
    position: relative;
      box-sizing: border-box;
      overflow-x: hidden;
    .sender {
      display: flex;
      flex-direction: row;
      margin-bottom: 10px;
      img {
        width: 26px;
        height: 26px;
      }
      span {
        margin-top: 0;
        font-family: Roboto Bold;
        color: $blue_dark;
        background: $white_dark1;
        border-radius: 13px;
        padding-right: 15px;
        padding-top: 3px;
        padding-bottom: 3px;
        padding-left: 5px;
        font-size: 18px;
      }
    }
    .date {
      font-size: 15px;
      color: $grey;
      position: absolute;
      top: 33px;
      right: 15px;
    }
    .tag {
      background: $white_dark1;
      color: $grey;
      display: inline-block;
      padding: 2px;
      border-radius: 3px;
      margin-right: 5px;
      margin-bottom: 5px;
    }
    .subject {
      margin-bottom: 6px;
    }
    .text {
      color: $grey;
      margin-bottom: 20px;
    }
    .click {
      position: absolute;
      width: 150px;
      height: 400px;
      right: -20px;
      bottom: 0;
    }
  }
  .more {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    img {
      width: 23px;
      margin-right: 20px;
    }
  }
  input {
    width: 100%;
    height: 30px;
    border: 1px solid $grey;
    font-size: 16px;
    margin-bottom: 15px;
    border-radius: 4px;
  }
  .answers {
    width: 100%;
    margin-bottom: 10px;
    .answer {
      display: inline-block;
      margin-right: 5px;
      margin-bottom: 5px;
    background: $white_dark2;
      padding-left: 10px;
      padding-right: 10px;
      padding-bottom: 3px;
      padding-top: 3px;
      border-radius: 10px;
     color: $blue_dark;
    }
  }
  .menu {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    .back {
      width: 25px;
      height: 23px;
      display: flex;
      justify-content: center;
      align-items: center;
      background: none;
      border: none;
      img {
        width: 25px;
        height: 23px;
      }
    }
    .helper {
      display: flex;
      flex-direction: row;
      .forward {
        width: 26px;
        height: 26px;
        display: flex;
        justify-content: center;
        align-items: center;
        background: none;
        border: none;
        margin-right: 15px;
        img {
          width: 26px;
          height: 26px;
        }
      }
      .unsee {
        width: 26px;
        height: 26px;
        display: flex;
        justify-content: center;
        align-items: center;
        background: none;
        border: none;
        margin-right: 15px;
        img {
          width: 26px;
          height: 26px;
        }
      }
      .voice {
        width: 28px;
        height: 26px;
        display: flex;
        justify-content: center;
        align-items: center;
        background: none;
        border: none;
        margin-right: 15px;
        img {
          width: 28px;
          height: 26px;
        }
      }
      .micro {
        width: 26px;
        height: 26px;
        display: flex;
        justify-content: center;
        align-items: center;
        background: none;
        border: none;
        margin-right: 15px;
        img {
          width: 26px;
          height: 26px;
        }
      }
      .reply {
        width: 28px;
        height: 23px;
        display: flex;
        justify-content: center;
        align-items: center;
        background: none;
        border: none;
        img {
          width: 32px;
          height: 26px;
        }
      }
    }
  }
  .forwardWindow {
    position: absolute;
    height: calc(100% - 50px);
    width: 100%;
    margin: 0;
    top: 0;
    left: 0;
    box-sizing: border-box;
    .shadow {
      background: rgba(34, 40, 46, 0.8);
      width: 100%;
      height: 100%;
      position: absolute;
      top: 0;
      left: 0;
      box-sizing: border-box;
    }
      .forward {
          position: absolute;
          background: $white;
          bottom: 25px;
          width: 325px;
          height: 170px;
          margin-left: 15px;
          display: flex;
          flex-direction: column;
          padding: 10px;
          .item {
              display: flex;
              color: $blue_dark;
              margin-bottom: 5px;
              span {
                  font-family: Roboto Bold;
                  margin-bottom: 5px;
                  background: $white_dark2;
                  padding-right: 15px;
                  padding-bottom: 3px;
                  padding-top: 3px;
                  padding-left: 5px;
                  border-radius: 13px;
              }
              img {

              }
              &.selected {
                  color: $green;
              }
          }
      }
  }
}
</style>
