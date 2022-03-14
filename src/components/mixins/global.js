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
  },
};
