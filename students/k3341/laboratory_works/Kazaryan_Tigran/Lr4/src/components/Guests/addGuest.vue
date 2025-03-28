<script setup>
import { ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();

const form = ref({
  passport_number: "",
  guest_name: "",
  city: "",
});

function create() {
  instance
    .post("/main/guest/", form.value, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 201) {
        router.push("/guests");
      }
    })
    .catch((error) => console.log(error));
}
</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Гость</h2>
      <v-text-field label="Имя" v-model="form.guest_name"></v-text-field>
      <v-text-field
        label="Номер паспорта"
        v-model="form.passport_number"
      ></v-text-field>
      <v-text-field label="Город" v-model="form.city"></v-text-field>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped></style>
