<template>
  <div class="top-detail col text-color rounded" @click.prevent="goDetail(movie.id)">
    <!-- 이미지 -->
    <div class="col-2 detail-img">
      <img :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" :alt="`등록된 포스터가 없습니다.`" width="100%">
    </div>
    <div class="col-10" style="position: relative;">
      <!-- 제목, 평점 -->
      <div class="detail-title">
        <h1 style="font-size: 30px;">{{ movie.title }}</h1>
        <h3>
          <i class="fa-solid fa-star" style="color: yellow;"></i>
          {{ (movie.vote_average / 2).toFixed(1) }}
        </h3>
      </div>
      <!-- 줄거리 -->
      <div style="padding: 20px;">
        <p v-if="movie.overview.length < 440">{{ movie.overview }}</p>
        <p v-else>{{ movie.overview.substring(0, 440) }}...</p>
      </div>
      <!-- 장르 -->
      <div style="padding: 20px;">
        <p class="d-flex m-0 genre">장르 :
        <p class="px-2 m-0" v-for="genre in movie.genres">{{ genre.name }}</p>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const movieData = ref({})

const props = defineProps({
  movie: Object
})

const goDetail = function (movie_id) {
  router.push({ name: 'DetailView', params: { tmdb_id: movie_id } })
}

onMounted(() => {
  if (props.movie['id']) {
    props.movie['tmdb_id'] = props.movie.id
  }
  Object.assign(movieData.value, props.movie)
})
</script>

<style scoped>
.top-detail {
  display: flex;
  border: 2px solid white;
  margin: 10px;
}

.detail-img {
  padding: 10px;
}

.detail-title {
  padding: 20px;
  display: flex;
  justify-content: space-between;
}

.genre {
  position: absolute;
  left: 20px;
  bottom: 20px;
}
</style>