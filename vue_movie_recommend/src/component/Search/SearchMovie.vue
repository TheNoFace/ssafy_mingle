<template>
  <div class="text-color">
    <CategoryRecommendMovieCard
      v-for="movie in movies"
      :key="movie.tmdb_id"
      :movie="movie"
    />
  </div>
</template>

<script setup>
import CategoryRecommendMovieCard from '@/component/Category/CategoryRecommendMovieCard.vue';

defineProps({
  movies: Array,
});
</script>

<style scoped></style>
