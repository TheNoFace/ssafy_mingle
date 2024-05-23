<template>
  <div v-if="userData" class="text-color">
    <h1 class="my-3">
      <i class="fa-regular fa-face-smile" style="color: #76abae"></i>
      {{ userData.nickname }}님의 프로필
    </h1>
    <p class="m-0 my-2">@{{ userData.username }}</p>
    <p class="m-0 my-2">
      팔로잉: {{ userData.followings.length }} | 팔로워:
      {{ userData.followers.length }}
    </p>


    <div>
      <div class="d-flex" v-if="userTempStore.hasPermission"> 
        <RouterLink :to="{ name: 'ProfileUpdateView' }" class="profile-change">
          <p class="profile-button rounded ms-0" style="width: 100px">
            프로필 수정
          </p>
        </RouterLink>
        <button @click="logOut" class="profile-change profile-button rounded">
          로그아웃
        </button>
        <button @click="logOutAll" class="profile-change profile-button rounded">
          모든 기기에서 로그아웃
        </button>
      </div>
  
      <div v-else>
        <div v-if="userData">
          <button class="profile-change profile-button rounded" @click="followClick(userData.username)">
            {{ isFollowing }}
          </button>
        </div>
      </div>
    </div>

    <RouterLink :to="{ name: 'ProfileGenre' }" class="nav-router ps-0">Genre</RouterLink>
    <RouterLink :to="{ name: 'ProfileMovie' }" class="nav-router">Movie</RouterLink>
    <RouterLink :to="{ name: 'ProfileReview' }" class="nav-router">Review</RouterLink>
    <RouterLink :to="{ name: 'ProfileComment' }" class="nav-router">Comment</RouterLink>

    <RouterView />
  </div>
</template>

<script setup>
import { useUserStore, useUserTempStore } from "@/stores/user"
import { ref, onMounted, computed } from "vue"
import { useRoute, RouterLink, RouterView } from "vue-router"
import axios from "axios"

const route = useRoute()
const userStore = useUserStore()  // 현재 프로필 사용자 정보
const userTempStore = useUserTempStore()  // 현재 요청한 사용자 정보
const userData = ref(null)

const isFollowing = computed(() => {
  return userData.value.followers.find(id => id === userTempStore.tempData.id) ? '팔로우 취소' : '팔로우'
})

const logOut = function () {
  userStore.logOut()
}

const logOutAll = function () {
  userStore.logOutAll()
}

const followClick = function (userName) {
  console.log('clicked')
  followUser(userName)
}

const getProfileDetail = function (userName) {
  axios({
    method: "get",
    url: `${userStore.AUTH_BASE_URL}/profile/${userName}/detail/`,
  })
    .then((response) => {
      userData.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
}

const followUser = function (userName) {
    axios({
      method: "put",
      url: `${userStore.AUTH_BASE_URL}/profile/${userName}/follow/`,
      headers: {
        Authorization: `Token ${userStore.sessionData.token}`,
      },
    })
      .then((response) => {
        getProfileDetail(userName)
      })
      .catch((error) => {
        console.log(error)
      })
  }

onMounted(() => {
  userTempStore.checkPermission(route.params.username)
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

.profile-change {
  color: white;
  text-decoration: none;
}

.profile-logout {
  border: none;
  color: white;
}

.review-border {
  border: 2px #76abae solid;
  margin: 10px;
}

.profile-button:hover {
  background-color: #76abae;
  color: black;
}

.nav-router:hover {
  color: #76abae;
}
</style>
