<template>
  <alert-window
    :alertShowing="alertShowing"
    :alertTitle="this.title"
    :alertDescription="this.description"
    @alertres="alertres"
  />
  <div class="shop-container">
    <div class="shop__search">
      <input
        type="text"
        placeholder="Find plugin..."
        class="shop__search-input"
        :value="inputValue"
        @input="setInputValue($event.target.value)"
      />
    </div>

    <div class="shop_elem-wrapper">
      <template v-for="plugin in searchedPlugins">
        <div
          class="shop_elem"
          v-if="
            plugin.name.includes(inputValue) ||
            plugin.description.includes(inputValue)
          "
          :key="plugin"
        >
          <div class="shop_info">
            <div class="shop_info_container">
              <h1 class="shop_info_title">
                {{ plugin.name }}
              </h1>
              <h4 class="shop_info_description">{{ plugin.description }}</h4>
              <h5 class="shop_info_link">
                https://github.com{{ plugin.link }}
              </h5>
            </div>
          </div>
          <div
            class="shop_info_icon"
            v-if="this.debico === 'wait'"
            @click="instplugin(plugin.link, plugin.name)"
          >
            <a
              ><svg
                xmlns="http://www.w3.org/2000/svg"
                height="60px"
                viewBox="0 0 24 24"
                width="60px"
                class="shop_info_svg"
              >
                <path d="M0 0h24v24H0z" fill="none"></path>
                <path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"></path></svg
            ></a>
          </div>
        </div>
      </template>
    </div>
    <div class="j-center">
      <img src="../../public/loading.svg" class="shop_loader" v-if="loading" />
      <button
        v-else-if="!loading && currentPage <= pageLimit && internet === true"
        @click="getPlugins"
        class="shop_load-new-data"
      >
        Load more
      </button>
      <button
        v-else-if="!loading && currentPage <= pageLimit && internet === false"
        @click="reloadapp()"
        class="shop_load-new-data"
      >
        Reload application
      </button>
    </div>
    <progressbar :icon="debico" />
  </div>
  <notify :type="typein" />
</template>

<script>
import progressbar from "../components/progressbar.vue";
import { utils } from "../components/mixins/global.js";
import notify from "../components/notify.vue";
import alertWindow from "../components/alertWindow.vue";

export default {
  data() {
    return {
      plugins: [],
      currentPage: 1,
      loading: true,
      pageLimit: 16,
      searchedPlugins: [],
      inputValue: "",
      internet: true,
    };
  },
  components: {
    progressbar,
    notify,
    alertWindow,
  },
  mixins: [utils],
  methods: {
    setInputValue(value) {
      this.inputValue = value;
    },
    alertres(status) {
      this.alertShowing = status;
    },
  },
  async mounted() {
    this.getPlugins();
  },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Ubuntu&display=swap");

.shop-container {
  font-family: "Ubuntu", sans-serif;
  width: 100%;
}

.shop_elem-wrapper {
  width: 60%;
  display: flex;
  margin: 0 auto;
  flex-wrap: wrap;
  justify-content: center;
}

.shop_elem {
  position: relative;
  width: 47%;
  margin: 10px 10px;
  background-color: #3d3d3d;
  border-radius: 13px;
  color: white;
  opacity: 0;
  animation: load3 1s forwards;
  transition: 0.2s ease;
  &:hover {
    box-shadow: 0px 0px 10px whitesmoke;
  }
}

.shop__search {
  width: 96%;
  height: 10%;
  padding: 0px 15px 15px 15px;
  display: flex;
  flex-direction: row-reverse;
}

.shop__search-input {
  border: 0;
  background: #3d3d3d;
  text-align: center;
  font-size: 23px;
  border-radius: 5px;
  transition: 0.3s ease;
  color: white;
  outline: 0;
}

.shop__search-input:focus {
  box-shadow: 0px 0px 10px whitesmoke;
}

// .shop__search-input::placeholder {
//   color: white;
//   transition: 0.3s ease-in;
// }

// .shop__search-input:focus {
//   color: black;
//   outline: 0;
//   background: rgba(195, 195, 195, 1);
// }

// .shop__search-input:focus::placeholder {
//   color: black;
// }

.shop_info {
  padding: 10px;
}
.shop_info_container {
  width: 70%;
  border-radius: 5px;
  padding: 10px;
}

.shop_info_title {
  margin-left: 5%;
  width: 65%;
  cursor: default;
}

.shop_info_description {
  width: 100%;
  cursor: default;
}

.shop_info_link {
  color: rgba(255, 255, 255, 0.3);
  height: 100%;
}

.shop_info_svg {
  fill: rgba(255, 255, 255, 0.7);
  transition: 0.3s ease-in-out;
  margin: 15%;
}

.shop_info_svg:hover {
  fill: rgba(255, 255, 255, 1);
  cursor: pointer;
}

.shop_info_icon {
  position: absolute;
  margin-left: 80%;
  bottom: 30%;
}

.shop_info_icon > h1 {
  position: absolute;
  top: 50%;
  text-align: center;
  margin-left: 30px;
}

.shop_menu {
  position: fixed;
  width: 10%;
  height: auto;
  display: flex;
  flex-direction: column;
  top: 35%;
  padding-bottom: 10px;
  border-bottom-right-radius: 5px;
  border-top-right-radius: 5px;
  background-color: #3d3d3d;
  transform: translateX(-100%);
  animation: load2 1s forwards;
}

@keyframes load2 {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(0%);
  }
}

.elem_menu {
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  margin-right: 15px;
  margin-top: 10px;
  background-color: rgba(238, 238, 238, 0.85);
  border-bottom-right-radius: 5px;
  border-top-right-radius: 5px;
  list-style-type: none;
  transition: 0.2s ease-in-out;
  transform: translateX(-100%);
  animation: load2 2s forwards;
}

.elem_menu:hover {
  background-color: rgb(238, 238, 238);
  margin-right: 3px;
}

@keyframes load3 {
  0% {
    transform: translateY(-100%);
  }
  60% {
    opacity: 0;
  }
  100% {
    opacity: 1;
    transform: translateY(0%);
  }
}

.j-center {
  display: flex;
  justify-content: center;
}

.shop_load-new-data {
  cursor: pointer;
  color: white;
  margin: 10px;
  margin-bottom: 70px;
  background: transparent;
  border: 2px solid white;
  padding: 7px 25px;
  border-radius: 13px;
  transition: 0.3s;
  font-size: 15px;
}

.shop_load-new-data:hover {
  color: rgb(150, 150, 150);
  border: 2px solid rgb(150, 150, 150);
}

.shop_loader {
  color: white;
  margin: 10px;
  padding: 7px 25px;
  background: transparent;
}

@media (max-width: 2000px) {
  /* desktop */
  .shop-container {
    margin-top: 40px;
  }
}

@media (max-width: 1500px) {
  .shop-container {
    margin-top: 10px;
  }
  .shop_elem-wrapper {
    width: 70%;
  }
  .shop__search-input {
    width: 14%;
    font-size: 1.3rem;
  }
}
@media (max-width: 1000px) {
  .shop-container {
    margin-top: 10px;
  }
  .shop_elem-wrapper {
    width: 100%;
  }
  .shop_search {
    margin-left: 70%;
  }
  .shop__search-input {
    width: 100%;
  }
}
@media (max-width: 700px) {
  /* mobile */
  .shop_elem-wrapper {
    width: 100%;
  }
  .shop_elem {
    padding-right: 30%;
  }
  .shop-container {
    margin-top: 10px;
  }
  .shop_info {
    padding: 0;
  }
  .shop_elem {
    width: 100%;
  }
  .shop_info_container {
    padding: 2px;
    margin-left: 10%;
  }
  .shop_info_svg {
    margin: 0;
  }
  .shop__search {
    position: relative;
    margin-left: 0%;
    width: 96%;
    padding: 2%;
  }
}

@media (max-width: 500px) {
  .shop__search {
    position: relative;
    margin-left: 0%;
    width: 90%;
    height: 60px;
    padding: 5%;
  }
}
</style>
