<template>
  <div
    class="modal fade"
    id="login"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content modal-border-none">
        <div class="modal-body modal-border">
          <button type="button" class="btn close-btn" data-bs-dismiss="modal">
            <i class="fa-solid fa-xmark"></i>
          </button>
          <!-- modal 상단 -->
          <div class="modal-top">
            <i
              class="fa-solid fa-video p-3 m-2"
              style="color: #76abae; height: 30px"
            ></i>
            <h2 class="m-0 m-2" style="color: white">영화 추천 서비스</h2>
          </div>
          <!-- 로그인 폼 -->
          <h4 class="modal-login-text">로그인</h4>
          <div class="login-form-outer">
            <form ref="loginForm" @submit.prevent="userLogIn">
              <input
                class="form-control login-form-inner"
                type="text"
                placeholder="아이디를 입력하세요."
                name="username"
                v-model="usernameInput"
              />
              <input
                class="form-control login-form-inner"
                type="password"
                placeholder="비밀번호를 입력하세요."
                name="password"
                v-model="passwordInput"
              />
              <input
                class="form-control login-form-submit"
                type="submit"
                :value="logInBtn"
              />
            </form>
          </div>
          <!-- 회원 가입 RouterLink -->
          <hr />
          <div class="text-center">
            <RouterLink :to="{ name: 'SignUpView' }" class="nav-router"
              >회원 가입</RouterLink
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import { ref } from "vue";
import { RouterLink, useRouter } from "vue-router";
import { Modal } from "bootstrap";
import axios from "axios";

const router = useRouter();
const userStore = useUserStore();
const loginForm = ref(null);
const logInBtn = ref("로그인");
const usernameInput = ref("");
const passwordInput = ref("");

const userLogIn = function () {
  const payload = new FormData(loginForm.value);
  const logInModal = Modal.getInstance("#login");
  logInBtn.value = "로그인 중...";

  axios({
    method: "post",
    url: `${userStore.AUTH_BASE_URL}/login/`,
    data: payload,
  })
    .then((response) => {
      userStore.sessionData = response.data;
      logInBtn.value = "로그인 완료!";
      async function briefWait() {
        await new Promise((resolve) => setTimeout(resolve, 500));
        logInModal.hide();
        router.push({ name: "MainView" });
        router.go(0);
      }
      briefWait();
    })
    .catch((error) => {
      logInBtn.value = "로그인 실패";
      console.log(error);
    });
};
</script>

<style scoped>
* {
  color: white;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
}

.modal-border-none {
  border: none;
}

.modal-border {
  border: 0.5px white solid;
  border-radius: 10px;
}

.modal-top {
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-login-text {
  text-align: center;
  margin: 40px 20px 0 0;
}

.login-form-outer {
  margin: 15px 0;
}

.login-form-inner {
  margin: 10px 0;
  background-color: #222831;
  color: white;
}

input::placeholder {
  color: white;
}

.login-form-submit {
  border: none;
  margin: 10px 0;
  background-color: #76abae;
  color: white;
}
</style>
