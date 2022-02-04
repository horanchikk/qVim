<template>
  <div class="settings-container">
    <button class="settings-container-btn" id="content-js">
      {{ title }}
    </button>
  </div>
</template>

<script>


export default {
  props: {
    title: {
      type: String,
    },
  },
};

</script>

<style>
.settings-container {
  display: flex;
  justify-content: center;
  margin: 5px;
  padding: 5px;
}

.settings-container-btn {
  padding: 5px;
  background: rgba(255, 255, 255, 0.35);
  border: 3px solid rgba(255, 255, 255, 0.35);
  border-radius: 5px;
  font-size: 1.5rem;
  transition: 0.1s ease-in;
}

.settings-container-btn:hover {
  border: 3px solid rgba(255, 255, 255, 0.7);
}
</style>