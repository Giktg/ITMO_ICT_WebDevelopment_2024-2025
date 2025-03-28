<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();
const residents = ref([]);

function getResidents() {
  instance
    .get("/main/resident/", {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        residents.value = response.data;
      }
    })
    .catch((error) => console.log(error));
}

function deleteResident(id) {
  instance
    .delete(`/main/resident/${id}/`, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 204) {
        getResidents();
      }
    })
    .catch((error) => console.log(error));
}

onMounted(() => {
  getResidents();
});
</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Постояльцы</h2>
    <v-btn @click="router.push('/residents/find-cleaner')">
      Найти уборщика
    </v-btn>
    <template v-for="resident in residents" :key="resident.id">
      <v-card
        width="400"
        :title="`${resident.passport_number} живет в номере ${resident.apartment_number}`"
        :subtitle="`С ${resident.check_in} по ${resident.check_out}`"
        style="white-space: pre-line; text-align: center"
        ><v-card-actions style="margin-left: 10%">
          <v-btn @click="router.push('/residents/' + resident.id)">
            Изменить
          </v-btn>
          <v-btn @click="deleteResident(resident.id)"> Удалить </v-btn>
          <v-btn
            @click="
              router.push('/residents/' + resident.id + '/other_residents')
            "
          >
            Другие
          </v-btn>
        </v-card-actions></v-card
      >
    </template>
    <v-btn @click="router.push('/add-residents')">Добавить</v-btn>
  </div>
</template>

<style scoped>
h2 {
  margin-top: 10%;
  margin-bottom: 5%;
}
</style>
