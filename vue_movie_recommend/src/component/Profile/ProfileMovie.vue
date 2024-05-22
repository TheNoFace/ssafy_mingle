<template>
  <div v-if="userData" class="mt-5">
    <div>
      <h4 class="m-0">좋아하는 영화 {{ userData.liked_movies.length }}개</h4>
    </div>
    <div class="d-flex flex-wrap mt-3">
      <div v-for="movie in userData.liked_movies" :key="movie.tmdb_id" :movie="movie">
        <div id="box">
          <img :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" :alt="movie.title" width="190px;"
            style="margin: 10px" @click="godetail(movie.tmdb_id)" />
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

<style scoped>
img {
  border-radius: 20px;
}

#box {
  width: 100%;
  height: 100%;
  border-radius: 8px;
  overflow: hidden;
  transition: all 0.1s cubic-bezier(0.42, 0.0, 0.58, 1.0);
}

#box:hover {
  transform: translateY(-10px);
}

#box .img {
  display: block;
  width: inherit;
  height: inherit;
  ;
  padding: 0;

}
</style>
