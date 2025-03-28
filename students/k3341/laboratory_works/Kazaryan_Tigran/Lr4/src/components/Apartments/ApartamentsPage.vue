<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();

const form = ref({
  apartment_number: "",
  rooms: "",
  price: "",
  status: "",
  phone: "",
  floor: "",
});

function getPaper() {
  instance
    .get(`/main/apartments/${router.currentRoute.value.params.id}/`, {
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
  const { apartment_number, rooms, price, status, phone, floor } = form.value;
  console.log(router.currentRoute.value.params.id);
  instance
    .patch(
      `/main/apartments/${router.currentRoute.value.params.id}/`,
      {
        apartment_number: apartment_number,
        rooms: rooms,
        price: price,
        status: status,
        phone: phone,
        floor: floor,
      },
      {
        headers: {
          Authorization: `Bearer ${Token.token}`,
        },
      }
    )
    .then((response) => {
      if (response.status === 200) {
        router.push("/apartments");
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
      <h2>Номер</h2>
      <h3>{{ form.apartment_number }} номер</h3>
      <h3>{{ form.rooms }} комнаты</h3>
      <v-text-field label="Цена" v-model="form.price"></v-text-field>
      <v-text-field label="статус" v-model="form.status"></v-text-field>
      <h3>{{ form.floor }} этаж</h3>
      <v-btn @click="savePaper">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped>
h3 {
  margin: 20px;
  margin-left: 0;
}
</style>
