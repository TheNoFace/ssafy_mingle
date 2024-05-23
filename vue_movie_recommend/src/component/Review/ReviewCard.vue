<template>
  <div class="review-border rounded p-2" style="position: relative">
    <!-- ReviewCard Header-->
    <div class="container d-flex justify-content-between">
      <div>
        <p class="m-0">
          <i class="fa-solid fa-circle-user" style="color: #76abae"></i>
          <span class="ms-2">{{ review.user.nickname }}</span>
        </p>
      </div>
      <!-- <div class="review-count mt-1"> -->
      <div class="d-flex">
        <p class="m-0">
          <i class="fa-solid fa-thumbs-up mx-1"></i>
          <span class="mx-1">{{ review.liked_users.length }}</span>
        </p>
        <p class="m-0 me-2">
          <i class="fa-solid fa-comments mx-1"></i>
          <span class="ms-1">{{ review.comment_set.length }}</span>
        </p>
      </div>
    </div>

    <div class="p-2 scroll" @click.prevent="goDetailReview(review.id)" style="position: relative">
      <p class="m-0 mb-4 fw-bold fs-5" style="width: 250px">
        {{ review.title }}
      </p>
      <p class="m-0 mb-4" style="width: 250px">
        {{ review.content.substring(0, 71) }}...
      </p>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router"

const router = useRouter()

defineProps({
  review: Object,
})

const goDetailReview = function (reviewId) {
  router.push({ name: "ReviewDetailView", params: { review_id: reviewId } })
}
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

.review-delete-update {
  position: absolute;
  right: 0;
  top: 0;
}

.review-button {
  border: none;
}
</style>
