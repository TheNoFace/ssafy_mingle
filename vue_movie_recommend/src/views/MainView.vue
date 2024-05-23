<template>
  <div>
    <!-- searchBox -->
    <div class="container">
      <div class="search-box">
        <div class="input-group mb-3">
          <label class="input-group-text search-box-input" for="searchBox">
            <i class="fa-solid fa-magnifying-glass" style="color: white"></i>
          </label>
          <input type="text" class="form-control search-box-input" id="searchBox" @focus="search" />
        </div>
      </div>
    </div>

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
import MainPopularity from "@/component/MainPage/MainPopularity.vue"
import MainReleased from "@/component/MainPage/MainReleased.vue"
import MainCategoryMovie from "@/component/MainPage/MainCategoryMovie.vue"
import { useRouter } from 'vue-router'

const router = useRouter()

const search = function () {
  router.push({ name: 'SearchView' })
}
</script>

<style scoped></style>

<style>
.search-box {
  margin: 50px;
}

.search-box-input {
  border-color: white;
  background-color: rgba(255, 255, 255, 0);
  color: white;
}
</style>