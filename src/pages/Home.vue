<template>
  <div class="home__main">
    <div class="home__cont">
      <h1 class="cont__title">Welcome to qVim!</h1>
      <p class="cont__desc desc__welcome">
        <a href="https://github.com/horanDEV/qVim">qVim</a> - it is vim plugin
        manager with graphic interface. Here you can find some plugins and qVim
        install it to your favorite text editor automatically.
      </p>
    </div>
    <div class="home__cont">
      <h2 class="cont__title">Why qVim?</h2>
      <span class="cont__desc desc__why">
        <ul>
          <li>This is more convenient than using the default terminal</li>
          <li>It is using vim-plug technology</li>
          <li>You can manage your plugins</li>
          <li>
            You can load your favorite config and qVim can working with it
          </li>
          <li>Store of configs for vim in one utility</li>
          <li>And many functions for easiest plugin management...</li>
        </ul>
      </span>
    </div>
    <div class="home__cont">
      <h2 class="cont__title">About developing</h2>
      <p class="cont__desc desc__dev">
        Our product is currently under development, so some functions may not be
        working. Please, wait, when product has been released. If you have any
        suggestions for improving the product or you have found a bug, please
        contact us:
        <a href="mailto:horandev.service@gmail.com"
          >horandev.service@gmail.com</a
        >.
      </p>
    </div>
  </div>
</template>

<script />

<style>
.home__main {
  display: flex;
  flex-direction: column;
  margin-left: 20%;
  margin-right: 20%;
}

/* Cont */

.home__cont {
  margin: 20px 10px 0px 0px;
  padding: 10px;
  border-radius: 13px;
  color: whitesmoke;
}

.cont__title {
  opacity: 0;
  font-size: 60px;
  text-align: center;
  transform: translateY(-100%);
  animation: load 1s forwards;
}

.cont__desc {
  opacity: 0;
  transform: translateY(-100%);
  font-size: 30px;
  line-height: 3rem;
}

/* Desc */

.desc__welcome {
  text-align: center;
  animation: load 1s forwards;
  animation-delay: 0.5s;
}

.desc__welcome > a {
  text-decoration: none;
}

.desc__why {
  animation: load 1s forwards;
  animation-delay: 1s;
}

.desc__dev {
  list-style-type: circle;
  animation: load 1s forwards;
  animation-delay: 1.5s;
  text-align: center;
}

.desc__dev > a {
  text-decoration: none;
}

@keyframes load {
  0% {
    transform: translateY(-100%);
    opacity: 0;
  }
  70% {
    opacity: 0;
  }
  100% {
    transform: translateY(0%);
    opacity: 1;
  }
}

@media (max-width: 1300px) {
  .home__main {
    margin-left: 10%;
    margin-right: 10%;
  }
}

@media (max-width: 900px) {
  .home__main {
    margin: 0;
  }
  .cont__title {
    font-size: 50px;
  }
  .cont__desc {
    font-size: 35px;
    line-height: 2.5rem;
  }
}

@media (max-width: 600px) {
  .home__main {
    margin: 0;
  }
  .cont__title {
    font-size: 40px;
  }
  .cont__desc {
    font-size: 20px;
    line-height: 1.5rem;
  }
}
</style>
