<template>
  <div v-if="store.popularMovieList.length">
    <div id="carouselExampleCaptions" class="carousel slide carousel-total-size">
      <div class="carousel-indicators" style="background-color: #ffffff00; padding-bottom: 40px;">
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button v-for="n in idx" :key="n" type="button" data-bs-target="#carouselExampleCaptions" :data-bs-slide-to="n"></button>
      </div>
      <div class="carousel-inner">
        <MainPopularityCard 
        :isActive="true"
        :movie="store.popularMovieList[0]"
        :rank="1"
        />
        <MainPopularityCard 
        v-for="(movie, idx) in store.popularMovieList.slice(1)"
        :key="movie.title"
        :isActive="false"
        :movie="movie"
        :rank="idx+2"
        />
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev" style="padding-left: 50px;">
        <span class="carousel-control-prev-icon" aria-hidden="true" style="background-color: #ffffff00;"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next" style="padding-right: 50px;">
        <span class="carousel-control-next-icon" aria-hidden="true" style="background-color: #ffffff00;"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import MainPopularityCard from '@/component/MainPopularityCard.vue';
import { useMovieStore } from '@/stores/movie'
import { ref, onMounted } from 'vue'

const idx = [1, 2, 3, 4, 5, 6, 7, 8, 9]
const rank = 2
const store = useMovieStore()

onMounted(() => {
  store.getMovieList('popularity')
})
</script>

<style scoped>
.carousel-total-size {
  padding : 0px 60px 40px 60px;
}
</style>