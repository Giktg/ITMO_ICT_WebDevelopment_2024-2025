<script setup>
import { ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();
const error = ref(false);
const form = ref({
  guest_name: "",
  day: "",
});
const count = ref();
function find() {
  console.log(form.value);
  instance
    .post("/main/resident/get_cleaner/", form.value, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        count.value = response.data.cleaner_name;
        console.log(count.value);
        error.value = false;
      }
    })
    .catch((e) => (error.value = true));
}
</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Найти уборщика</h2>
      <v-text-field
        label="Номер паспорта постояльца"
        v-model="form.guest_name"
      ></v-text-field>
      <v-select
        label="День недели"
        v-model="form.day"
        :items="['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']"
      ></v-select>
      <v-btn @click="find">Найти</v-btn>
      <h2 v-if="error" class="text-red">Не найдено</h2>
      <div v-else-if="count">
        <h2>Номер убирал {{ count }}</h2>
      </div>
    </div>
  </v-app>
</template>

<style scoped>
h2 {
  margin-top: 10%;
  margin-bottom: 5%;
}
</style>
