<template>
  <alert-window :isShowing="true" @alertres="alertres" />
  <div>
    <h1 style="color: white">Page work</h1>
  </div>
</template>

<script>
import alertWindow from "../components/alertWindow.vue";
import { animations } from "../components/mixins/global";
export default {
  data() {
    return {
      isShowing: false,
    };
  },
  components: {
    alertWindow,
  },
  methods: {
    alertres(status) {
      if (status === false) {
        // change isShowing prop to false, HOW?
      }
    },
  },
  mixins: [animations],
};
</script>

<style lang="scss" scoped></style>
