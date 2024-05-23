<template>
  <div class="review-card-border rounded p-2" style="position: relative" @click.prevent="goDetailReview(review.id)">
    <div class="d-flex">
      <div class="col-1">
        <img :src="`https://image.tmdb.org/t/p/original${review.movie.poster_path}`" :alt="review.movie.title"
          width="100%" />
      </div>
      <div class="mx-3">
        <h4 class="m-0">{{ review.title }}</h4>
        <h6 class="m-0 my-3">
          <i class="fa-solid fa-star" style="color: yellow"></i>
          {{ review.vote }}
        </h6>
        <p class="m-0 mt-2">{{ review.content }}</p>
      </div>
      <h6 class="m-0 create-position">
        {{ review.created_at.substring(0, 10) }}
      </h6>
    </div>
    <div class="d-flex mt-2">
      <h6 class="m-0 ms-2">
        <i class="fa-solid fa-thumbs-up"></i>
        {{ review.liked_users.length }}
      </h6>
      <h6 class="m-0 ms-2">
        <i class="fa-solid fa-comments"></i>
        {{ review.comment_set.length }}
      </h6>
    </div>

    <!-- 버튼 -->
    <div class="d-flex review-delete-update" v-if="nickname === review.user.nickname">
      <!-- 리뷰 수정 버튼 -->
      <button class="review-button" style="color: #0077ff;" @click.prevent="updateReview(review.id)">
        <i class="fa-solid fa-pen"></i>
      </button>
      <!-- 리뷰 삭제 버튼 -->
      <button class="review-button" @click.prevent="deleteReview(review.id)" style="color: #d43f3f;">
        <i class="fa-solid fa-trash-can"></i>
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useRouter } from "vue-router";
import { useUserStore } from "@/stores/user";
import { useMovieStore } from "@/stores/movie";

const router = useRouter();
const userStore = useUserStore()
const store = useMovieStore();

const props = defineProps({
  review: Object,
});

const goDetailReview = function (reviewId) {
  console.log(update.value)
  if (update.value === false) {
    router.push({ name: "ReviewDetailView", params: { review_id: reviewId } })
  }
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

const update = ref(false)
const updateReview = function (reviewId) {
  update.value = !update.value
  router.push({ name: "ReviewUpdateView", params: { review_id: reviewId } })
}

const nickname = computed(() => {
  if (userStore.isLogin) {
    return userStore.sessionData.user.nickname
  }
})

</script>

<style scoped>
.review-card-border {
  border: 2px white solid;
}

.create-position {
  position: absolute;
  right: 10px;
  top: 10px;
}

.review-delete-update {
  position: absolute;
  right: 0;
  bottom: 0;
}

.review-button {
  border: none;
}
</style>
