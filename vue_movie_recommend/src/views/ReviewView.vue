<template>
  <div class="text-color">
    <div v-for="review in store.reviewList" :key="review.id" class="m-3">
      <AllReviewCard :review="review" />
    </div>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useMovieStore } from "@/stores/movie";
import AllReviewCard from "@/component/Review/AllReviewCard.vue";

const store = useMovieStore();

onMounted(() => {
  store.getReviewList();
});
</script>

<style scoped></style>
