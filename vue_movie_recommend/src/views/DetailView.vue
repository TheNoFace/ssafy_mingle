<template>
  <div v-if="store.detailMovie">
    <div class="container">
      <DetailMovie :movie="store.detailMovie" />
    </div>
    <div class="container mt-5">
      <DetailReview :reviews="store.detailMovie.review_set" />
    </div>
  </div>
  <div v-else>
    <p class="text-color">불러오는 중...</p>
  </div>
</template>

<script setup>
import DetailMovie from "@/component/DetailMovie.vue"
import DetailReview from "@/component/DetailMovieReview.vue"
import { useMovieStore } from "@/stores/movie"
import { ref, onMounted } from "vue"
import { useRoute } from "vue-router"

const route = useRoute()
const store = useMovieStore()

const tmdbId = ref(route.params.tmdb_id)

onMounted(() => {
  if (store.detailMovie) {
    store.detailMovie = null    
  }
  store.getDetailMovie(tmdbId.value)
})
</script>

<style scoped>

</style>