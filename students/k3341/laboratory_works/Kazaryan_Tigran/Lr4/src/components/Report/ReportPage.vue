<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();
const report = ref([]);
const quarter = ref();
function getReport(quarter) {
  instance
    .get("/main/report/" + quarter + "/", {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        report.value = response.data;
      }
    })
    .catch((error) => console.log(error));
}
</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Отчет</h2>
    <v-select
      label="Квартал"
      v-model="quarter"
      :items="[1, 2, 3, 4]"
      style="width: 500px"
    ></v-select>
    <v-btn @click="getReport(quarter)">Создать отчет</v-btn>
    <template v-for="apart in report" :key="apart.id">
      <v-card
        width="400"
        :title="`Апартаменты ${apart.apartment_number}`"
        :text="`Клиентов: ${apart.total_clients}\n\nВыручка: ${apart.total_income}₽`"
        style="white-space: pre-line; text-align: center"
      ></v-card>
    </template>
  </div>
</template>

<style scoped>
h2 {
  margin-top: 10%;
  margin-bottom: 5%;
}
</style>
