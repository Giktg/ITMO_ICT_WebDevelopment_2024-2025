<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();

const form = ref({
  passport_number: "",
  guest_name: "",
  city: "",
});

function getPaper() {
  instance
    .get(`/main/guest/${router.currentRoute.value.params.id}/`, {
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
  const { passport_number, guest_name, city } = form.value;
  instance
    .patch(
      `/main/guest/${router.currentRoute.value.params.id}/`,
      {
        passport_number: passport_number,
        guest_name: guest_name,
        city: city,
      },
      {
        headers: {
          Authorization: `Bearer ${Token.token}`,
        },
      }
    )
    .then((response) => {
      if (response.status === 200) {
        router.push("/guests");
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
      <h2>Гость</h2>
      <v-text-field label="Имя" v-model="form.guest_name"></v-text-field>
      <v-text-field
        label="Номер паспорта"
        v-model="form.passport_number"
      ></v-text-field>
      <v-text-field label="Город" v-model="form.city"></v-text-field>
      <v-btn @click="savePaper">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped></style>
