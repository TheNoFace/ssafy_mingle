<template>
  <div class="modal fade" id="login" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content modal-border-none">
        <div class="modal-body modal-border">
          <button type="button" class="btn close-btn" data-bs-dismiss="modal">
            <i class="fa-solid fa-xmark"></i>
          </button>
          <!-- modal 상단 -->
          <div class="modal-top">
            <i class="fa-solid fa-video p-3 m-2" style="color: #76ABAE; height: 30px;"></i>
            <h2 class="m-0 m-2" style="color: white;">영화 추천 서비스</h2>
          </div>
          <!-- 로그인 폼 -->
          <h4 class="modal-login-text">로그인</h4>
          <div class="login-form-outer">
            <form>
              <input class="form-control login-form-inner" type="text" placeholder="아이디를 입력하세요.">
              <input class="form-control login-form-inner" type="password" placeholder="비밀번호를 입력하세요.">
              <input class="form-control login-form-submit" type="submit" value="로그인">
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
* {
  color: white
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
  color: white  ;
}

input::placeholder {
  color: white;
}

.login-form-submit {
  border: none;
  margin: 10px 0;
  background-color: #76ABAE;
  color: white  ;
}

</style>