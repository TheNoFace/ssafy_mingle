<template>
    <div class="container">
        <DetailMovie 
        :movie="store.detailMovie"
        />
    </div>
    <div class="container mt-5">
        <DetailReview 
        :reviews="store.detailMovie.review_set"
        />
    </div>
</template>

<script setup>
import DetailMovie from '@/component/DetailMovie.vue';
import DetailReview from '@/component/DetailReview.vue';
import { useMovieStore } from '@/stores/movie'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const store = useMovieStore()

const tmdbId = ref(route.params.tmdb_id)

onMounted(() => {
    store.getDetailMovie(tmdbId.value)
})
</script>

<style scoped>

</style>