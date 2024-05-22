<template>
  <!-- 아직 안함: 이미지 선택 시 영화 상세 페이지 이동 -->
  <div v-if="userData" class="mt-5">
    <div>
      <h4 class="m-0">좋아하는 영화 {{ userData.liked_movies.length }}개</h4>
    </div>
    <div class="d-flex flex-wrap">
      <div
        v-for="movie in userData.liked_movies"
        :key="movie.tmdb_id"
        :movie="movie"
      >
        <div>
          <img
            :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`"
            :alt="movie.title"
            width="190px;"
            style="margin: 10px"
            @click="godetail(movie.tmdb_id)"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";

const route = useRoute();
const router = useRouter();
const userStore = useUserStore();
const userData = ref(null);

const getProfileDetail = function (userName) {
  axios({
    method: "get",
    url: `${userStore.AUTH_BASE_URL}/profile/${userName}/detail/`,
  })
    .then((response) => {
      console.log(response.data);
      userData.value = response.data;
    })
    .catch((error) => {
      console.log(error);
    });
};

onMounted(() => {
  getProfileDetail(route.params.username);
});

const godetail = function (tmdb_id) {
  router.push({ name: "DetailView", params: { tmdb_id: tmdb_id } });
};
</script>

<style scoped></style>
