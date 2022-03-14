<template>
  <div
    v-if="isShowing"
    class="p-3 fixed bottom-3 right-3 border-2 border-black rounded-md"
  >
    <span>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias
    </span>
    <hr class="w-full hg-1 bg-black my-2" />
    <div class="flex justify-end">
      <button class="px-3 py-1 bg-red-500 ml-2 rounded-md">close</button>
      <button
        class="px-3 py-1 bg-blue-500 ml-2 rounded-md"
        @click="$emit('alertres', true)"
      >
        open?
      </button>
    </div>
  </div>
</template>

<script>
export default {
  emits: ["alertres"],
  props: {
    isShowing: Boolean,
  },
};
</script>

<style scoped>
hr {
  height: 2px;
}
</style>

// awpdolfmwoaf

<template>
  {{ isShowing }}

  <alert-window :isShowing="isShowing" @alertres="alertres" />

  <button class="px-3 py-1 bg-blue-500 ml-2 rounded-md" @click="alertres(true)">
    open
  </button>

  <button class="px-3 py-1 bg-red-500 ml-2 rounded-md" @click="alertres(false)">
    close
  </button>
</template>

<script>
import AlertWindow from "./components/AlertWindow.vue";

export default {
  components: {
    AlertWindow,
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
};
</script>

<style scoped></style>
