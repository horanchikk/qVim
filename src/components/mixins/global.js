const SERVER_URL = "http://0.0.0.0:5005";

export const utils = {
  data() {
    return {
      debico: "res",
      typein: "error",
      editor: "none",
      alertShowing: false,
      title: "",
      description: "",
    };
  },
  methods: {
    async notify(message, icon) {
      // Icons: done error loop wifinot
      this.typein = icon;

      document.getElementById("notify-container-message").innerText = message;
      let elem = document.getElementById("notify-container").style;
      elem.display = "flex";

      setTimeout(() => {
        elem.opacity = "1";
        elem.transform = "translateX(0%)";
      }, 100);
      setTimeout(() => {
        elem.opacity = "0";
        elem.transform = "translateX(-20%)";
      }, 2000);
      setTimeout(() => {
        elem.display = "none";
      }, 2400);
    },
    async debug() {
      for (;;) {
        let res = await fetch(`${SERVER_URL}/log`);
        let restext = await res.text();

        if (restext === "Waiting...") {
          this.debico = "wait";
        } else if (
          restext ===
          "Exception: command not found! Install Neovim and try again!"
        ) {
          this.debico = "err";
        } else if (restext === "Check your internet connection!") {
          this.debico = "err";
          this.internet = false;
          this.loading = false;
        } else {
          this.debico = "req";
        }

        document.getElementById("progressbar__messages").innerText = restext;
      }
    },
    async launch() {
      this.notify(`Launching nvim/vim`, "loop");
      const req = await fetch(`${SERVER_URL}/launch`);
      const res = await req.text();
      if (res === "ok") {
        this.notify(`Launched!`, "done");
      } else {
        this.notify(`Exception!`, "error");
      }
    },
    async getPlugins() {
      this.loading = true;
      this.notify(`Requesting to Flask server. Please wait...`, "loop");
      const data = await fetch(`${SERVER_URL}/topics?page=${this.currentPage}`);
      const plugins = await data.json();
      plugins.forEach((plugin) => {
        this.plugins.push(plugin);
        this.searchedPlugins.push(plugin);
      });
      this.currentPage += 1;
      this.loading = false;
    },
    async instplugin(link, name) {
      this.notify(`Installing ${name}...`, "loop");
      const req = await fetch(
        `${SERVER_URL}/pluginstall?link=${link.toString()}`
      );
      const res = await req.text();
      if (res === "ok") {
        this.notify(`${name} has been installed!`, "done");
      } else {
        this.notify(`${name} is not installed!`, "error");
      }
    },
    async updplugin() {
      this.notify(`Updating plugins, please wait...`, "loop");
      const req = await fetch(`${SERVER_URL}/plugupdate`);
      const res = await req.text();
      if (res === "ok") {
        this.notify(`Plugins has been updated!`, "done");
      } else {
        this.notify(`Plugins aren't updated!`, "error");
      }
    },
    async editorcheck() {
      const req = await fetch(`${SERVER_URL}/vimcheck`);
      const res = await req.json();
      if (res.editor === "none") {
        return undefined;
      }
      this.editor = res.editor;
    },
    async updatevim() {
      this.notify(`Updating nvim/vim, please wait...`, "loop");
      const req = await fetch(`${SERVER_URL}/upgradevim`);
      const res = await req.text();
      if (res === "ok") {
        this.notify(`Nvim/vim has been updated!`, "done");
      } else {
        this.notify(`Nvim/vim hasn't been updated.`, "error");
      }
    },
    async reloadapp() {
      window.history.go();
    },
  },
  async mounted() {
    this.editorcheck();
    this.debug();
  },
};
