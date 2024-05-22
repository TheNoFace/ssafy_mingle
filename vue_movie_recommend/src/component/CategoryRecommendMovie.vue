<template>
  <div class="text-color container">
    <div v-if="store.recommendCategoryMovieList">
      <p class="m-0 my-2">선택한 카테고리 : {{ categoryName }}</p>
      <div
        v-for="movie in store.recommendCategoryMovieList[1]"
        :key="movie.tmdb_id"
      >
        <CategoryRecommendMovieCard :movie="movie" />
      </div>
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
