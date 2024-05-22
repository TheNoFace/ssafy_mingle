<template>
  <div>
    <nav class="navbar">
      <div class="nav-left">
        <div>
          <RouterLink :to="{ name: 'MainView' }">
            <i class="fa-solid fa-video p-3" style="color: #76abae; height: 30px" />
          </RouterLink>
        </div>
        <div class="nav-standard">
          <RouterLink :to="{ name: 'CategoryView' }" class="nav-router">
            Category
          </RouterLink>
          <RouterLink :to="{ name: 'ReviewView' }" class="nav-router">
            Review
          </RouterLink>
        </div>
      </div>
      <div class="nav-right">
        <button v-if="!userStore.isLogin" type="button" class="btn nav-router login me-3" @click="launchModal">
          Login
        </button>
        <LoginModal />
        <div v-if="userStore.isLogin && userTempStore.tempData" class="d-flex align-items-center">
          <p class="m-0 text-color">{{ userTempStore.tempData.nickname }}</p>
          <RouterLink :to="{ name: 'ProfileView', params: { username: username } }">
            <i class="fa-solid fa-user p-3" style="color: #76abae; height: 30px" />
          </RouterLink>
        </div>
      </div>
    </nav>

    <div class="container">
      <!-- searchBox -->
      <div class="search-box">
        <div class="input-group mb-3">
          <label class="input-group-text inputBox" for="searchBox">
            <i class="fa-solid fa-magnifying-glass" style="color: white"></i>
          </label>
          <input type="text" class="form-control inputBox" id="searchBox" :value="searchText"
            @input="(event) => (searchText = event.target.value)" v-debounce:500ms="search" />
        </div>
      </div>

      <!-- 메인 추천 페이지 -->
      <div v-if="!searchText">
        <RouterView />
      </div>

      <div v-else>
        <p class="text-color">총 {{ store.searchMovieList.total_results }}개의 검색 결과가 있습니다.</p>
        <SearchMovie :movies="store.searchMovieList.results" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from "vue"
import { RouterLink } from "vue-router"
import { useUserStore, useUserTempStore } from "./stores/user"
import { useMovieStore } from "@/stores/movie"
import { Modal } from "bootstrap"
import LoginModal from "@/component/User/LoginModal.vue"
import SearchMovie from "@/component/Search/SearchMovie.vue"
import vueDebounce from 'vue-debounce'

const vDebounce = vueDebounce({ lock: true })
const userStore = useUserStore()
const userTempStore = useUserTempStore()
const store = useMovieStore()
const searchText = ref(null)

const username = computed(() => {
  if (userStore.isLogin) {
    return userStore.sessionData.user.username
  }
})

const launchModal = function () {
  const logInModal = new Modal("#login", {
    backdrop: true,
  })
  logInModal.show()
}

onMounted(() => {
  userTempStore.checkPermission()
})

const search = function () {
  // console.log(searchText.value)
  store.searchMovie(searchText.value)
}
</script>

<style scoped>
* {
  font-family: Pretendard;
}

nav {
  display: flex;
  justify-content: space-between;
}

.nav-left {
  display: flex;
}

.nav-right {
  display: flex;
}

.nav-standard {
  display: flex;
  align-items: center;
}

.nav-router:hover {
  color: #76abae;
}

.search-box {
  margin: 50px;
}

.inputBox {
  border-color: white;
  background-color: rgba(255, 255, 255, 0);
  color: white;
}
</style>

<style>
@import url("https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard-dynamic-subset.min.css");

* {
  background-color: #222831;
}

.text-color {
  color: white;
}

.nav-router {
  color: white;
  text-decoration: none;
  padding-left: 10px;
  padding-right: 10px;
  font-size: large;
}

.category-button {
  border: 2px solid #76abae;
  margin: 0;
  margin: 0 10px 10px 10px;
  padding: 0 10px 0 10px;
}

::-webkit-scrollbar {
  background-color: #ffffff00;
  height: 5px;
}

::-webkit-scrollbar-thumb {
  background-color: #76abae;
  border-radius: 10px;
}
</style>
