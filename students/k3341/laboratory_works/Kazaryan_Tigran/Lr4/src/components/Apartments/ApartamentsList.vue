<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();
const apartments = ref([]);
const free = ref([]);

function getRooms() {
  instance
    .get("/main/apartments/", {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        apartments.value = response.data;
      }
    })
    .catch((error) => console.log(error));
}

function getFree() {
  instance
    .get("/main/apartments/count_free/", {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        free.value = response.data;
        console.log(free.value);
      }
    })
    .catch((error) => console.log(error));
}

function start() {
  getRooms();
  getFree();
}
onMounted(() => {
  start();
});
</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Номера</h2>
    <v-card width="500" :title="`${free.Free} свободных`"></v-card>
    <template v-for="apart in apartments" :key="apart.id">
      <v-card
        width="400"
        :title="apart.apartment_number"
        :subtitle="`Статус: ${apart.status}`"
        :text="`rooms: ${apart.rooms}\nprice: ${apart.price}\nphone: ${apart.phone}\nfloor: ${apart.floor}`"
        style="white-space: pre-line; text-align: center"
        ><v-card-actions style="margin-left: 35%">
          <v-btn @click="router.push('/apartments/' + apart.apartment_number)">
            Изменить
          </v-btn>
        </v-card-actions></v-card
      >
    </template>
  </div>
</template>
h2 { margin-top: 10%; margin-bottom: 5%; }
<style scoped></style>
