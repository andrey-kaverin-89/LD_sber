import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);
Vue.config.devtools = true;
export default new Vuex.Store({
  state: {
    token: "",
    currentNav: "",
    currentPage: "Main",
    associationsWord: String,
    associationsRows: Array,
    searchWord: String,
    searchTexts: Array,
    widthParameters: 600,
    response: Object,
    fakeFileInput: {
      info: false, //false - файла нет, true - файл есть
      name: String,
      value: Object,
      html: Object
    },
    formInputData: {
      info: false, //false - данных нет, true - данные есть
      data: {
        file: Object,
        columnName: String,
        topicsAmount: Number,
        removeWords: Number,
        removePosts: Number,
        bigrams: false,
        ldaPasses: Number,
        saveTokens: Number,
        tokenProportion: Number
      }
    }
  },
  actions: {
    updateToken({ commit }, token) {
      commit("UPDATE_TOKEN", token);
    },
    updateCurrentNav({ commit }, currentNav) {
      commit("UPDATE_CURRENT_NAV", currentNav);
    },
    updateCurrentPage({ commit }, currentPage) {
      commit("UPDATE_CURRENT_PAGE", currentPage);
    },
    updateWidthParameters({ commit }, widthParameters) {
      commit("UPDATE_WIDTH_PARAMETERS", widthParameters);
    },
    updateResponse({ commit }, response) {
      commit("UPDATE_RESPONSE", response);
    },
    updateFakeFileInputInfo({ commit }, value) {
      commit("UPDATE_FAKE_FILE_INPUT_INFO", value);
    },
    updateFakeFileInputName({ commit }, name) {
      commit("UPDATE_FAKE_FILE_INPUT_NAME", name);
    },
    updateFakeFileInputValue({ commit }, value) {
      commit("UPDATE_FAKE_FILE_INPUT_VALUE", value);
    },
    updateFakeFileInputHTML({ commit }, value) {
      commit("UPDATE_FAKE_FILE_INPUT_HTML", value);
    },
    updateAssociationsWord({ commit }, word) {
      commit("UPDATE_ASSOCIATIONS_WORD", word);
    },
    updateAssociationsRows({ commit }, rows) {
      commit("UPDATE_ASSOCIATIONS_ROWS", rows);
    },
    updateSearchWord({ commit }, word) {
      commit("UPDATE_SEARCH_WORD", word);
    },
    updateSearchTexts({ commit }, texts) {
      commit("UPDATE_SEARCH_TEXTS", texts);
    },
    updateFormInputData({ commit }, formInputData) {
      commit("UPDATE_FORM_INPUT_DATA", formInputData);
    },
    updateFIDInfo({ commit }, value) {
      // FID = FormInputData
      commit("UPDATE_FID_INFO", value);
    },
    updateFIDFile({ commit }, file) {
      commit("UPDATE_FID_FILE", file);
    },
    updateFIDColumnName({ commit }, name) {
      commit("UPDATE_FID_COLUMN_NAME", name);
    },
    updateFIDTopicsAmount({ commit }, amount) {
      commit("UPDATE_FID_TOPICS_AMOUNT", amount);
    },
    updateFIDRemoveWords({ commit }, amount) {
      commit("UPDATE_FID_REMOVE_WORDS", amount);
    },
    updateFIDRemovePosts({ commit }, amount) {
      commit("UPDATE_FID_REMOVE_POSTS", amount);
    },
    updateFIDBigrams({ commit }, value) {
      commit("UPDATE_FID_BIGRAMS", value);
    },
    updateFIDLdaPasses({ commit }, amount) {
      commit("UPDATE_FID_LDA_PASSES", amount);
    },
    updateFIDSaveTokens({ commit }, amount) {
      commit("UPDATE_FID_SAVE_TOKENS", amount);
    },
    updateFIDTokenProportion({ commit }, amount) {
      commit("UPDATE_FID_TOKEN_PROPORTION", amount);
    }
  },
  mutations: {
    UPDATE_TOKEN(state, token) {
      state.token = token;
    },
    UPDATE_CURRENT_NAV(state, currentNav) {
      state.currentNav = currentNav;
    },
    UPDATE_CURRENT_PAGE(state, currentPage) {
      state.currentPage = currentPage;
    },
    UPDATE_WIDTH_PARAMETERS(state, widthParameters) {
      state.widthParameters = widthParameters;
    },
    UPDATE_RESPONSE(state, response) {
      state.response = response;
    },
    UPDATE_FAKE_FILE_INPUT_INFO(state, value) {
      state.fakeFileInput.info = value;
    },
    UPDATE_FAKE_FILE_INPUT_NAME(state, name) {
      state.fakeFileInput.name = name;
    },
    UPDATE_FAKE_FILE_INPUT_VALUE(state, value) {
      state.fakeFileInput.value = value;
    },
    UPDATE_FAKE_FILE_INPUT_HTML(state, value) {
      state.fakeFileInput.html = value;
    },
    UPDATE_ASSOCIATIONS_WORD(state, word) {
      state.associationsWord = word;
    },
    UPDATE_ASSOCIATIONS_ROWS(state, rows) {
      state.associationsRows = rows;
    },
    UPDATE_SEARCH_WORD(state, word) {
      state.searchWord = word;
    },
    UPDATE_SEARCH_TEXTS(state, texts) {
      state.searchTexts = texts;
    },
    UPDATE_FORM_INPUT_DATA(state, formInputData) {
      state.formInputData = formInputData;
    },
    UPDATE_FID_INFO(state, value) {
      state.formInputData.info = value;
    },
    UPDATE_FID_FILE(state, file) {
      state.formInputData.data.file = file;
    },
    UPDATE_FID_COLUMN_NAME(state, name) {
      state.formInputData.data.columnName = name;
    },
    UPDATE_FID_TOPICS_AMOUNT(state, amount) {
      state.formInputData.data.topicsAmount = amount;
    },
    UPDATE_FID_REMOVE_WORDS(state, amount) {
      state.formInputData.data.removeWords = amount;
    },
    UPDATE_FID_REMOVE_POSTS(state, amount) {
      state.formInputData.data.removePosts = amount;
    },
    UPDATE_FID_BIGRAMS(state, value) {
      state.formInputData.data.bigrams = value;
    },
    UPDATE_FID_LDA_PASSES(state, amount) {
      state.formInputData.data.ldaPasses = amount;
    },
    UPDATE_FID_SAVE_TOKENS(state, amount) {
      state.formInputData.data.saveTokens = amount;
    },
    UPDATE_FID_TOKEN_PROPORTION(state, amount) {
      state.formInputData.data.tokenProportion = amount;
    }
  },
  getters: {
    token(state) {
      return state.token;
    },
    currentNav(state) {
      return state.currentNav;
    },
    currentPage(state) {
      return state.currentPage;
    },
    widthParameters(state) {
      return state.widthParameters;
    },
    response(state) {
      return state.response;
    },
    fakeFileInput(state) {
      return state.fakeFileInput;
    },
    associationsWord(state) {
      return state.associationsWord;
    },
    associationsRows(state) {
      return state.associationsRows;
    },
    searchWord(state) {
      return state.searchWord;
    },
    searchTexts(state) {
      return state.searchTexts;
    },
    formInputData(state) {
      return state.formInputData;
    },
    fidInfo(state) {
      return state.formInputData.info;
    },
    fidFile(state) {
      return state.formInputData.data.file;
    },
    fidColumnName(state) {
      return state.formInputData.data.columnName;
    },
    fidTopicsAmount(state) {
      return state.formInputData.data.topicsAmount;
    },
    fidRemoveWords(state) {
      return state.formInputData.data.removeWords;
    },
    fidRemovePosts(state) {
      return state.formInputData.data.removePosts;
    },
    fidBigrams(state) {
      return state.formInputData.data.bigrams;
    },
    fidLdaPasses(state) {
      return state.formInputData.data.ldaPasses;
    },
    fidSaveTokens(state) {
      return state.formInputData.data.saveTokens;
    },
    fidTokenProportion(state) {
      return state.formInputData.data.tokenProportion;
    }
  },
  modules: {}
});
