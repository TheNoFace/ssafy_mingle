<template>
  <div>
    <nav>
      <div class="nav-left">
        <div>
          <RouterLink :to="{ name: 'MainView' }">
            <i
              class="fa-solid fa-video p-3"
              style="color: #76abae; height: 30px"
            ></i>
          </RouterLink>
        </div>
        <div class="nav-standard">
          <RouterLink :to="{ name: 'CategoryView' }" class="nav-router"
            >Category</RouterLink
          >
          <RouterLink :to="{ name: 'ReviewView' }" class="nav-router"
            >Review</RouterLink
          >
        </div>
      </div>
      <div class="nav-right">
        <button
          type="button"
          class="btn nav-router"
          data-bs-toggle="modal"
          data-bs-target="#login"
        >
          Login
        </button>
        <LoginModal />
        <RouterLink :to="{ name: 'ProfileView' }">
          <i
            class="fa-solid fa-user p-3"
            style="color: #76abae; height: 30px"
          ></i>
        </RouterLink>
      </div>
    </nav>

    <div class="container">
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from "vue-router";
import LoginModal from "@/component/LoginModal.vue";
</script>

<style scoped>
* {
  font-family: Pretendard;
}

nav {
  display: flex;
  justify-content: space-between;
}

.nav-router {
  color: white;
  text-decoration: none;
  padding-left: 10px;
  padding-right: 10px;
  font-size: large;
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
</style>
