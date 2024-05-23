<template>
  <div>
    <form @submit.prevent="createComment" class="d-flex mb-5">
      <input
        type="text"
        v-model.trim="content"
        class="form-control comment-input"
        placeholder="댓글을 입력하세요."
      />
      <input
        type="submit"
        class="comment-input-btn rounded"
        value="댓글 작성"
      />
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";
import { useMovieStore } from "@/stores/movie";
import { useUserStore } from "@/stores/user";

const store = useMovieStore();
const userStore = useUserStore();
const route = useRoute();
const router = useRouter()

const content = ref(null);
const reviewId = route.params.review_id;

const createComment = function () {
  console.log(reviewId);
  axios({
    method: "post",
    url: `${store.BASE_URL}/api/v1/movies/review/detail/${reviewId}/`,
    data: {
      content: content.value,
    },
    headers: {
      Authorization: `Token ${userStore.sessionData.token}`,
    },
  })
    .then((response) => {
      console.log(response);
      router.go()
    })
    .catch((error) => {
      console.log(error);
    });
};
</script>

<style scoped>
.comment-input {
  width: 100%;
  margin-right: 10px;
  background-color: #ffffff00;
  color: white;
}

.comment-input-btn {
  border: 2px solid #76abae;
  color: white;
}

.comment-input::placeholder {
  color: white;
}
</style>
