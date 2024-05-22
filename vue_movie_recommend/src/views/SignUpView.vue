<template>
  <div>
    <h1 style="color: white">회원 가입</h1>
    <div>
      <form ref="signUpForm" @submit.prevent="userSignUp">
        <input
          class="form-control login-form-inner"
          type="text"
          placeholder="아이디를 입력하세요."
          name="username"
          required
        />
        <input
          class="form-control login-form-inner"
          type="text"
          placeholder="닉네임을 입력하세요."
          name="nickname"
          required
        />
        <input
          class="form-control login-form-inner"
          type="password"
          placeholder="비밀번호를 입력하세요."
          name="password"
          required
        />
        <input
          class="form-control login-form-submit"
          type="submit"
          value="로그인"
        />
      </form>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import { ref } from "vue";

const userStore = useUserStore();
const signUpForm = ref(null);

const userSignUp = function () {
  const payload = new FormData(signUpForm.value);
  userStore.userSignUp(payload);
};
</script>

<style scoped></style>
