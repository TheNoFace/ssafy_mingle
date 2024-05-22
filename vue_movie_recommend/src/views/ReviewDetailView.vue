<template>
  <div class="text-color">
    <!-- 영화, 리뷰 정보 -->
    <ReviewDetail :review="review" />

    <!-- 좋아요, 댓글 개수, 버튼 -->
    <div class="d-flex my-3 mb-5">
      <h3 class="m-0 ms-2">
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
      <ReviewComment :comment="comment" />
    </div>

    <!-- 댓글 작성 컴포넌트 -->
    <CommentForm />
  </div>
</template>

<script setup>
import ReviewDetail from "@/component/ReviewDetail.vue";
import ReviewComment from "@/component/ReviewComment.vue";
import CommentForm from "@/component/CommentForm.vue";
import { onMounted, ref } from "vue";
import { useMovieStore } from "@/stores/movie";
import { useRoute } from "vue-router";

const route = useRoute();
const store = useMovieStore();

const reviewId = route.params.review_id;

onMounted(() => {
  store.getDetailReview(reviewId);
});

const review = ref(store.reviewDetail);
</script>

<style scoped></style>
