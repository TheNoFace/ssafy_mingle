<template>
  <div class="review-card-border rounded p-2" style="position: relative">
    <div class="d-flex">
      <div class="col-1">
        <img :src="`https://image.tmdb.org/t/p/original${review.movie.poster_path}`" :alt="review.movie.title" width="100%">
      </div>
      <div class="mx-3">
        <h4 class="m-0">{{ review.title }}</h4>
        <h6 class="m-0 my-3">
          <i class="fa-solid fa-star" style="color: yellow;"></i>
          {{ review.vote }}
        </h6>
        <p class="m-0 mt-2">{{ review.content }}</p>
      </div>
      <h6 class="m-0 create-position">{{ review.created_at.substring(0, 10) }}</h6>
    </div>
    <div class="d-flex mt-2">
      <h6 class="m-0 ms-2">
        <i class="fa-solid fa-thumbs-up"></i>
        {{ review.liked_users_count }}
      </h6>
      <h6 class="m-0 ms-2">
        <i class="fa-solid fa-comments"></i>
        {{ review.comment_count }}
      </h6>
    </div>
  </div>
  

</template>

<script setup>
const props = defineProps({
  review : Object
})
</script>

<style scoped>
.review-card-border {
  border: 2px white solid
}

.create-position {
  position: absolute;
  right: 10px;
  top: 10px;
}
</style>