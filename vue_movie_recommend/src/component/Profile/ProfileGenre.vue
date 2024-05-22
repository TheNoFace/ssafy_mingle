<template>
  <!-- 아직 안함: 장르 카테고리 선택 시 카테고리 추천 페이지 이동 -->
  <div class="my-5" v-if="userData">
    <h4 class="my-2">선호하는 장르</h4>
    <div class="d-flex flex-wrap">
      <p
        class="category-button rounded"
        v-for="genreName in userData.liked_genres"
        :key="genreName.name"
      >
        {{ genreName.name }}
      </p>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

const route = useRoute();
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
</script>

<style scoped>
.category-button:hover {
  background-color: #76abae;
  color: black;
}
</style>
