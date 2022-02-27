<template>
  <div class="settings__main">
    <div class="settings__container">
      <!-- <button class="settings__btn" @click="notify('Installing...', 'loop')">Install vim-plug</button> -->
    </div>
    <div class="settings__container">
      <h1>world</h1>
    </div>
  </div>
  <notify :type="typein" />
</template>

<script>
import notify from "../components/notify.vue";

export default {
  data() {
    return {
      typein: 'done',
    }
  },
  methods: {
    async notify(message, icon) {
      if (icon == 'done') {
        this.typein = 'done';
      } else if (icon == 'error') {
        this.typein = 'error';
      } else if (icon == 'loop') {
        this.typein = 'loop'
      } else if (icon == 'wifinot') {
        this.typein = 'wifinot'
      }

      document.getElementById('notify-container-message').innerText = message;
      let elem = document.getElementById('notify-container').style;
      elem.display = "flex";

      setTimeout(() => {
        elem.opacity = '1';
        elem.transform = "translateX(0%)";
      }, 100)
      setTimeout(() => {
        elem.opacity = '0';
        elem.transform = "translateX(-20%)";
      }, 2000)
      setTimeout(() => {
        elem.display = "none";
      }, 2400)
    }
  },
  components: {
    notify
  }
}
</script>

<style lang="scss" scoped>
body {
  margin: 0;
  font-family: "Ubuntu", sans-serif;
  background-color: #131313;
}

.settings__main {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.settings__container {
  width: 30%;
  display: flex;
  justify-content: center;
  margin: 10px 10px;
  background-color: #3d3d3d;
  border-radius: 13px;
  color: white;
  opacity: 0;
  padding: 10px;
  transform: translateY(-100%);
  animation: load3 1s forwards;
}

.settings__btn {
  cursor: pointer;
  width: 80%;
  padding: 5px;
  background: transparent;
  border: 3px solid #b6b6b6;
  color: #b6b6b6;
  border-radius: 5px;
  font-size: 1.5rem;
  transition: 0.1s ease-in;
}

.settings__btn:hover {
  border: 3px solid #dddddd;
  color: #dddddd;
}
</style>