<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();
const lessons = ref([]);

function getLessons() {
  instance
    .get("/main/cleaner/", {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        lessons.value = response.data;
      }
    })
    .catch((error) => console.log(error));
}

function deleteLesson(id) {
  instance
    .delete(`/main/cleaner/${id}/`, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 204) {
        getLessons();
      }
    })
    .catch((error) => console.log(error));
}

onMounted(() => {
  getLessons();
});
</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Уборщики</h2>

    <template v-for="cleaner in lessons" :key="cleaner.cleaner_name">
      <v-card
        width="400"
        :title="cleaner.cleaner_name"
        style="white-space: pre-line; text-align: center"
        ><v-card-actions style="margin-left: 37%">
          <v-btn @click="deleteLesson(cleaner.cleaner_name)"> Удалить </v-btn>
        </v-card-actions></v-card
      >
    </template>
    <v-btn @click="router.push('/add-lesson')">Добавить</v-btn>
  </div>
</template>

<style scoped>
h2 {
  margin-top: 10%;
  margin-bottom: 5%;
}
</style>
