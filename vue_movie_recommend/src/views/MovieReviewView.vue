<template>
  <div class="text-color">
    <h1>{{ store.MovieReviewList[0] }}</h1>
    <div
      v-for="review in store.MovieReviewList[1]"
      :key="review.id"
      class="my-3"
    >
      <AllReviewCard :review="review" />
    </div>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useRoute } from "vue-router";
import { useMovieStore } from "@/stores/movie";
import AllReviewCard from "@/component/AllReviewCard.vue";

const store = useMovieStore();
const route = useRoute();

const tmdb_id = route.params.tmdb_id;

onMounted(() => {
  store.getMovieReview(tmdb_id);
});
</script>

<style scoped></style>
