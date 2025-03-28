<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";
const cleanersArr = ref([]);
const Token = TokenStore();
const cleaners = ref([]);
const form = ref({
  day: "",
  cleaner_id: "",
  floor: "",
});

function create() {
  instance
    .post("/main/schedule/", form.value, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 201) {
        router.push("/schedules");
      }
    })
    .catch((error) => console.log(error));
}
function getCleaners() {
  instance
    .get("/main/cleaner/", {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        cleaners.value = response.data;
        cleaners.value.forEach((element) =>
          cleanersArr.value.push(element.cleaner_name)
        );
      }
    })
    .catch((error) => console.log(error));
}
onMounted(() => {
  getCleaners();
});
</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Добавить расписание</h2>
      <v-select
        label="День недели"
        v-model="form.day"
        :items="['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']"
      ></v-select>
      <v-select label="Этаж" v-model="form.floor" :items="[1, 2, 3]"></v-select>
      <v-select
        label="Уборщик"
        v-model="form.cleaner_id"
        :items="cleanersArr"
      ></v-select>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>
h2 {
  margin-top: 10%;
  margin-bottom: 5%;
}
</style>
