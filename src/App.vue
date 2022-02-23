<template>
  <header class="header-main">
    <div class="header-img">
      <router-link to="/">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          height="24px"
          viewBox="0 0 24 24"
          width="24px"
        >
          <path clip-rule="evenodd" d="M0 0h24v24H0z" fill="none" />
          <path
            d="M22.7 19l-9.1-9.1c.9-2.3.4-5-1.5-6.9-2-2-5-2.4-7.4-1.3L9 6 6 9 1.6 4.7C.4 7.1.9 10.1 2.9 12.1c1.9 1.9 4.6 2.4 6.9 1.5l9.1 9.1c.4.4 1 .4 1.4 0l2.3-2.3c.5-.4.5-1.1.1-1.4z"
          />
        </svg>
      </router-link>
    </div>

    <div class="header-menu">
      <router-link to="/plugins"> <li class="header-elem">Plugins</li> </router-link>
      <router-link to="/configs"> <li class="header-elem">Configs</li> </router-link>
      <router-link to="/settings"> <li class="header-elem">Settings</li> </router-link>
      <li class="header-elem">About</li>
    </div>
    <div class="header-turnoff">
      <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24">
        <g data-name="Layer 2">
          <g data-name="power">
            <rect width="24" height="24" opacity="0" />
            <path d="M12 13a1 1 0 0 0 1-1V2a1 1 0 0 0-2 0v10a1 1 0 0 0 1 1z" />
            <path
              d="M16.59 3.11a1 1 0 0 0-.92 1.78 8 8 0 1 1-7.34 0 1 1 0 1 0-.92-1.78 10 10 0 1 0 9.18 0z"
            />
          </g>
        </g>
      </svg>
    </div>
  </header>
  <div id="app">
    <router-view />
  </div>
</template>

<script />

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Dongle:wght@300&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Ubuntu:wght@500&display=swap");

body {
  margin: 0;
  font-family: "Ubuntu", sans-serif;
  background-color: #131313;
}

.header-main {
  width: 100%;
  height: 20%;
  // padding: 5px 0;
  margin: 0 auto;
  background-color: #242424;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: "Dongle", sans-serif;
}

.header-elem {
  height: 100%;
  margin: 0 20px;
  padding: 0 10px;
  color: #9e9e9e;
  font-size: 30px;
  transition: 0.2s ease-in-out;
  list-style-type: none;
  text-align: center;
  vertical-align: middle;
  cursor: default;
  line-height: 50px;
}

.header-elem:hover {
  cursor: pointer;
  font-size: 40px;
  //   transform: scale(1.25);
  color: rgba(255, 255, 255, 1);
}

.header-menu {
  display: flex;
  align-items: center;
  justify-content: center;
  a {
    text-decoration: none;
  }
}

.header-img {
  display: flex;
  align-items: center;
  margin-right: 30px;
  a {
    height: 27px;
    svg {
      fill: rgba(255, 255, 255, 0.7);
      transition: 0.3s ease-in-out;
      :hover {
        fill: rgba(255, 255, 255, 1);
      }
    }
  }
}

.header-turnoff {
  margin-left: 30px;
  display: flex;
  align-items: center;
  cursor: pointer;
  svg {
    left: 100px;
    fill: rgba(255, 0, 0, 0.5);
    transition: 0.3s ease-in-out;
    :hover {
      fill: rgba(255, 0, 0, 1);
    }
  }
}

.header-turnoff > svg:hover {
  fill: rgba(255, 0, 0, 1);
}

.router-link-active {
  li {
    font-size: 35px;
    color: rgb(255, 255, 255);
  }
  svg {
    fill: rgb(255, 255, 255);
  }
}

@media (max-width: 1700px) {
  .header-elem {
    margin: 0 10px;
  }
}
@media (max-width: 800px) {
  .header-elem {
    margin: 0;
    padding: 10px;
  }
}
@media (max-width: 500px) {
  .header-elem {
    font-size: 17px;
    margin: 0;
    padding: 10px;
  }
  .header-elem:hover {
    font-size: 17px;
    margin: 0;
    padding: 10px;
  }
  .router-link-active {
    li {
      font-size: 18px;
    }
  }
}
</style>
