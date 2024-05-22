<template>
  <div class="carousel-item carousel-image" :class="{ active : isActive }">
    <img :src="backimageURL" alt="image" class="backdrop-image" @click="godetail(movie.tmdb_id)">
    <img :src="posterimageURL" alt="image" class="d-block poster-image m-auto" @click="godetail(movie.tmdb_id)">
    <h1 class="carousel-text m-0 nunito-text rank">{{ rank }}</h1>
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

const backimageURL = ref(
  `https://image.tmdb.org/t/p/original${props.movie.backdrop_path}`
);

const posterimageURL = ref(
  `https://image.tmdb.org/t/p/original${props.movie.poster_path}`
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

.backdrop-image {
  z-index: 1;
  position: absolute;
  left: 0;
  top: 0;
  height: 100%;
  filter : brightness(30%)
}

.poster-image {
  position: relative;
  width: 40%;
  height: 100%;
  z-index: 2;
}

.rank {
  z-index: 2;
}
</style>
