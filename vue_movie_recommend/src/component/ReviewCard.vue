<template>
  <div class="review-border rounded p-2 scroll">
    <p class="m-0">
      <i class="fa-solid fa-circle-user" style="color: #76ABAE;"></i>
      {{ review.user.nickname }}
    </p>
    <p class="m-0" style="width: 250px;">{{ review.content.substring(0, 71) }}...</p>
    <!-- 댓글 갯수, 좋아요 갯수 -->
    <div class="review-count mt-1">
      <p class="m-0 me-2"><i class="fa-solid fa-comments mx-1"></i>댓글 갯수</p>
      <p class="m-0"><i class="fa-solid fa-thumbs-up mx-1"></i>{{ review.liked_users_count }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  review : Object
})
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