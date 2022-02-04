<template>
  <Notify :title="'hello'" :type="typein" />
  <div class="settings-main">
    <div class="settings-wrapper">
      <div class="container">
        <btn1 :title="'POST to flask server'" @click="postflask()" />
        <btn1 :title="'GET to flask server'" @click="getflask()" />
        <!-- <btn1 :title="''" />
        <btn1 :title="''" />
        <btn1 :title="''" /> -->
      </div>
    </div>
    <div class="settings-wrapper">
      <div class="container">
        <div class="settings-container2">
          <h1>Config</h1>
          <textarea name="" id="cfg" cols="30" rows="10" ></textarea>
          <!-- textarea => config.vim -->
        </div> 
        <btn1 :title="'Save and update'" />
      </div>
    </div>
  </div>
</template>

<script>
import btn1 from "../components/btn1.vue";
import Notify from "../components/notify.vue"

export default {
  components: {
    btn1,
    Notify
  },
  data() {
    return {
      typein: 'done'
    };
  },
  methods: {
    showstatus(message, type) {
      let elem = document.getElementById('settings-notifier-js').style;
      document.getElementById('settings-notifier-js-message').innerText = message;

      if (type == 'done') {
        this.typein = 'done';
      } else if (type == 'error') {
        this.typein = 'error';
      } else if (type == 'code') {
        this.typein = 'code'
      }

      elem.opacity = '1';
      elem.transform = "translateX(0%)";
      setTimeout(() => {
        elem.opacity = '0';
        elem.transform = "translateX(20%)";
      }, 2000)
    },
    getflask() {
      var client = new XMLHttpRequest();
      client.open("GET", "http://127.0.0.1:5000/test", false);
      client.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
      client.send(null);
      this.showstatus("Sended!", 'done');
      document.getElementById('cfg').innerText = client.responseText;
    },
    postflask() {
      fetch('http://localhost:5000/config/change?type=vim', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin' : '*',
        },
        body: JSON.stringify(document.getElementById('cfg').value),
      })
      .then(response => response.json())
      .then(data => {
        console.log('success: ', data)
      })
      .catch((error) => {
        console.error('Error:', error);
      });
    }
  },
};
</script>

<style lang="scss">
.settings-main {
  width: 100%;
  height: 100%;
  display: flex;
  margin-top: 10px;
}

.settings-wrapper {
  width: 30%;
  height: 70%;
  border-radius: 5px;
  margin-left: auto;
  margin-right: auto;
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
