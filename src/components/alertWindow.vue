<template>
  <div v-if="isShowing" class="vim-alert-bg" id="vim-alert-bg">
    <div class="vim-alert-container" id="vim-alert-container">
      <h1 class="vim-alert-container-title">Warning!</h1>
      <h2 class="vim-alert-container-description">
        For the program to work correctly, you need to install vim-plug.
        Install?
      </h2>
      <li class="vim-alert-container-btns">
        <btn1 :title="'Yes'" @click="resTrue" />
        <btn1 :title="'No'" @click="resFalse" />
      </li>
    </div>
  </div>
</template>

<script>
import btn1 from "../components/btn1.vue";
import { animations } from "../components/mixins/global.js";

export default {
  props: {
    isShowing: {
      type: Boolean,
      required: true,
    },
  },
  components: {
    btn1,
  },
  methods: {
    resTrue() {
      this.$emit("alertres", true);
    },
    resFalse() {
      this.$emit("alertres", false);
    },
  },
  mixins: [animations],
};
</script>

<style lang="scss" scoped>
.vim-alert-bg {
  width: 100%;
  height: 100%;
  display: block;
  position: fixed;
  cursor: default;
  background-color: rgb(0 0 0 / 0.7);
  z-index: 1;
  transition: 0.6s ease-in-out;
}

.vim-alert-container {
  position: absolute;
  width: 400px;
  height: 300px;
  top: 50%;
  left: 50%;
  display: flex;
  flex-direction: column;
  transform: translate(-50%, -50%);
  background-color: rgb(50 50 50 / 1);
  color: whitesmoke;
  padding: 15px;
  border-radius: 13px;
  transition: 0.4s ease-in-out;
  border: yellow solid 1px;
}

.vim-alert-container-title {
  text-align: center;
}

.vim-alert-container-btns {
  display: flex;
  flex-direction: row;
  width: 100%;
}
</style>
