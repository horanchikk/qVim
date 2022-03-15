<template>
  <div class="shop-container">
    <div class="shop__search">
      <input
        type="text"
        placeholder="Find plugin..."
        class="shop_search_elem"
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
              <h1 class="shop_info_title">{{ plugin.name }}</h1>
              <h4 class="shop_info_description">{{ plugin.description }}</h4>
            </div>
          </div>

          <div
            class="shop_info_icon"
            @click="installpkg(plugin.link, plugin.name)"
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
        v-else-if="!loading && currentPage <= pageLimit"
        @click="getPlugins"
        class="shop_load-new-data"
      >
        Load more
      </button>
    </div>
    <progressbar :icon="debico" />
  </div>
</template>

<script>
import progressbar from "../components/progressbar.vue";
import { animations } from "../components/mixins/global.js";

export default {
  data() {
    return {
      plugins: [],
      currentPage: 1,
      loading: true,
      pageLimit: 16,
      searchedPlugins: [],
      inputValue: "",
      debico: "res",
      editor: "none",
    };
  },
  components: {
    progressbar,
  },
  mixins: [animations],
  methods: {
    async debug() {
      for (;;) {
        let res = await fetch(`http://localhost:5000/log`);
        let restext = await res.text();

        if (restext === "Waiting...") {
          this.debico = "wait";
        } else {
          this.debico = "req";
        }

        document.getElementById("progressbar-messages").innerText = restext;
      }
    },
    async getPlugins() {
      this.loading = true;
      this.notify(`Requesting to Flask server. Please wait...`, "loop");
      const data = await fetch(
        `http://localhost:5000/topics?page=${this.currentPage}`
      );
      const plugins = await data.json();
      plugins.forEach((plugin) => {
        this.plugins.push(plugin);
        this.searchedPlugins.push(plugin);
      });
      this.currentPage += 1;
      this.loading = false;
    },
    async installpkg(link, name) {
      this.notify(`Installing ${name}...`, "loop");
      const req = await fetch(
        `http://localhost:5000/pluginstall?link=${link.toString()}`
      );
      const res = await req.text();
      if (res === "ok") {
        this.notify(`${name} has been installed!`, "done");
      }
    },
    async editorcheck() {
      const req = await fetch(`http://localhost:5000/vimcheck`);
      const res = await req.json();
      if (res.editor === "none") {
        return undefined;
      }
      this.editor = res.editor;
    },
  },
  async mounted() {
    this.getPlugins();
    this.debug();
    this.editorcheck();
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Ubuntu&display=swap");

.shop-container {
  font-family: "Ubuntu", sans-serif;
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
  transform: translateY(-100%);
  animation: load3 1s forwards;
}

.shop__search {
  margin-top: 10px;
  width: 15%;
  height: 10%;
  padding: 0px 15px 15px 15px;
  margin-left: 82%;
}

.shop_search_elem {
  width: 100%;
  border: 0;
  background: #3d3d3d;
  height: 50%;
  text-align: center;
  font-size: 23px;
  border-radius: 5px;
  transition: 0.3s ease-in;
  color: white;
}

.shop_search_elem::placeholder {
  color: white;
  transition: 0.3s ease-in;
}

.shop_search_elem:focus {
  color: black;
  outline: 0;
  background: rgba(195, 195, 195, 1);
}

.shop_search_elem:focus::placeholder {
  color: black;
}

.shop_info {
  margin: 10px;
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
}

.shop_info_description {
  width: 100%;
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
    position: fixed;
    margin-top: 40px;
  }
}

@media (max-width: 1500px) {
  .shop-container {
    margin-top: 40px;
  }
  .shop_elem-wrapper {
    width: 70%;
  }
  .shop_search {
    position: relative;
    width: 15%;
  }
}
@media (max-width: 1000px) {
  .shop-container {
    margin-top: 40px;
  }
  .shop_elem-wrapper {
    width: 100%;
  }
  .shop_search {
    width: 25%;
    margin-left: 70%;
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
    margin-top: 0px;
  }
  .shop_search {
    margin-left: 20%;
    width: 50%;
  }
  .shop_info {
    padding: 0;
  }
  .shop_elem {
    width: 100%;
  }
  .shop_info_container {
    padding: 2px;
  }
  .shop_info_svg {
    margin: 0;
  }
}

@media (max-width: 500px) {
  .shop_search {
    position: relative;
    margin-left: 0%;
    width: 90%;
  }
}
</style>
