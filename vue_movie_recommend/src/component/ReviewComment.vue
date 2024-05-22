<template>
  <div>
    <div class="comment-user">
      <i class="fa-solid fa-user"></i>
      <p class="m-0 ms-2">{{ comment.user.nickname }}</p>
    </div>
    <p class="m-0 my-2">{{ comment.content }}</p>
    <div class="comment-user thumbs-up">
      <i class="fa-solid fa-thumbs-up"></i>
      <p class="m-0 ms-2">{{ comment.liked_users.length }}</p>
    </div>
    <hr />
  </div>
</template>

<script setup>
defineProps({
  comment: Object,
});
</script>

<style scoped>
.comment-user {
  display: flex;
  align-items: center;
}

.thumbs-up {
  justify-content: end;
}
</style>
