<template>
  <div v-if="userData">
    <h1>프로필</h1>
    <p>아이디: {{ route.params.username }}</p>
    <p>닉네임: {{ userData.nickname }}</p>
    <RouterLink :to="{ name: 'ProfileUpdateView' }">프로필 수정</RouterLink>
    <button @click="logOut">로그아웃</button>
    <button @click="logOutAll">모든 기기에서 로그아웃</button>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user'
import { computed, onMounted } from 'vue'
import { useRoute, RouterLink } from 'vue-router'

const route = useRoute()
const userStore = useUserStore()
const userData = computed(() => {
  return userStore.userData
})

const logOut = function () {
  userStore.logOut()
}

const logOutAll = function () {
  userStore.logOutAll()
}

onMounted(() => {
  userStore.getProfile(route.params.username)
})
</script>

<style scoped>

</style>