<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();
const guests = ref([]);

function getGuests() {
  instance
    .get("/main/guest/", {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        guests.value = response.data;
      }
    })
    .catch((error) => console.log(error));
}

function deleteGuest(id) {
  instance
    .delete(`/main/guest/${id}/`, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 204) {
        getGuests();
      }
    })
    .catch((error) => console.log(error));
}

onMounted(() => {
  getGuests();
});
</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Гости</h2>
    <v-btn @click="router.push('/guests/find')">Поиск по городу</v-btn>
    <template v-for="guest in guests" :key="guest.passport_number">
      <v-card
        width="400"
        :title="guest.guest_name"
        :text="`passport_number: ${guest.passport_number}\ncity: ${guest.city}`"
        style="white-space: pre-line; text-align: center"
        ><v-card-actions style="margin-left: 25%">
          <v-btn @click="router.push('/guests/' + guest.passport_number)">
            Изменить
          </v-btn>
          <v-btn @click="deleteGuest(guest.passport_number)"> Удалить </v-btn>
        </v-card-actions></v-card
      >
    </template>
    <v-btn @click="router.push('/add-guest')">Добавить</v-btn>
  </div>
</template>

<style scoped></style>
