<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();

const form = ref({
  check_in: "",
  check_out: "",
  passport_number: "",
  apartment_number: "",
});
const guests = ref([]);
const guestsArr = ref([]);
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
        guests.value.forEach((element) =>
          guestsArr.value.push(element.passport_number)
        );
      }
    })
    .catch((error) => console.log(error));
}
const aps = ref([]);
const apsArr = ref([]);
function getAps() {
  instance
    .get("/main/apartments/", {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        aps.value = response.data;
        aps.value.forEach((element) =>
          apsArr.value.push(element.apartment_number)
        );
      }
    })
    .catch((error) => console.log(error));
}

onMounted(() => {
  getGuests();
  getAps();
});
function create() {
  console.log(form.value);
  instance
    .post("/main/resident/", form.value, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 201) {
        router.push("/teachers-lessons");
      }
    })
    .catch((error) => console.log(error));
}
</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Добавить постояльца</h2>
      <v-select
        label="Номер паспорта гостя"
        v-model="form.passport_number"
        :items="guestsArr"
      ></v-select>
      <v-select
        label="Номер апартаментов"
        v-model="form.apartment_number"
        :items="apsArr"
      ></v-select>
      <v-text-field label="Дата заезда" v-model="form.check_in"></v-text-field>
      <v-text-field label="Дата выезда" v-model="form.check_out"></v-text-field>
      <v-btn @click="create">Добавить</v-btn>
    </div>
  </v-app>
</template>

<style scoped>
h2 {
  margin-top: 10%;
  margin-bottom: 5%;
}
</style>
