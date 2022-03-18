<template>
  <alert-window
    :alertShowing="alertShowing"
    :alertTitle="this.title"
    :alertDescription="this.description"
    @alertres="alertres"
  />
  <div class="states">
    <h4>
      alertShowing state:
      <a style="color: rgb(200, 0, 0)" v-if="this.alertShowing === false">{{
        alertShowing
      }}</a
      ><a style="color: rgb(0, 200, 0)" v-else>{{ alertShowing }}</a>
    </h4>
    <h4>
      Editor:
      <a style="color: rgb(200, 0, 0)" v-if="this.editor === 'none'">{{
        editor
      }}</a
      ><a style="color: rgb(0, 200, 0)" v-else>{{ editor }}</a>
    </h4>
  </div>
  <div class="debugging">
    <div class="debugging__menu">
      <div class="menu__controls">
        <input
          type="text"
          class="debugging__input"
          placeholder="title"
          v-model="title"
        />
        <input
          type="text"
          class="debugging__input"
          placeholder="description"
          v-model="description"
        />
        <mainBtn @click="alertres(true)" :title="'open'"></mainBtn>
      </div>
    </div>
  </div>
  <div class="debugging">
    <div class="debugging__menu">
      <div class="menu__controls" style="justify-content: space-between">
        <mainBtn
          @click="editorcheck()"
          :title="'Update state of editor'"
          style="font-size: 15px; padding: 10px"
        ></mainBtn>
        <mainBtn
          @click="updplugin()"
          :title="'Update plugins in nvim/vim'"
          style="font-size: 15px; padding: 10px"
        ></mainBtn>
      </div>
    </div>
  </div>
  <notify :type="typein" />
  <progressbar :icon="debico" />
</template>

<script>
import alertWindow from "../components/alertWindow.vue";
import mainBtn from "../components/mainBtn.vue";
import progressbar from "../components/progressbar.vue";
import notify from "../components/notify";
import { utils } from "../components/mixins/global.js";

export default {
  components: {
    alertWindow,
    mainBtn,
    notify,
    progressbar,
  },
  mixins: [utils],
  data() {
    return {
      alertShowing: false,
      title: "",
      description: "",
      typein: "none",
      debico: "res",
      editor: "none",
    };
  },
  methods: {
    alertres(status) {
      this.alertShowing = status;
    },
  },
  async mounted() {
    this.debug();
  },
};
</script>

<style lang="scss" scoped>
.states {
  display: flex;
  justify-content: space-between;
  width: 30%;
  color: white;
  margin-left: 1rem;
}

.debugging {
  h4 {
    color: white;
    text-align: center;
  }
  input {
    width: 100%;
    border: 0;
    background: none;
    height: 50%;
    text-align: center;
    font-size: 15px;
    transition: 0.3s ease-in;
    color: white;
    margin-right: 10px;
    border: 0.15rem solid rgb(170, 170, 170);
    border-radius: 3px;
    padding: 5px;
    &::placeholder {
      color: white;
      transition: 0.3s ease-in;
    }
    &:focus {
      color: black;
      outline: 0;
      background: rgba(195, 195, 195, 1);
    }
    &:focus::placeholder {
      color: black;
    }
  }
}

.debugging__menu {
  margin: 1em;
  padding: 1em;
  width: 40%;
  border-radius: 5px;
  background-color: rgba(80, 80, 80, 0.7);
}
.menu__controls {
  display: flex;
  justify-content: center;
}

.customBtn {
  font-size: 15px;
  padding: 5px;
}
</style>
