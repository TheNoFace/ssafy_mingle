<template>
  <div v-if="store.detailMovie">
    <div class="container">
      <DetailMovie :movie="store.detailMovie" />
    </div>
    <div class="container mt-5">
      <DetailMovieReview :reviews="store.detailMovie.review_set" />
    </div>
  </div>
  <div v-else class="text-center">
    <v-progress-circular indeterminate :size="70" :width="8"></v-progress-circular>
  </div>
</template>

<script setup>
import DetailMovie from "@/component/MovieDetail/DetailMovie.vue";
import DetailMovieReview from "@/component/MovieDetail/DetailMovieReview.vue";
import { useMovieStore } from "@/stores/movie";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const store = useMovieStore();

const tmdbId = ref(route.params.tmdb_id);

onMounted(() => {
  if (store.detailMovie) {
    store.detailMovie = null;
  }
  store.getDetailMovie(tmdbId.value);
});
</script>

<style scoped></style>
