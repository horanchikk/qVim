<template>
  <div class="shop-container">
    <div class="shop_menu">
    <li class="elem_menu">Integrations</li>
    <li class="elem_menu">Code Display</li>
    <li class="elem_menu">Lauguage</li>
    <li class="elem_menu">Interface</li>
  </div>
  <div class="eac"><h1>EARLY ACCESS</h1></div>
  <div class="shop_search">
    <input type="text" placeholder="Find plugin..." class="shop_search_elem" />
  </div>
  <div class="shop_elem" v-for="plugin in plugins" :key="plugin">
    <div class="shop_info">
      <div class="shop_info_container">
        <h1 class="shop_info_title">{{ plugin.name }}</h1>
        <h4 class="shop_info_description">{{ plugin.description }}</h4>
      </div>
    </div>
    <div class="shop_info_icon">
      <a :href="plugin.link"
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
  </div>
</template>

<script>
export default {
  data() {
    return {
      plugins: [
        {
          name: "fugitive.vim",
          description:
            "Fugitive is the premier Vim plugin for Git. Or maybe it's the premier Git plugin for Vim? Either way, it's so awesome, it should be illegal. That's why it's called Fugitive.",
          link: "https://github.com/tpope/vim-fugitive",
          type: "Integrations",
        },
        {
          name: "surround.vim",
          description:
            "parentheses, brackets, quotes, XML tags, and more. The plugin provides mappings to easily delete, change and add such surroundings in pairs",
          link: "https://github.com/tpope/vim-surround",
          type: "Code Display",
        },
        {
          name: "The NERD Tree",
          description:
            "The NERDTree is a file system explorer for the Vim editor. Using this plugin, users can visually browse complex directory hierarchies, quickly open files for reading or editing, and perform basic file system operations.",
          link: "https://github.com/scrooloose/nerdtree",
          type: "Integrations",
        },
        {
          name: "Syntatic",
          description:
            "Syntastic is a syntax checking plugin for Vim created by Martin Grenfell. It runs files through external syntax checkers and displays any resulting errors to the user. This can be done on demand, or automatically as files are saved. If syntax errors are detected, the user is notified and is happy because they didn't have to compile their code or execute their script to find them.",
          link: "https://github.com/scrooloose/syntastic",
          type: "Code Display",
        },
      ],
    };
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Ubuntu&display=swap');

.shop-container {font-family: 'Ubuntu', sans-serif;}

.shop_elem {
  position: relative;
  width: 60%;
  height: auto;
  margin-left: 20%;
  background-color: rgba(110, 110, 110, 0.7);
  border-radius: 5px;
  color: white;
  opacity: 0;
  transform: translateY(-100%);
  animation: load3 1s forwards;
}

.eac {
  position: fixed;
  color: rgba(155, 155, 155, 0.3);
  margin-left: 10px;
  margin-top: 38%;
  font-weight: bolder;
  cursor: default;
}

.shop_search {
  position: absolute;
  width: 15%;
  height: 10%;
  padding: 0px 15px 15px 15px;
  margin-left: 82%;
}

.shop_search_elem {
  width: 100%;
  border: 0;
  background: rgba(155, 155, 155, 0.5);
  height: 50%;
  text-align: center;
  font-size: 23px;
  border-radius: 5px;
  transition: 0.3s ease-in;
}
.shop_search_elem::placeholder {
  color: white;
  transition: 0.3s ease-in;
}

.shop_search_elem:focus {
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
  margin-top: 15%;
  padding-bottom: 10px;
  border-bottom-right-radius: 5px;
  border-top-right-radius: 5px;
  background-color: rgba(170, 170, 170, 0.7);
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
  width: auto;
  height: 40px;
  cursor: pointer;
  margin-right: 15px;
  margin-top: 10px;
  background-color: rgba(236, 240, 241, 0.6);
  border-bottom-right-radius: 5px;
  border-top-right-radius: 5px;
  list-style-type: none;
  transition: 0.2s ease-in-out;
  transform: translateX(-100%);
  animation: load2 2s forwards;
  font-size: 100%;
  font-family: "Ubuntu", sans-serif;
  text-align: center;
}

.elem_menu:hover {
  background-color: rgba(236, 240, 241, 1);
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
</style>
