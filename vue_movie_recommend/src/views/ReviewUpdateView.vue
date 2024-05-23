<template>
  <div class="text-color" v-if="reviewInfo">
    <h1>Review Update Page</h1>
    <!-- 영화 정보 -->
    <div class="d-flex" style="padding: 10px">
      <div class="col-1">
        <img :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" :alt="movie.title" style="width: 100px" />
      </div>
      <div class="ms-2 col-11" style="position: relative">
        <h1>{{ movie.title }}</h1>
        <div class="movie-info">
          <p class="m-1">평점 : {{ (movie.vote_average/2).toFixed(1) }}</p>
          <div class="d-flex">
            <p v-for="genre in movie.genres" class="category-button rounded ms-0">
              {{ genre.name }}
            </p>
          </div>
        </div>
        <!-- 평점 입력 칸 -->
        <div class="vote">
          <p>평점 입력 칸</p>
        </div>
      </div>
    </div>

    <!-- 리뷰 수정 칸 -->
    <form @submit.prevent="updateReview(reviewInfo.id)" ref="updateForm">
      <input class="form-control review-input" type="text" :placeholder="reviewInfo.title" name="title" />
      <textarea class="form-control review-input text-color" type="text" style="height: 300px"
        name="content"></textarea>
      <div class="d-flex justify-content-end">
        <input class="review-submit rounded px-3 py-1" type="submit" value="리뷰 수정" />
      </div>
    </form>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
import { useUserStore } from '@/stores/user';
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const store = useMovieStore()
const userStore = useUserStore()
const route = useRoute()

const reviewInfo = ref(null)
const reviewId = route.params.review_id
const movie = ref(null)
const movieId = ref(null)

onMounted(() => {
  store.getDetailReview(reviewId)
  reviewInfo.value = store.reviewDetail
  movie.value = store.reviewDetail.movie
  movieId.value = movie.value.tmdb_id
  console.log(reviewInfo)
})

const updateForm = ref(null)
const updateReview = function (reviewId) {
  const payload = new FormData(updateForm.value)
  store.updateReview(payload, reviewId, movieId)
}

</script>

<style scoped>
.movie-info {
  position: absolute;
  left: 0;
  bottom: 0;
}

.vote {
  position: absolute;
  right: 10px;
  top: 0;
}

input::placeholder {
  color: white;
}

.review-input {
  background-color: #ffffff00;
  color: white;
  margin-top: 20px;
  margin-bottom: 10px;
}

.review-submit {
  border: 2px solid #76abae;
  color: white;
}
</style>