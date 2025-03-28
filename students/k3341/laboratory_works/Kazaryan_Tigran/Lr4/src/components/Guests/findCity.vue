<script setup>
import { ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();
const error = ref(false);
const form = ref({
  city: "",
});
const count = ref();
function find() {
  console.log(11);
  instance
    .post("/main/guest/find/", form.value, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        count.value = response.data.count;
        // if (count.value[form.city])
        console.log(count.value);
        // console.log(response.data.count);
        error.value = false;
        // router.push("/guests");
      }
    })
    .catch((e) => (error.value = true));
}
</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Поиск по городу</h2>
      <v-text-field label="Имя" v-model="form.city"></v-text-field>
      <v-btn @click="find">Найти</v-btn>
      <h2 v-if="error" class="text-red">Не найдено</h2>
      <div v-else-if="count">
        <h2>Найдено: {{ count }}</h2>
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
