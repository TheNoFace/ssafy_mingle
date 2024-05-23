<template>
  <div class="text-color container">
    <div v-if="store.recommendCategoryMovieList">
      <p class="m-0 my-2">{{ categoryName }} 장르의 영화를 보고있어요!</p>
      <div v-for="movie in store.recommendCategoryMovieList[1]" :key="movie.tmdb_id">
        <CategoryRecommendMovieCard :movie="movie" />
      </div>
    </div>
    <div v-else class="text-center">
      <v-progress-circular indeterminate :size="70" :width="8" color="white"></v-progress-circular>
    </div>
  </div>
</template>

<script setup>
import { onMounted, computed } from "vue";
import { useRoute } from "vue-router";
import { useMovieStore } from "@/stores/movie";
import CategoryRecommendMovieCard from "./CategoryRecommendMovieCard.vue";

const route = useRoute();
const store = useMovieStore();
const categoryName = computed(() => {
  if (store.recommendCategoryMovieList.length) {
    return store.recommendCategoryMovieList[0];
  }
});

onMounted(() => {
  if (store.recommendCategoryMovieList) {
    categoryName.value = store.recommendCategoryMovieList[0];
  } else {
    store.recommendCategory(route.params.category_id);
  }
});
</script>

<style scoped></style>
