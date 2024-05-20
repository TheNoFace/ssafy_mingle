<template>
  <div class="carousel-item carousel-image" :class="{ active : isActive }">
    <img :src="imageURL" alt="image" class="d-block w-100" @click="godetail(movie.tmdb_id)">
    <h1 class="carousel-text m-0 nunito-text">{{ rank }}</h1>
    <p class="carousel-content">{{ movie.title }}</p>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from 'vue-router'

const router = useRouter()

const props = defineProps({
  isActive: Boolean,
  movie: Object,
  rank : Number
});

const imageURL = ref(
  `https://image.tmdb.org/t/p/original${props.movie.backdrop_path}`
);

const godetail = function (tmdb_id) {
    router.push({ name : 'DetailView', params : { tmdb_id : tmdb_id} })
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200..1000;1,200..1000&display=swap');

.nunito-text {
  color: white;
  font-family: "Nunito", sans-serif;
  font-optical-sizing: auto;
  font-weight: 700;
  font-style: bold;
  font-size: 350px;
  position: absolute;
  left: 100px;
  top: 0px;
}

.carousel-text {
  background-color: #ffffff00
}

.carousel-content{
  background-color: #ffffff00;
  font-family: "Nunito", sans-serif;
  font-optical-sizing: auto;
  font-weight: 700;
  font-style: bold;
  color: white;
  position: absolute;
  right: 30px;
  bottom: 30px;
  font-size: 80px;
}
</style>
