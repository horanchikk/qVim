<template>
  <div class="notify-container" id='notify-container'>
    <div class="notify-container-icon" :class="setIcon(type)">

      <img v-if="type === 'done'" src="../assets/img/done.svg" alt="done" />
      <img v-if="type === 'error'" src="../assets/img/error.svg" alt="error" />
      <img v-if="type === 'loop'" src="../assets/img/loop.svg" alt="loop" />
      <img v-if="type === 'wifinot'" src="../assets/img/wifinot.svg" alt="wifinot" />
    
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
  min-height: 5%;
  max-width: 17%;
  display: flex; 
  flex-direction: row;
  padding: 20px;
  opacity: 0;
  border-bottom-right-radius: 5px;
  border-top-right-radius: 5px;
  background: rgba(61, 61, 61, 0.5);
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

.notify-container-message a {
  padding: 7px;
}

</style>