export const utils = {
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
        let res = await fetch(`http://localhost:5000/log`);
        let restext = await res.text();

        if (restext === "Waiting...") {
          this.debico = "wait";
        } else if (restext === "Exception: command not found!") {
          this.debico = "err";
        } else {
          this.debico = "req";
        }

        document.getElementById("progressbar__messages").innerText = restext;
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
    async instplugin(link, name) {
      this.notify(`Installing ${name}...`, "loop");
      const req = await fetch(
        `http://localhost:5000/pluginstall?link=${link.toString()}`
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
      const req = await fetch(
        `http://localhost:5000/plugupdate`
      );
      const res = await req.text();
      if (res === "ok") {
        this.notify(`Plugins has been updated!`, "done");
      } else {
        this.notify(`Plugins aren't updated!`, "error");
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
};
