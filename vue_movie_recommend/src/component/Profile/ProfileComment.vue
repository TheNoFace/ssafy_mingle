<template>
  <div v-if="userData">
    <div class="mt-5">
      <h4 class="m-0">
        {{ userData.nickname }}님이 작성한 {{ userData.comment_set.length }}개의
        댓글
      </h4>
    </div>
    <div
      v-for="comment in userData.comment_set"
      :key="comment.id"
      class="container mt-3"
    >
      <ReviewComment :comment="comment" />
    </div>
  </div>
</template>

<script setup>
import ReviewComment from "@/component/Review/ReviewComment.vue";
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

<style scoped></style>
