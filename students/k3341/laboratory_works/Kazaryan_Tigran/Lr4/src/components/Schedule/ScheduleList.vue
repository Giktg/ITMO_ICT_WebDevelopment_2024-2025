<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();
const schedules = ref([]);

function getSchedules() {
  instance
    .get("/main/schedule/", {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        schedules.value = response.data;
      }
    })
    .catch((error) => console.log(error));
}

function deleteSchedule(id) {
  instance
    .delete(`/main/schedules/${id}/`, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 204) {
        getSchedules();
      }
    })
    .catch((error) => console.log(error));
}

onMounted(() => {
  getSchedules();
});
</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Расписание</h2>

    <template v-for="schedule in schedules" :key="schedule.id">
      <v-card
        width="400"
        :title="`${schedule.day}, ${schedule.floor} этаж`"
        :subtitle="`${schedule.cleaner_id}`"
        style="white-space: pre-line; text-align: center"
        ><v-card-actions style="margin-left: 23%">
          <v-btn @click="router.push('/schedules/' + schedule.id)">
            Изменить
          </v-btn>
          <v-btn @click="deleteSchedule(schedule.id)"> Удалить </v-btn>
        </v-card-actions></v-card
      >
    </template>
    <v-btn @click="router.push('/add-schedule')">Добавить</v-btn>
  </div>
</template>

<style scoped>
h2 {
  margin-top: 10%;
  margin-bottom: 5%;
}
</style>
