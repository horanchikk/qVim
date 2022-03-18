<template>
  <div></div>
  <progressbar :icon="debico" />
  <notify :type="typein" />
</template>

<script>
import progressbar from "../components/progressbar.vue";
import { utils } from "../components/mixins/global.js";
import notify from "../components/notify";

export default {
  data() {
    return {
      debico: "",
      typein: "",
    };
  },
  components: {
    notify,
    progressbar,
  },
  mixins: [utils],
};
</script>

<style lang="scss" scoped></style>
