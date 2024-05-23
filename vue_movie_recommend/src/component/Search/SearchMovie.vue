<template>
  <div class="text-color">
    <CategoryRecommendMovieCard
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script setup>
import CategoryRecommendMovieCard from '@/component/Category/CategoryRecommendMovieCard.vue'

const props = defineProps({
  movies: Array,
})
</script>

<style scoped></style>
 