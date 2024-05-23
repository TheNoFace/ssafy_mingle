<template>
  <div class="text-color" v-if="reviewInfo">
    <h1>Review Update Page</h1>
    <form @submit.prevent="updateReview(reviewInfo.id)" ref="updateForm">
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
            <div class="star-rating space-x-4 mx-auto">
              <input type="radio" id="5-stars" name="vote" value="5" v-model="vote" />
              <label for="5-stars" class="star pr-4">★</label>
              <input type="radio" id="4-stars" name="vote" value="4" v-model="vote" />
              <label for="4-stars" class="star">★</label>
              <input type="radio" id="3-stars" name="vote" value="3" v-model="vote" />
              <label for="3-stars" class="star">★</label>
              <input type="radio" id="2-stars" name="vote" value="2" v-model="vote" />
              <label for="2-stars" class="star">★</label>
              <input type="radio" id="1-star" name="vote" value="1" v-model="vote" />
              <label for="1-star" class="star">★</label>
            </div>
          </div>
        </div>
      </div>

    <!-- 리뷰 수정 칸 -->
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

.star-rating {
  display: flex;
  flex-direction: row-reverse;
  font-size: 2.25rem;
  line-height: 2.5rem;
  justify-content: space-around;
  padding: 0 0.2em;
  text-align: center;
  width: 5em;
}
 
.star-rating input {
  display: none;
}
 
.star-rating label {
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 2.3px;
  -webkit-text-stroke-color: white;
  cursor: pointer;
}
 
.star-rating :checked ~ label {
  -webkit-text-fill-color: #ffff72;
  -webkit-text-stroke-color: #fff58c
}
 
.star-rating label:hover,
.star-rating label:hover ~ label {
  -webkit-text-fill-color: #fff58c;
  -webkit-text-stroke-color: #fff58c
}
</style>