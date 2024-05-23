<template>
  <div v-if="movieList ">
    <h4 class="m-0 my-3" style="color: white">카테고리별 추천 영화</h4>
    <div
      class="my-3"
      v-for="category in Object.keys(movieList)"
      :keys="category"
    >
      <h5 class="category-name rounded text-color" style="margin: 0">
        {{ category }}
      </h5>
      <div class="scroll-container">
        <MainRecommendCard
          v-for="movie in movieList[category]"
          :key="movie.title"
          :movie="movie"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useMovieStore } from '@/stores/movie'
import { useUserStore, useUserTempStore } from '@/stores/user';
import axios from 'axios'
import MainRecommendCard from './MainRecommendCard.vue';

const store = useMovieStore()
const userStore = useUserStore()
const userTempStore = useUserTempStore()

const movieList = ref(null)
onMounted(() => {
  axios({
    method: 'get',
    url: `${store.BASE_URL}/api/v1/movies/like/category/movie/`,
    headers: {
      Authorization: `Token ${userStore.sessionData.token}`,
    },
  })
    .then(response => {
      // console.log(response.data)
      movieList.value = response.data
      console.log(movieList.value)
    })
    .catch(error => {
      console.log(error)
    })
})
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

.category-name {
  width: 10%;
  text-align: center;
  border: 2px solid #76abae;
}
</style>