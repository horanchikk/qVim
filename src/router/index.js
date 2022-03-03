import { createRouter, createWebHashHistory } from "vue-router";
import Home from "../pages/Home.vue";
import Plugins from "../pages/Plugins.vue";
import Settings from "../pages/Settings.vue";
import Configs from "../pages/Configs.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/plugins",
    name: "Plugins",
    component: Plugins,
  },
  {
    path: "/configs",
    name: "configs",
    component: Configs,
  },
  {
    path: "/settings",
    name: "Settings",
    component: Settings,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
