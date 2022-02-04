<template>
  <div class="settings-notifier" id="settings-notifier-js">
    <div class="settings-notifier-icon" :class="checkType(type)">
      <img v-if="type === 'done'" src="../assets/img/done.svg" alt="done" id="settings-notifier-icon-js" />
      <img v-if="type === 'error'" src="../assets/img/error.svg" alt="error" id="settings-notifier-icon-js" />
      <img v-if="type === 'code'" src="../assets/img/code.svg" alt="code" id="settings-notifier-icon-js" />
    </div>
    <div class="settings-notifier-message" id="settings-notifier-js-message" >
      <a></a>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    type: {
      type: String,
      required: true
    }
  },
  methods: {
    checkType(type) {
      return type;
    }
  }
};
</script>

<style>

.settings-notifier {
  position: absolute;
  width: 20%;
  display: flex;
  margin-left: 70%;
  margin-top: 35%;
  opacity: 0;
  border-radius: 3px;
  transform: translateX(20%);
  background: linear-gradient(90deg, rgba(10, 10, 10, 0.7) 0%, rgba(10, 10, 10 ,0.7) 0%, rgba(0, 0, 0, 0) 100%);
  transition: .4s ease-in-out;
}

.settings-notifier-icon {width: 10%; height: 100%; margin: 5px;}
.settings-notifier-message {width: 90%; height: 100%; margin: 3px; color: white;}

</style>