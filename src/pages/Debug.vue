<template>
  {{ isShowing }}

  <alert-window :isShowing="isShowing" @alertres="alertres" />

  <div style="margin-top: 30px">
    <h1 style="color: white">Page work</h1>
    <button
      class="px-3 py-1 bg-blue-500 ml-2 rounded-md"
      @click="alertres(true)"
    >
      open
    </button>

    <button
      class="px-3 py-1 bg-red-500 ml-2 rounded-md"
      @click="alertres(false)"
    >
      close
    </button>
  </div>
</template>

<script>
import alertWindow from "../components/alertWindow.vue";
import { animations } from "../components/mixins/global";

export default {
  components: {
    alertWindow,
  },
  data() {
    return {
      isShowing: false,
    };
  },
  methods: {
    alertres(status) {
      this.isShowing = status;
    },
  },
  mixins: [animations],
};
</script>

<style lang="scss" scoped></style>
