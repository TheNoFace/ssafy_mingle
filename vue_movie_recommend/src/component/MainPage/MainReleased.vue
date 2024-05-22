<template>
  <div>
    <h4 style="color: white">신규 업데이트 된 영화</h4>
    <div class="scroll-container">
      <MainRecommendCard
        v-for="movie in store.releaseMovieList"
        :key="movie.title"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script setup>
import MainRecommendCard from "@/component/MainPage/MainRecommendCard.vue";
import { useMovieStore } from "@/stores/movie";
import { ref, onMounted } from "vue";

const store = useMovieStore();

onMounted(() => {
  store.getMovieList("release_date");
});
</script>

<style scoped>
.scroll-container {
  overflow-x: scroll;
  overflow-y: hidden;
  display: flex;
  flex-wrap: nowrap;
}
.scroll-container::-webkit-scrollbar {
  background-color: #ffffff00;
  height: 5px;
}

.scroll-container::-webkit-scrollbar-thumb {
  background-color: #76abae;
  border-radius: 5px;
}
</style>
