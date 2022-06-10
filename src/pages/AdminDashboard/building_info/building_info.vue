<template>
  <div class="row">
    <div class="col-5 " style="margin-right: 2rem">
      <q-card class="my-card">
        <q-card-section>
          <h5>اطلاعات اولیه ساختمان</h5>
          <q-input v-model="building_info.name" dense standout rounded class="text" label="نام ساختمان"></q-input>
          <q-input v-model="building_info.number" dense standout rounded class="text" type="number"
                   label="تعداد واحد"></q-input>
          <q-input v-model="building_info.initial" dense standout rounded type="number" class="text"
                   label="موجودی اولیه صندوق"></q-input>
          <q-input v-model="building_info.manager_name" dense standout rounded class="text" label="نام مدیر"></q-input>
          <q-input v-model="building_info.manager_family" dense standout rounded class="text"
                   label="نام خانوادگی مدیر"></q-input>
          <q-separator style="margin-top: 1rem ; color: black"></q-separator>
          <q-btn @click="save_building" color="pink-6" rounded class="q-btn full-width" label="ثبت"></q-btn>
        </q-card-section>
      </q-card>
    </div>
    <div class="col-1"></div>
    <div class="col-5">
      <q-card class="my-card">
        <q-card-section>
          <h5>اطلاعات اولیه واحد ها</h5>
          <q-select v-model="searching_data.buildiing_selection" :options="searching_data.list_building" option-value="id"
                    class="text" option-label="name" rounded standout></q-select>
          <q-input dense standout rounded class="text" label="شماره واحد"></q-input>
          <q-input dense standout rounded class="text" type="number" label="تعداد نفرات"></q-input>
          <q-input dense standout rounded class="text" type="number" label="متراژ"></q-input>
          <q-input dense standout rounded class="text" type="number" label="نوع ملک"></q-input>
          <q-input dense standout rounded class="text" label="شماره موبایل"></q-input>
          <q-separator style="margin-top: 1rem ; color: black"></q-separator>
          <q-btn @click="Test" color="deep-purple-9" rounded class="q-btn full-width" label="ایجاد"></q-btn>
        </q-card-section>
      </q-card>
    </div>
    <div class="col-1"></div>
  </div>

  <div class="row">
    <q-table
      style="margin-right: 5% ; margin-left: 5% ; margin-top: 2rem"
      class="full-width"
      dense
      title="Treats"
      :rows="rows"
      :columns="columns"
      row-key="name"
    />
  </div>

</template>

<script>
import axios from "axios";
import URLS from "src/URL/url";
import {reactive} from "vue";
import {useStore} from 'vuex'
import {useQuasar} from 'quasar'

export default {
  name: "DashBoard",

  data() {

    const store = useStore()
    const $q = useQuasar()
    const building_info = reactive({
      name: '',
      number: 0,
      initial: 0,
      manager_name: '',
      manager_family: ''

    })
    const searching_data = reactive({
      list_building: [],
      buildiing_selection: ''
    })

    function searching() {
      const address = new URLS()
      axios.get(address.building_list()).then(value => {
        if (value.data.done === true) {
          searching_data.list_building = value.data.data
          console.log(searching_data.list_building)
        }
      })
    }
    searching()


    return {
      searching,
      searching_data,
      store,
      building_info,
      toast(text, color, textColor,) {
        $q.notify({
          type: "total",
          message: text,
          color: color,
          textColor: textColor,
          classes: 'text',
        });
      },
    }
  },

  methods: {
    Test() {
      this.toast('عملیات با موفقیت انجام شد', 'light-green-10', 'white')
    },

    save_building() {
      const address = new URLS()
      const token = this.store.getters['StoreBase/get_token']
      axios.post(address.create_building(), {
        building_name: this.building_info.name,
        number_of_apartement: this.building_info.number,
        initial: this.building_info.initial,
        name_of_manager: this.building_info.manager_name,
        family_of_manager: this.building_info.manager_family
      }).then(value => {
        if (value.data.data.done === true) {
          this.toast('عملیات با موفقیت انجام شد', 'light-green-10', 'white')
          this.building_info.number = 0
          this.building_info.name = ''
          this.building_info.manager_name = ''
          this.building_info.manager_family = ''
          this.building_info.initial = 0
          this.searching()
        } else {
          this.toast('خطا در انجام عملیات', 'lred-9', 'white')
        }

      })
    }
  }


}
</script>

<style scoped>
.my-card {
  margin: 3rem 1rem 3rem 1rem;
}

h5 {
  font-family: myvazir;
  text-align: center;
}

.text {
  font-family: myvazir;
  margin-top: .5rem;
  width: 80%;
  margin-left: 10%;
  margin-right: 10%;
}

.q-btn {
  font-family: myyekan;
  margin-top: 1rem;
  margin-bottom: 1rem;
}
</style>
