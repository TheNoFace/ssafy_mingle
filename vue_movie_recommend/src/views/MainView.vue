<template>
  <div>
    <div class="container">
      <MainPopularity />
    </div>
    <div class="container">
      <MainReleased />
    </div>
    <div class="container">
      <MainCategoryMovie />
    </div>
  </div>
</template>

<script setup>
import MainPopularity from "@/component/MainPage/MainPopularity.vue";
import MainReleased from "@/component/MainPage/MainReleased.vue";
import MainCategoryMovie from "@/component/MainPage/MainCategoryMovie.vue";
</script>

<style scoped></style>
