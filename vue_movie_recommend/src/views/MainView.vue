<template>
  <div>
    <Search class="searchBox" />
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
import Search from "@/component/Search/Search.vue";
import MainPopularity from "@/component/MainPage/MainPopularity.vue";
import MainReleased from "@/component/MainPage/MainReleased.vue";
import MainCategoryMovie from "@/component/MainPage/MainCategoryMovie.vue";
</script>

<style scoped>
.searchBox {
  margin: 50px;
}
</style>
