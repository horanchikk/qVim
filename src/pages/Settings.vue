<template>
  <div class="settings-main">
    <div class="settings-wrapper">
      <div class="container">
        <btn1 :title="'POST to flask server'" @click="postflask()" />
        <btn1 :title="'GET to flask server'" @click="getflask()" />
      </div>
    </div>
    <div class="settings-wrapper">
      <div class="container">
        <div class="settings-container2">
          <h1>Config</h1>
          <textarea name="" id="cfg" cols="30" rows="10"></textarea>
          <!-- textarea => config.vim -->
        </div>
        <btn1 :title="'Save and update'" />
      </div>
    </div>
  </div>
  <Notify :title="'hello'" :type="typein" />
</template>

<script>
import btn1 from "../components/btn1.vue";
import Notify from "../components/notify.vue";

export default {
  components: {
    btn1,
    Notify,
  },
  data() {
    return {
      typein: "done",
    };
  },
  methods: {
    postflask() {
      fetch("http://localhost:5000/config/change?type=vim", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
        body: JSON.stringify(document.getElementById("cfg").value),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log("success: ", data);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
  },
};
</script>

<style lang="scss">
.settings-main {
  width: 60%;
  margin: 0 auto;
  height: 100%;
  display: flex;
  margin-top: 40px;
}

.settings-wrapper {
  width: 30%;
  height: 70%;
  background-color: #242424;
  border-radius: 13px;
  width: 50%;
  height: 100%;
  margin: 0 10px;
}

.settings-title {
  font-size: 40px;
  color: black;
  text-align: center;
}

.container {
  margin: 15px;
  border-radius: 5px;
  padding: 10px;
}

.settings-container2 {
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.7);
  border-radius: 5px;
  display: flex;
  flex-direction: column;

  h1 {
    text-align: center;
  }

  textarea {
    background: rgba(0, 0, 0, 0.5);
    color: white;
    resize: none;
  }
}
</style>
