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
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from "vue"
import { RouterLink } from "vue-router"
import { useUserStore, useUserTempStore } from "./stores/user"
import { Modal } from "bootstrap"
import LoginModal from "@/component/User/LoginModal.vue"

const userStore = useUserStore()
const userTempStore = useUserTempStore()

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
