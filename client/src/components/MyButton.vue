<script setup></script>

<template>
  <button class="btn">
    <slot>Create</slot>
  </button>
</template>

<style lang="scss" scoped>
.btn {
  background-color: #41b080;
  padding: 8px 16px;
  border: none;
  display: block;
  width: 20%;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;

  &:hover {
    cursor: pointer;
    background-color: darken(#41b080, 10%);
  }
}
</style>
