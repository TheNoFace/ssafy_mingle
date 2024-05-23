<template>
  <div class="review-detail-top">
    <div class="col-3">
      <img
        :src="`https://image.tmdb.org/t/p/original${review.movie.poster_path}`"
        :alt="review.movie.title"
        style="width: 100%"
      />
    </div>
    <div class="m-4 col-9" style="position: relative">
      <div>
        <div class="d-flex justify-content-between">
          <div class="info">
            <i
              class="fa-regular fa-face-smile"
              style="color: #76abae; height: 45px"
            ></i>
            <h4 class="m-0 mx-3">{{ review.user.nickname }}</h4>
          </div>
        </div>
        <h1 class="m-0 my-4">{{ review.title }}</h1>
        <p>{{ review.content }}</p>
      </div>
      <div class="movie-info">
        <p class="m-0 my-1">개봉 연도 : {{ review.movie.release_date }}</p>
        <p class="m-0 my-1">영화 평점 : {{ (review.movie.vote_average/2).toFixed(1) }}</p>
        <div class="d-flex my-1">
          <p
            v-for="genreName in review.movie.genres"
            :key="genreName.name"
            class="m-0 category-button rounded me-2"
          >
            {{ genreName.name }}
          </p>
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
defineProps({
  review: Object,
});
</script>

<style scoped>
.review-detail-top {
  display: flex;
}

.info {
  display: flex;
  align-items: center;
}

.movie-info {
  position: absolute;
  left: 0;
  bottom: 0;
}

.vote-info {
  display: flex;
  align-items: center;
  position: absolute;
  right: 0;
  top: 0;
}
</style>
