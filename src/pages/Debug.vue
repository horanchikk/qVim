<template>
  <alert-window
    :alertShowing="alertShowing"
    :alertTitle="this.title"
    :alertDescription="this.description"
    @alertres="alertres"
  />
  <div class="debugging">
    <div class="debugging__menu">
      <input type="text" class="debugging__input" placeholder="title" />
      <input type="text" class="debugging__input" placeholder="description" />
      <btn1 @click="alertres(true)" :title="'open'"></btn1>
    </div>
    <h4 style="color: white">alertShowing state: {{ alertShowing }}</h4>
    <h4>{{ typein }}</h4>
  </div>
</template>

<script>
import alertWindow from "../components/alertWindow.vue";
import Btn1 from "../components/mainBtn.vue";
import { animations } from "../components/mixins/global";

export default {
  components: {
    alertWindow,
    Btn1,
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
      this.typein = "error";
    },
  },
  created() {
    this.title = "Warning!";
    this.description =
      "For fully work qVim, you should to install vim-plug. Install it?";
  },
  mixins: [animations],
};
</script>

<style lang="scss" scoped>
.debugging {
  padding: 30px;
}
</style>
