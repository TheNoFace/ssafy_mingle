<template>
  <div class="top-detail col text-color">
    <!-- 이미지 -->
    <div class="col-4 detail-img">
      <img
        :src="`https://image.tmdb.org/t/p/original${props.movie.poster_path}`"
        :alt="movie.title"
        width="100%"
      />
    </div>
    <div class="col-8" style="position: relative;">
      <!-- 제목, 평점 -->
      <div class="detail-title">
        <h1 style="font-size: 70px">{{ movie.title }}</h1>
        <h3>
          <i class="fa-solid fa-star" style="color: yellow"></i>
          {{ (movie.vote_average / 2).toFixed(1) }}
        </h3>
      </div>
      <!-- 줄거리 -->
      <div style="padding: 20px">
        <p>{{ movie.overview }}</p>
      </div>
      <!-- 장르 -->
      <div style="padding: 20px">
        <div class="d-flex">
          <p class="px-2 category-button rounded" v-for="genre in movie.genres">
            {{ genre.name }}
          </p>
        </div>
      </div>
      <!-- 좋아요 버튼 -->
      <div class="likeBtn">
        <h3 class="m-0 ms-2" @click.prevent="likeMovie(movie.tmdb_id)">
          <i class="fa-solid fa-thumbs-up me-2" style="height: 30px"></i>
          {{ movie.liked_users.length }}
        </h3>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useMovieStore } from '@/stores/movie';
import { useUserStore } from '@/stores/user'; 
import axios from 'axios'

const store = useMovieStore()
const userStore = useUserStore()
const router = useRouter()

const props = defineProps({
  movie: Object,
});

const likeMovie = function (movieId) {
  axios({
    method : 'post',
    url : `${store.BASE_URL}/api/v1/movies/like/movie/${movieId}/`,
    headers: {
      Authorization: `Token ${userStore.sessionData.token}`,
    },
  })
    .then(response => {
      console.log(response.data)
      router.go()
    })
    .catch(error => {
      console.log(error)
    })
}
</script>

<style scoped>
.top-detail {
  display: flex;
}

.detail-img {
  padding: 20px;
}

.detail-title {
  padding: 20px;
  display: flex;
  justify-content: space-between;
}

.likeBtn {
    position: absolute;
    left: 20px;
    bottom: 20px;
}
</style>
