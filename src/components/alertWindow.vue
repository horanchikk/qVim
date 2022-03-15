<template>
  <Transition name="fade">
    <main v-if="alertShowing" class="alertWindow">
      <section class="alertwindow__cont">
        <h2>{{ alertTitle }}</h2>
        <h1>{{ alertDescription }}</h1>
        <div class="alertwindow__btns">
          <btn1 :title="'Yes'" @click="$emit('alertres', true)" />
          <btn1 :title="'No'" @click="$emit('alertres', false)" />
        </div>
      </section>
    </main>
  </Transition>
</template>

<script>
//
//
//     Using component alertWindow in your project
//
// -- Copy it to <template> --
//
// <alert-window
//     :alertShowing="alertShowing"
//     :alertTitle="this.title"
//     :alertDescription="this.description"
//     @alertres="alertres"
//   />
//
// -- This in <script> --
//
// import alertWindow from "../components/alertWindow.vue";
//
// export default {
//  data() {
//    return {
//       alertShowing: false,
//       title: "",
//       description: "",
//    };
//  },
//  methods: {
//   alertres(status) {
//     this.alertShowing = status;
//   },
// },
//
//     How to change state of showing alertWindow?
//
//  In component: <button @click="alertres(true|false)" />
//
//  In method: this.alertShowing = true|false;
//
//

import btn1 from "./mainBtn.vue";
export default {
  emits: ["alertres"],
  props: {
    alertTitle: String,
    alertDescription: String,
    alertShowing: Boolean,
  },
  data() {
    return {
      title: this.alertTitle,
      description: this.alertDescription,
    };
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
};
</script>

<style lang="scss" scoped>
// Set alertWindow style
.alertWindow {
  position: fixed;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.3);
}
.alertwindow__cont {
  // Centering block
  position: absolute;
  width: 350px;
  height: 180px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  // Styilng
  padding: 10px;
  border: 0.1rem solid yellow;
  background-color: rgba(50, 50, 50, 0.9);
  border-radius: 0.3rem;
  color: whitesmoke;
  text-align: center;
}
.alertwindow__btns {
  position: relative;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

// Set component style
.customBtn {
  width: 40%;
  padding: 0.35rem;
  font-size: 1.2rem;
}

// Vue transition
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease-in-out;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
