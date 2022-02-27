<template>
  <div class="home__main">
    <div class="home__cont">
      <h1 class="cont__title">Welcome to qVim!</h1>
      <a class="cont__desc">qVim - it is vim plugin manager with graphic interface. Here you can find some plugins and qVim install it to your favorite text editor automatically.</a>
    </div>
    <div class="home__cont">
      <h2 class="cont__title">Why qVim?</h2>
    </div>
  </div>
</template>

<script />

<style>
.home__main {
  width: 640px;
  display: flex;
  flex-direction: row;
  margin-left: auto;
  margin-right: auto;
  
}

.home__cont {
  margin: 20px 10px 0px 0px;
  padding: 10px;
  border-radius: 13px;
  color: whitesmoke;
  background-color: #3d3d3d;
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
  text-align: center;
  font-size: 30px;
  transform: translateY(-100%);
  animation: load 2s forwards;
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
</style>
