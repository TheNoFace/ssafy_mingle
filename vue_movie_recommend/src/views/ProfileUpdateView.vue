<template>
  <div v-if="userData">
    <h1 class="text-color">프로필 수정</h1>
    <form ref="updateForm" @submit.prevent="updateProfile">
      <input class="form-control update-form-inner my-3" type="text" :placeholder="`현재 닉네임: ${userData.nickname}`"
        name="nickname" />
      <input class="form-control update-form-inner my-3" type="password" placeholder="비밀번호를 입력하세요." name="password" />
      <input class="form-control update-form-submit" type="submit" value="정보 수정" />
    </form>
  </div>
</template>

<script setup>
import { useUserStore, useUserTempStore } from "@/stores/user"
import { ref, computed, onMounted } from "vue"

const userStore = useUserStore()
const userTempStore = useUserTempStore()
const userData = computed(() => {
  return userTempStore.tempData
})

const updateForm = ref(null)
const updateProfile = function () {
  const payload = new FormData(updateForm.value)
  userStore.updateProfile(payload)
}

onMounted(() => {
  userTempStore.checkPermission()
})
</script>

<style scoped>
.update-form-inner {
  background-color: #ffffff00;
  color: white;
}

.update-form-inner::placeholder {
  color: white;
  /* text-align: center; */
}

.update-form-submit {
  background-color: #76abae;
  border: 1px #76abae solid;
  color: black;
}

.update-form-submit:hover {
  background-color: #ffffff00;
  color: white;
}
</style>
