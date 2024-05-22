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
import Search from "@/component/Search.vue";
import MainPopularity from "@/component/MainPopularity.vue";
import MainReleased from "@/component/MainReleased.vue";
import MainCategoryMovie from "@/component/MainCategoryMovie.vue";
</script>

<style scoped>
.searchBox {
  margin: 50px;
}
</style>
