<template>
  <div class="notify-container" id='notify-container'>
    <div class="notify-container-icon" :class="setIcon(type)">

      <img v-if="type === 'done'" src="../assets/img/done.svg" alt="done" id='notify-container-icon-done' />
      <img v-if="type === 'error'" src="../assets/img/error.svg" alt="error" id='notify-container-icon-error' />
      <img v-if="type === 'loop'" src="../assets/img/loop.svg" alt="loop" id='notify-container-icon-loop' />
      <img v-if="type === 'wifinot'" src="../assets/img/wifinot.svg" alt="wifinot" id='notify-container-icon-wifinot' />
    
    </div>
    <div class="notify-container-message" id="notify-container-message">
      <a>Notify example.</a>
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
    setIcon(type) {
      return type;
    }
  }
};
</script>

<style>

.notify-container {
  position: fixed;
  top: 7%;
  display: flex;
  flex-direction: row;
  opacity: 0;
  border-bottom-right-radius: 5px;
  border-top-right-radius: 5px;
  color: white;
  transform: translateX(-20%);
  transition: 0.2s ease-in-out;
}

.notify-container-icon {
  display: flex;
  justify-content: center;
  align-items: center;
}

.notify-container-message {
  width: 80%;
  padding: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}

@media (max-width: 2000px) {
  .notify-container {
    padding: 6px;
    background: rgba(61, 61, 61, 0.5);
  }
}
@media (max-width: 700px) {
  /* mobile */
}

@media (max-width: 500px) {
  .notify-container {
    top: 0;
    padding-right: 100%;
    background: rgba(0,0,0, 0.7);
  }
  .notify-container-message {
    white-space: nowrap;
  }
}

</style>