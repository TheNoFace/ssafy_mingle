<template>
  <div>
    <h1 style="color: white; text-align: center;">회원 가입</h1>
    <div>
      <form ref="signUpForm" @submit.prevent="userSignUp" class="m-auto" style="width: 50%;">
        <input class="form-control signup-form-inner my-3" type="text" placeholder="아이디를 입력하세요." name="username"
          required />
        <input class="form-control signup-form-inner my-3" type="text" placeholder="닉네임을 입력하세요." name="nickname"
          required />
        <input class="form-control signup-form-inner my-3" type="password" placeholder="비밀번호를 입력하세요." name="password"
          required />
        <input class="form-control signup-form-submit" type="submit" value="회원가입" />
      </form>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user"
import { ref } from "vue"

const userStore = useUserStore()
const signUpForm = ref(null)

const userSignUp = function () {
  const payload = new FormData(signUpForm.value)
  console.log(payload)
  userStore.userSignUp(payload)
}
</script>

<style scoped>
.signup-form-inner {
  background-color: #ffffff00;
  color: white;
}

.signup-form-inner::placeholder {
  color: white;
  /* text-align: center; */
}

.signup-form-submit {
  background-color: #76abae;
  border: 1px #76abae solid;
  color: black;
}

.signup-form-submit:hover {
  background-color: #ffffff00;
  color: white;
}
</style>
