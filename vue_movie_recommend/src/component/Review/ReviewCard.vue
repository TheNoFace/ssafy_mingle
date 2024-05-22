<template>
  <div class="review-border rounded" style="position: relative">
    <div
      class="p-2 scroll"
      @click.prevent="goDetailReview(review.id)"
      style="position: relative"
    >
      <p class="m-0">
        <i class="fa-solid fa-circle-user" style="color: #76abae"></i>
        {{ review.user.nickname }}
      </p>
      <p class="m-0 mb-4" style="width: 250px">
        {{ review.content.substring(0, 71) }}...
      </p>
    </div>
    <!-- 댓글 갯수, 좋아요 갯수 -->
    <div class="review-count mt-1">
      <p class="m-0">
        <i class="fa-solid fa-thumbs-up mx-1"></i
        >{{ review.liked_users.length }}
      </p>
      <p class="m-0 me-2">
        <i class="fa-solid fa-comments mx-1"></i>{{ review.comment_set.length }}
      </p>
    </div>
    <!-- 리뷰 삭제 버튼 -->
    <button class="review-delete" @click.prevent="deleteReview(review.id)">
      <i class="fa-solid fa-trash-can"></i>
    </button>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { useUserStore } from "@/stores/user";
import { useMovieStore } from "@/stores/movie";
import axios from "axios";

const router = useRouter();
const userStore = useUserStore();
const store = useMovieStore();

defineProps({
  review: Object,
});

const goDetailReview = function (reviewId) {
  router.push({ name: "ReviewDetailView", params: { review_id: reviewId } });
};

const deleteReview = function (reviewId) {
  axios({
    method: "delete",
    url: `${store.BASE_URL}/api/v1/movies/review/detail/${reviewId}/`,
    headers: {
      Authorization: `Token ${userStore.sessionData.token}`,
    },
  })
    .then(response => {
      console.log(response)
      router.go()
    })
    .catch(error => {
      console.log(error)
    })
};
</script>

<style scoped>
.scroll {
  display: inline-block;
}

.review-border {
  border: 2px white solid;
  margin-right: 15px;
}

.review-count {
  display: flex;
  justify-content: end;
  position: absolute;
  right: 0;
  bottom: 5px;
}

.review-delete {
  position: absolute;
  right: 0;
  top: 0;
  border: none;
  color: rgb(212, 63, 63);
}
</style>
