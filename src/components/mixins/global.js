export const animations = {
  methods: {
    async notify(message, icon) {
      if (icon == "done") {
        this.typein = "done";
      } else if (icon == "error") {
        this.typein = "error";
      } else if (icon == "loop") {
        this.typein = "loop";
      } else if (icon == "wifinot") {
        this.typein = "wifinot";
      }

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
    async alertclose() {
      let container = document.getElementById("vim-alert-container").style;
      let bg = document.getElementById("vim-alert-bg").style;
      container.transform = "translate(-50%, -300%)";
      bg.background = "rgb(0 0 0 / 0)";
      setTimeout(() => {
        bg.display = "none";
        document.getElementById("main-container").style.filter = "blur(0px)";
        document.getElementById("header-container").style.filter = "blur(0px)";
      }, 600);
    },
    async alertopen() {
      document.getElementById("main-container").style.filter = "blur(5px)";
      document.getElementById("header-container").style.filter = "blur(5px)";
      document.getElementById("vim-alert-bg").style.display = "block";
    },
  },
};
