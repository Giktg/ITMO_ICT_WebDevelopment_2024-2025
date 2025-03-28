<script setup>
import { ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();

const form = ref({
  username: "",
  password: "",
});

function login() {
  instance
    .post("/main/login/", form.value)
    .then((response) => {
      if (response.status === 200) {
        Token.setToken(response.data.access);
        router.push("/apartments");
      }
    })
    .catch((error) => console.log(error));
}
</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Вход</h2>
      <v-text-field label="Логин" v-model="form.username"></v-text-field>
      <v-text-field label="Пароль" v-model="form.password"></v-text-field>
      <v-btn @click="login">Войти</v-btn>
    </div>
  </v-app>
</template>

<style scoped>
h2 {
  margin-top: 10%;
  margin-bottom: 5%;
}
</style>
