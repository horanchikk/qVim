<template>
  <Transition name="fade">
    <div class="progressbar__waiting" v-if="icon === 'wait'">
      <div class="progressbar__messages">
        <h2 id="progressbar__messages" style="display: none"></h2>
      </div>
    </div>
    <div class="progressbar" v-else>
      <div class="progressbar__icon">
        <svg
          v-if="icon === 'req'"
          xmlns="http://www.w3.org/2000/svg"
          enable-background="new 0 0 24 24"
          height="48px"
          viewBox="0 0 24 24"
          width="24px"
          fill="#11CCEE"
        >
          <rect fill="none" height="24" width="24" />
          <path
            d="M15,5l-1.41,1.41L18.17,11H2V13h16.17l-4.59,4.59L15,19l7-7L15,5z"
          />
        </svg>
        <svg
          v-if="icon === 'res'"
          xmlns="http://www.w3.org/2000/svg"
          enable-background="new 0 0 24 24"
          height="24px"
          viewBox="0 0 24 24"
          width="24px"
          fill="#FF2400"
        >
          <rect fill="none" height="24" width="24" />
          <path
            d="M9,19l1.41-1.41L5.83,13H22V11H5.83l4.59-4.59L9,5l-7,7L9,19z"
          />
        </svg>
        <svg
          v-if="icon === 'wait'"
          xmlns="http://www.w3.org/2000/svg"
          enable-background="new 0 0 24 24"
          height="24px"
          viewBox="0 0 24 24"
          width="24px"
          fill="#bad1ce"
        >
          <g><rect fill="none" height="24" width="24" /></g>
          <g>
            <path
              d="M12,2C6.48,2,2,6.48,2,12c0,5.52,4.48,10,10,10s10-4.48,10-10C22,6.48,17.52,2,12,2z M7,13.5c-0.83,0-1.5-0.67-1.5-1.5 c0-0.83,0.67-1.5,1.5-1.5s1.5,0.67,1.5,1.5C8.5,12.83,7.83,13.5,7,13.5z M12,13.5c-0.83,0-1.5-0.67-1.5-1.5 c0-0.83,0.67-1.5,1.5-1.5s1.5,0.67,1.5,1.5C13.5,12.83,12.83,13.5,12,13.5z M17,13.5c-0.83,0-1.5-0.67-1.5-1.5 c0-0.83,0.67-1.5,1.5-1.5s1.5,0.67,1.5,1.5C18.5,12.83,17.83,13.5,17,13.5z"
            />
          </g>
        </svg>
        <svg
          v-if="icon === 'err'"
          xmlns="http://www.w3.org/2000/svg"
          height="24px"
          viewBox="0 0 24 24"
          width="24px"
          fill="#000000"
        >
          <path
            d="M4.47 21h15.06c1.54 0 2.5-1.67 1.73-3L13.73 4.99c-.77-1.33-2.69-1.33-3.46 0L2.74 18c-.77 1.33.19 3 1.73 3zM12 14c-.55 0-1-.45-1-1v-2c0-.55.45-1 1-1s1 .45 1 1v2c0 .55-.45 1-1 1zm1 4h-2v-2h2v2z"
            preserveAspectRatio="none"
            fill="#d84d4d"
          />
        </svg>
      </div>
      <div class="progressbar__messages">
        <h2 id="progressbar__messages">Please wait...</h2>
      </div>
    </div>
  </Transition>
</template>

<script>
export default {
  props: {
    icon: {
      type: String,
      required: true,
    },
  },
  methods: {
    setIcon(type) {
      return type;
    },
  },
};
</script>

<style lang="scss" scoped>
@keyframes loading {
  0% {
    opacity: 0%;
  }
  50% {
    opacity: 100%;
  }
  100% {
    opacity: 0%;
  }
}

.fade-enter-active,
.fade-leave-active {
  transform: translateY(0%);
  transition: 0.4s ease;
}

.fade-enter-from,
.fade-leave-to {
  transform: translateY(50%);
  opacity: 0;
}

.progressbar {
  position: fixed;
  width: 100%;
  height: 50px;
  bottom: 0;
  left: 0;
  right: 0;
  cursor: default;
  display: flex;
  flex-direction: row;
  background: rgba(0, 0, 0, 0.7);
}

.progressbar__icon {
  width: 10%;
  display: flex;
  align-items: center;
  justify-content: center;
  svg {
    animation-name: loading;
    animation-duration: 0.8s;
    animation-iteration-count: infinite;
  }
}

.progressbar__messages {
  width: 90%;
  color: white;
  font-size: 10px;
  text-justify: center;
}
</style>
