<template>
  <div>
    <nav class="navbar">
      <div class="nav-left">
        <div>
          <RouterLink :to="{ name: 'MainView' }">
            <i
              class="fa-solid fa-video p-3"
              style="color: #76abae; height: 30px"
            />
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
        <button
          v-if="!userStore.isLogin"
          type="button"
          class="btn nav-router"
          @click="launchModal"
        >
          Login
        </button>
        <LoginModal />
        <div v-if="userStore.isLogin">
          <RouterLink
            :to="{ name: 'ProfileView', params: { username: username } }"
          >
            <i
              class="fa-solid fa-user p-3"
              style="color: #76abae; height: 30px"
            />
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
import { computed } from "vue";
import { RouterLink } from "vue-router";
import LoginModal from "@/component/User/LoginModal.vue";
import { useUserStore } from "./stores/user";
import { Modal } from "bootstrap";

const userStore = useUserStore();
const username = computed(() => {
  if (userStore.isLogin) {
    return userStore.sessionData.user.username;
  }
});

const launchModal = function () {
  const logInModal = new Modal("#login", {
    backdrop: true,
  });
  logInModal.show();
};
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
</style>
