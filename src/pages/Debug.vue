<template>
  <alert-window
    :alertShowing="alertShowing"
    :alertTitle="this.title"
    :alertDescription="this.description"
    @alertres="alertres"
  />
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
      <h4>alertShowing state: {{ alertShowing }}</h4>
    </div>
  </div>
</template>

<script>
import alertWindow from "../components/alertWindow.vue";
import mainBtn from "../components/mainBtn.vue";
import { animations } from "../components/mixins/global";

export default {
  components: {
    alertWindow,
    mainBtn,
  },
  data() {
    return {
      alertShowing: false,
      title: "",
      description: "",
    };
  },
  methods: {
    alertres(status) {
      this.alertShowing = status;
    },
  },
  mixins: [animations],
};
</script>

<style lang="scss" scoped>
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
