<template>
  <button class="customBtn">{{ title }}</button>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
    },
  },
};
</script>

<style lang="scss" scoped>
.customBtn {
  cursor: pointer;
  background-color: rgba(0, 0, 0, 0);
  border: 0.15rem solid rgb(170, 170, 170);
  border-radius: 3px;
  color: rgb(170, 170, 170);
  transition: 0.2s ease-in-out;
  &:hover {
    border: 0.15rem solid rgb(210, 210, 210);
    color: rgb(210, 210, 210);
  }
  // &:active {
  //   border: 0.15rem solid rgb(210, 210, 210);
  //   color: rgb(210, 210, 210);
  // }
}
</style>
