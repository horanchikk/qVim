<template>
  <div class="wrapper">
    <span class="cont_title">
      <h1 class="title">Welcome to qVim!</h1>
      <a class="description">It is qVim lol :D</a>
    </span>
  </div>
</template>

<script />

<style>
@import url("https://fonts.googleapis.com/css2?family=Ubuntu:wght@500&display=swap");

.wrapper {
  width: 640px;
  height: 300px;
  display: block;
  margin-left: auto;
  margin-right: auto;
  color: whitesmoke;
}

.title {
  font-family: "Ubuntu", sans-serif;
  font-size: 60px;
  margin-left: 2%;
  transform: translateY(-100%);
  opacity: 0;
  animation: load 1s forwards;
}

.description {
  font-family: "Ubuntu", sans-serif;
  font-size: 30px;
  padding-left: 5%;
  transform: translateY(-100%);
  opacity: 0;
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
