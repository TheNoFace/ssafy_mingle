<template>
  <div
    class="review-border rounded p-2 scroll"
    @click.prevent="goDetailReview(review.id)"
  >
    <p class="m-0">
      <i class="fa-solid fa-circle-user" style="color: #76abae"></i>
      {{ review.user.nickname }}
    </p>
    <p class="m-0" style="width: 250px">
      {{ review.content.substring(0, 71) }}...
    </p>
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
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

defineProps({
  review: Object,
});

const goDetailReview = function (reviewId) {
  router.push({ name: "ReviewDetailView", params: { review_id: reviewId } });
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
}
</style>
