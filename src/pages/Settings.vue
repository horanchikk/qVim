<template>
  <div class="settings__container"></div>
  <notify :type="typein" />
  <progressbar :icon="debico" />
  <btn1 />
</template>

<script>
import notify from "../components/notify.vue";
import btn1 from "../components/mainBtn.vue";
import progressbar from "../components/progressbar.vue";
import { utils } from "../components/mixins/global.js";

export default {
  data() {
    return {
      typein: "done",
      debico: "res",
      editor: "none",
    };
  },
  components: {
    notify,
    btn1,
    progressbar,
  },
  mixins: [utils],
};
</script>

<style lang="scss" scoped></style>
