<template>
  <div class="text-color">
    <div class="review-text">
      <h4 class="my-auto">등록된 리뷰</h4>
      <h6 class="m-0 my-auto" @click="goMovieReview()">
        리뷰 전체 보기
      </h6>
    </div>
    <div class="d-flex scroll-container py-5">
      <ReviewCard
        v-for="review in reviews.slice(0, 5)"
        :key="review.id"
        :review="review"
      />
    </div>
    <div class="write-review" @click.prevent="goReviewWrite()">
      <i class="fa-solid fa-pen" style="color: #76abae"></i>
      <p class="m-0 ms-2 ">리뷰 작성하기</p>
    </div>
  </div>
</template>

<script setup>
import ReviewCard from "@/component/Review/ReviewCard.vue";
import { useRouter } from "vue-router";

const router = useRouter();

defineProps({
  reviews: Array,
});

const goMovieReview = function () {
  router.push({ name: "MovieReviewView" });
};

const goReviewWrite = function () {
  router.push({ name: "ReviewFormView" });
};
</script>

<style scoped>
.scroll-container {
  overflow-x: scroll;
  overflow-y: hidden;
  display: flex;
  flex-wrap: nowrap;
  padding: 10px;
}

.scroll-container::-webkit-scrollbar {
  background-color: #ffffff00;
  height: 5px;
}

.scroll-container::-webkit-scrollbar-thumb {
  background-color: #76abae;
  border-radius: 5px;
}

.category-name {
  width: 10%;
  text-align: center;
  border: 2px solid #76abae;
}

.review-text {
  display: flex;
  justify-content: space-between;
  text-align: center;
}

.write-review {
  display: flex;
  align-items: center;
  margin-bottom: 100px;
}
</style>
