<template>
  <div class="text-color" v-if="movie">
    <h1>리뷰 작성 페이지</h1>
    <!-- 영화 정보 -->
    <div class="movie-info-border rounded d-flex" style="padding: 10px">
      <div class="col-1">
        <img
          :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`"
          :alt="movie.title"
          style="width: 100px"
        />
      </div>
      <div class="ms-2 col-11" style="position: relative">
        <h1>{{ movie.title }}</h1>
        <div class="movie-info">
          <p class="m-1">평점 : {{ movie.vote_average }}</p>
          <div class="d-flex">
            <p
              v-for="genre in movie.genres"
              class="category-button rounded ms-0"
            >
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

    <!-- 리뷰 작성 폼 -->
    <form @submit.prevent="createReview">
      <input
        class="form-control review-input"
        type="text"
        placeholder="제목을 입력하세요."
        v-model.trim="title"
      />
      <textarea
        class="form-control review-input"
        type="text"
        placeholder="리뷰 내용을 입력하세요."
        style="height: 300px"
        v-model.trim="content"
      ></textarea>
      <div class="d-flex justify-content-end">
        <input
          class="review-submit rounded px-3 py-1"
          type="submit"
          value="리뷰 등록"
        />
      </div>
    </form>
  </div>
</template>

<script setup>
import { useMovieStore } from "@/stores/movie";
import { useUserStore } from "@/stores/user";
import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";

const store = useMovieStore();
const userStore = useUserStore();
const route = useRoute();
const router = useRouter();

const tmdbId = route.params.tmdb_id;
const movie = ref(null);
const title = ref(null);
const content = ref(null);
const vote = ref(null);

onMounted(() => {
  store.getDetailMovie(tmdbId);
  movie.value = store.detailMovie;
});

const createReview = function () {
  axios({
    method: "post",
    url: `${store.BASE_URL}/api/v1/movies/detail/${tmdbId}/review/`,
    data: {
      title: title.value,
      content: content.value,
      vote: 5.0,
    },
    headers: {
      Authorization: `Token ${userStore.sessionData.token}`,
    },
  })
    .then((response) => {
      // console.log(response);
      router.push({ name: "DetailView" });
    })
    .catch((error) => {
      console.log(error);
    });
};
</script>

<style scoped>
.movie-info-border {
  border: 2px solid #76abae;
}

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
