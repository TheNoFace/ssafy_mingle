<template>
  <div class="review-detail-top">
    <div class="col-3" @click="goDetailMovie(review.movie.tmdb_id)">
      <img :src="`https://image.tmdb.org/t/p/original${review.movie.poster_path}`" :alt="review.movie.title"
        style="width: 100%" />
    </div>
    <div class="m-4 col-9" style="position: relative">
      <div>
        <div class="d-flex justify-content-between">
          <div class="info" @click="goProfile(review.user.username)">
            <i class="fa-regular fa-face-smile" style="color: #76abae; height: 45px"></i>
            <h4 class="m-0 mx-3">{{ review.user.nickname }}</h4>
          </div>
        </div>
        <h1 class="m-0 my-4">{{ review.title }}</h1>
        <p>{{ review.content }}</p>
      </div>
      <div class="review-detail-footer">
        <div class="movie-info">
          <p class="m-0 my-1">개봉 연도 : {{ review.movie.release_date }}</p>
          <p class="m-0 my-1">
            영화 평점 : {{ (review.movie.vote_average / 2).toFixed(1) }}
          </p>
        </div>
        <div class="d-flex justify-content-between">
          <div class="d-flex my-1">
            <p v-for="genreName in review.movie.genres" :key="genreName.name" class="m-0 category-button rounded me-2">
              {{ genreName.name }}
            </p>
          </div>
          <div class="d-flex review-delete-update" v-if="userTempStore.tempData && hasPermission">
            <!-- 리뷰 수정 버튼 -->
            <button class="review-button" style="color: #0077ff;" @click.prevent="updateReview(review.id)">
              <i class="fa-solid fa-pen"></i>
              <span class="mx-1">수정</span>
            </button>
            <!-- 리뷰 삭제 버튼 -->
            <button class="review-button ms-3" @click.prevent="deleteReview(review.id)" style="color: #d43f3f;">
              <i class="fa-solid fa-trash-can"></i>
              <span class="mx-1">삭제</span>
            </button>
          </div>
        </div>
      </div>
      <div class="vote-info">
        <i class="fa-solid fa-star" style="color: yellow; height: 25px"></i>
        <h4 class="m-0 mx-2">{{ review.vote }}</h4>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from "vue"
import { useRouter } from "vue-router"
import { useUserStore, useUserTempStore } from "@/stores/user"
import { useMovieStore } from "@/stores/movie"
import axios from "axios"

const router = useRouter()
const userStore = useUserStore()
const userTempStore = useUserTempStore()
const store = useMovieStore()

const props = defineProps({
  review: Object,
})

const hasPermission = computed(() => {
  if (props.review.user.username === userTempStore.tempData.username) {
    return true
  } else {
    return false
  }
})

const goProfile = function (username) {
  router.push({ name: "ProfileView", params: { username: username } })
}

const goDetailMovie = function (movieId) {
  router.push({ name: "DetailView", params: { tmdb_id: movieId } })
}

const deleteReview = function (reviewId) {
  axios({
    method: "delete",
    url: `${store.BASE_URL}/api/v1/movies/review/detail/${reviewId}/`,
    headers: {
      Authorization: `Token ${userStore.sessionData.token}`,
    },
  })
    .then(response => {
      // console.log(response)
      router.replace({ name: 'DetailView', params: { tmdb_id: props.review.movie.tmdb_id } })
    })
    .catch(error => {
      console.log(error)
    })
}

const updateReview = function (reviewId) {
  router.replace({ name: "ReviewUpdateView", params: { review_id: reviewId } })
}

const nickname = computed(() => {
  if (userStore.isLogin) {
    return userStore.sessionData.user.nickname
  }
})

onMounted(() => {
  userTempStore.checkPermission()
})
</script>

<style scoped>
.review-detail-top {
  display: flex;
}

.info {
  display: flex;
  align-items: center;
}

.vote-info {
  display: flex;
  align-items: center;
  position: absolute;
  right: 0;
  top: 0;
}
</style>
