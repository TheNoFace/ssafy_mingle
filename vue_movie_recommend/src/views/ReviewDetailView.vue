<template>
  <div class="text-color" v-if="review">
    <!-- 영화, 리뷰 정보 -->
    <ReviewDetail :review="review" />

    <!-- 좋아요, 댓글 개수, 버튼 -->
    <div class="d-flex my-3 mb-5">
      <h3 class="m-0 ms-2" @click.prevent="likeReview(review.id)">
        <i class="fa-solid fa-thumbs-up me-2" style="height: 30px"></i>
        {{ review.liked_users.length }}
      </h3>
      <h3 class="m-0 ms-5">
        <i class="fa-solid fa-comments me-2" style="height: 30px"></i>
        {{ review.comment_set.length }}
      </h3>
    </div>

    <!-- 댓글 전체 -->
    <div v-for="comment in review.comment_set">
      <ReviewComment :comment="comment"/>
    </div>

    <!-- 댓글 작성 컴포넌트 -->
    <CommentForm />
  </div>
</template>

<script setup>
import ReviewDetail from "@/component/Review/ReviewDetail.vue";
import ReviewComment from "@/component/Review/ReviewComment.vue";
import CommentForm from "@/component/Review/CommentForm.vue";
import { onMounted, computed } from "vue";
import { useMovieStore } from "@/stores/movie";
import { useUserStore } from "@/stores/user";
import { useRoute, useRouter } from "vue-router";
import axios from 'axios'

const route = useRoute();
const router = useRouter()
const store = useMovieStore();
const userStore = useUserStore()

const reviewId = route.params.review_id;

onMounted(() => {
  store.getDetailReview(reviewId);
});

const review = computed(() => {
  return store.reviewDetail
})

const likeReview = function (reviewId) {
  axios({
    method : 'post',
    url : `${store.BASE_URL}/api/v1/movies/like/review/${reviewId}/`,
    headers: {
      Authorization: `Token ${userStore.sessionData.token}`,
    },
  })
    .then(response => {
      console.log(response.data)
      router.go()
    })
    .catch(error => {
      console.log(error)
    })
}
</script>

<style scoped></style>
