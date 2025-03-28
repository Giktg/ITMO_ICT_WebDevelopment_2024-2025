<script setup>
import { ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();

const form = ref({
  cleaner_name: "",
});

function create() {
  instance
    .post("/main/cleaner/", form.value, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 201) {
        router.push("/cleaners");
      }
    })
    .catch((error) => console.log(error));
}
</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Добавить уборщика</h2>
      <v-text-field label="Имя" v-model="form.cleaner_name"></v-text-field>
      <v-btn @click="create">Добавить</v-btn>
    </div>
  </v-app>
</template>

<style scoped></style>
