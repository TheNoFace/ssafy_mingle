<template>
  <div>
    <div class="d-flex justify-content-between" style="position: relative;">
      <div class="comment-user">
        <i class="fa-solid fa-user"></i>
        <p class="m-0 ms-2">{{ comment.user.nickname }}</p>
      </div>
      <div class="d-flex comment-delete-update" v-if="userStore.isLogin && nickname === comment.user.nickname">
        <!-- 댓글 수정 버튼 -->
        <button class="comment-button" style="color: #0077ff;" @click.prevent="showCommentForm(comment.id)">
          <i class="fa-solid fa-pen"></i>
        </button>
        <!-- 댓글 삭제 버튼 -->
        <button class="comment-button" @click.prevent="deleteComment(comment.id)" style="color: #d43f3f;">
          <i class="fa-solid fa-trash-can"></i>
        </button>
      </div>
    </div>
    <p class="m-0 my-2">{{ comment.content }}</p>
    <div class="comment-user thumbs-up" @click.prevent="likeComment(comment.id)">
      <i class="fa-solid fa-thumbs-up"></i>
      <p class="m-0 ms-2">{{ comment.liked_users.length }}</p>
    </div>

    <!-- 댓글 수정 폼 -->
    <div v-show="show">
      <form @submit.prevent="updateComment(comment.id)" class="d-flex mt-2" ref="updateForm">
        <input type="text" class="form-control comment-input" :placeholder="comment.content" name="content"/>
        <input type="submit" class="comment-input-btn rounded" value="댓글 수정" />
      </form>
    </div>
    <hr />
  </div>
</template>

<script setup>
import axios from 'axios'
import { computed, ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore, useUserTempStore } from '@/stores/user';
import { useMovieStore } from '@/stores/movie';

const userStore = useUserStore()
const userTempStore = useUserTempStore()
const store = useMovieStore()
const router = useRouter()
const route = useRoute()

const reviewId = route.params.review_id

const props = defineProps({
  comment: Object,
});

const deleteComment = function (commentId) {
  axios({
    method: 'delete',
    url: `${store.BASE_URL}/api/v1/movies/comment/${commentId}`,
    headers: {
      Authorization: `Token ${userStore.sessionData.token}`,
    },
  })
    .then(response => {
      console.log('delete')
      store.getDetailReview(reviewId)
      // router.go()
    })
    .catch(error => {
      console.log(error)
    })
}

const nickname = computed(() => {
  if (userStore.isLogin) {
    return userStore.sessionData.user.nickname
  }
})

const show = ref(false)
const showCommentForm = function () {
  show.value = !show.value
  console.log(!show.value)
}

const updateForm = ref(null)
const updateComment = function (commentId) {
  const payload = new FormData(updateForm.value)
  // console.log(payload.getAll())
  store.updateComment(payload, commentId, reviewId)
}

const likeComment = function (commentId) {
  axios({
    method : 'post',
    url : `${store.BASE_URL}/api/v1/movies/like/comment/${commentId}/`,
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

<style scoped>
.comment-user {
  display: flex;
  align-items: center;
}

.thumbs-up {
  justify-content: end;
}

.comment-input {
  width: 100%;
  margin-right: 10px;
  background-color: #ffffff00;
  color: white;
}

.comment-input-btn {
  border: 2px solid #76abae;
  color: white;
}

.comment-input::placeholder {
  color: white;
}

.comment-delete-update {
  position: absolute;
  right: 0;
  top: 0;
}

.comment-button {
  border: none;
}
</style>
