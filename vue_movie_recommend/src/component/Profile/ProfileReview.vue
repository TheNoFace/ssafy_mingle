<template>
  <div class="mt-5" v-if="userData">
    <div>
      <h4 class="m-0">
        {{ userData.nickname }}님이 작성한 {{ userData.review_set.length }}개의
        리뷰
      </h4>
    </div>
    <div v-for="review in userData.review_set" :key="review.id" class="m-2">
      <AllReviewCard :review="review" />
    </div>
  </div>
</template>

<script setup>
import AllReviewCard from "@/component/Review/AllReviewCard.vue";
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
