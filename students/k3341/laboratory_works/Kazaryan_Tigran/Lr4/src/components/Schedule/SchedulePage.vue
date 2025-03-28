<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();

const form = ref({
  day: "",
  cleaner_id: "",
  floor: "",
});

function getPaper() {
  instance
    .get(`/main/schedule/${router.currentRoute.value.params.id}/`, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        form.value = response.data;
      }
    })
    .catch((error) => console.log(error));
}

function savePaper() {
  const { id, ...rest } = form.value;
  instance
    .patch(`/main/schedule/${router.currentRoute.value.params.id}/`, rest, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        router.push("/schedules");
      }
    })
    .catch((error) => console.log(error));
}

onMounted(() => {
  getPaper();
});
</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Расписание</h2>
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
      <v-btn @click="savePaper">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped>
h2 {
  margin-top: 10%;
  margin-bottom: 5%;
}
</style>
