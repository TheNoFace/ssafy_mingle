<template>
  <div v-if="userData" class="text-color">
    <h1 class="my-3">
      <i class="fa-regular fa-face-smile" style="color: #76abae;"></i>
      {{ userData.nickname }}님의 프로필
    </h1>
    <p class="m-0 my-2">@{{ userData.username}}</p>
    <p class="m-0 my-2">팔로잉: {{ userData.followings.length }} | 팔로워: {{ userData.followers.length }}</p>

    <!-- 아직 안함: 장르 카테고리 선택 시 카테고리 추천 페이지 이동 -->
    <div class="my-5">
      <h4 class="my-2">선호하는 장르</h4>
      <div class="d-flex flex-wrap">
        <p class="category-button rounded" v-for="genreName in userData.liked_genres" :key="genreName.name">{{ genreName.name }}</p>
      </div>
    </div>
    
    <!-- 아직 안함: 이미지 선택 시 영화 상세 페이지 이동 -->
    <div class="go-all-info">
      <h4 class="m-0">좋아하는 영화 {{ userData.liked_movies.length }}개</h4>
      <h5 class="m-0">영화 전체 보기</h5>
    </div>
    <div class="scroll-container">
      <MainRecommendCard
      v-for="movie in userData.liked_movies.slice(0, 10)"
      :key="movie.tmdb_id"
      :movie="movie"
      />
    </div>
    
    <!-- 아직 안함: 리뷰 선택 시 리뷰 상세 페이지 이동 -->
    <div class="mt-5">
      <div class="go-all-info">
        <h4 class="m-0">{{ userData.nickname }}님이 작성한 {{ userData.review_set.length }}개의 리뷰</h4>
        <h5 class="m-0">리뷰 전체 보기</h5>
      </div>
      <div v-for="review in userData.review_set.slice(0, 5)" :key="review.id" class="m-2">
        <AllReviewCard
        :review="review"
        />
      </div>
    </div>

    <!-- 댓글은 선택하면 어디로 가지...? -->
    <h4 class="m-0 mt-5">{{ userData.nickname }}님이 작성한 {{ userData.comment_set.length }}개의 댓글</h4>


    <div>
      <RouterLink :to="{ name: 'ProfileUpdateView' }" class="profile-change">
        <p class="profile-button rounded" style="width: 100px;">프로필 수정</p>
      </RouterLink>
      <button @click="logOut" class="profile-change profile-button rounded">로그아웃</button>
      <button @click="logOutAll" class="profile-change profile-button rounded">모든 기기에서 로그아웃</button>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user'
import { ref, onMounted } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import axios from 'axios'
import MainRecommendCard from '@/component/MainRecommendCard.vue'
import AllReviewCard from '@/component/AllReviewCard.vue'

const route = useRoute()
const userStore = useUserStore()
const userData = ref(null)

const logOut = function () {
  userStore.logOut()
}

const logOutAll = function () {
  userStore.logOutAll()
}

const getProfileDetail = function (userName) {
  axios({
    method: 'get',
    url: `${userStore.AUTH_BASE_URL}/profile/${userName}/detail/`,
  })
  .then((response) => {
    console.log(response.data)
    userData.value = response.data
  })
  .catch((error) => {
    console.log(error)
  })
}

onMounted(() => {
  getProfileDetail(route.params.username)
})
</script>

<style scoped>
.profile-button {
  border: 2px solid #76abae;
  margin: 0;
  margin: 0 10px 10px 10px;
  padding: 0 10px 0 10px;
}

.movie-image {
  width : 180px;
  height: 100%;
  margin: 10px;
}

.scroll-container {
  overflow-x: scroll;
  overflow-y: hidden;
  display: flex;
  flex-wrap: nowrap;
}
.scroll-container::-webkit-scrollbar {
    background-color: #ffffff00;
    height: 5px;
}

.scroll-container::-webkit-scrollbar-thumb {
    background-color: #76ABAE;
    border-radius: 5px;
}

.go-all-info {
  display: flex;
  justify-content: space-between;
}

.profile-change {
  color: white;
  text-decoration: none
}

.profile-logout {
  border: none;
  color: white;
}

.review-border {
  border: 2px #76ABAE solid;
  margin: 10px;
}
</style>