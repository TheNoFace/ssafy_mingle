<template>
  <div v-if="userData">
    <h1>프로필 수정</h1>
    <form ref="updateForm" @submit.prevent="updateProfile">
      <input class="form-control login-form-inner" type="text" :placeholder="`현재 닉네임: ${userData.nickname}`" name="nickname">
      <input class="form-control login-form-inner" type="password" placeholder="비밀번호를 입력하세요." name="password">
      <input class="form-control login-form-submit" type="submit" value="정보 수정">
    </form>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user'
import { ref, computed } from 'vue'

const userStore = useUserStore()
const userData = computed(() => {
  return userStore.userData
})

const updateForm = ref(null)
const updateProfile = function () {
  const payload = new FormData(updateForm.value)
  userStore.updateProfile(payload)
}
</script>

<style scoped>

</style>