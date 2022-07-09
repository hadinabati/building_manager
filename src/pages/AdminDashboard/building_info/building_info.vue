<template>
  <div class="row">
    <div class="col-md-5 col-xs-12" style="">
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
    <div class="col-md-5 col-xs-12">
      <q-card class="my-card">
        <q-card-section>
          <h5>اطلاعات اولیه واحد ها</h5>
          <q-select v-model="searching_data.buildiing_selection" :options="searching_data.list_building"
                    option-value="id"
                    class="text" option-label="name" rounded standout @update:model-value="apaetement_list"></q-select>
          <q-input v-model="apartements_info.number" dense standout rounded class="text" type="number"
                   label="شماره واحد"></q-input>
          <q-input v-model="apartements_info.person" dense standout rounded class="text" type="number"
                   label="تعداد نفرات"></q-input>
          <q-input v-model="apartements_info.M2" dense standout rounded class="text" type="number"
                   label="متراژ"></q-input>
          <q-select v-model="apartements_info.type_selected" :options="apartements_info.types"
                    class="text" rounded standout></q-select>
          <q-input dense v-model="apartements_info.mobile" standout rounded class="text" label="شماره موبایل"></q-input>
          <q-separator style="margin-top: 1rem ; color: black"></q-separator>
          <q-btn @click="create_apartements" color="deep-purple-9" rounded class="q-btn full-width"
                 label="ایجاد"></q-btn>
        </q-card-section>
      </q-card>
    </div>
    <div class="col-1"></div>
  </div>

  <div class="row">
    <q-table
      style="margin-right: 5% ; margin-left: 5% ; margin-top: 2rem"
      class="tables"
      dense
      title=""
      :rows="rows"
      :columns="columns"
      row-key="name"
    >
      <template v-slot:header="props">
        <q-tr :props="props">
          <q-th auto-width/>
          <q-th
            v-for="col in props.cols"
            :key="col.name"
            :props="props"
          >
            {{ col.label }}
          </q-th>
        </q-tr>
      </template>
      <template v-slot:body="props">
        <q-tr :props="props">
          <q-td auto-width>
            <q-btn size="sm" color="accent" round dense @click="props.expand = !props.expand"
                   :icon="props.expand ? 'remove' : 'add'"/>
          </q-td>
          <q-td
            v-for="col in props.cols"
            :key="col.name"
            :props="props"
          >
            {{ col.value }}
          </q-td>
        </q-tr>
        <q-tr v-show="props.expand" :props="props">
          <q-td colspan="50%">
            <q-btn label="ویرایش" disable></q-btn>
          </q-td>
        </q-tr>
      </template>
    </q-table>
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
    const apartements_info = reactive({
      number: 0,
      person: 0,
      M2: 0,
      types: ['مالک', 'مستاجر'],
      mobile: '',
      type_selected: ''
    })
    const searching_data = reactive({
      list_building: [],
      buildiing_selection: ''
    })

    const columns = [
      {
        name: 'name',
        required: true,
        label: 'شماره واحد',
        align: 'center',
        field: row => row.name,
        format: val => `${val}`,
        sortable: true
      },
      {name: 'person', align: 'center', label: 'تعداد نفرات', field: 'person', sortable: true},
      {name: 'M2', align: 'center', label: 'متراژ', field: 'M2', sortable: true},
      {name: 'types', align: 'center', label: 'نوع ملک', field: 'types', sortable: true},
      {name: 'mobile', align: 'center', label: 'شماره موبایل', field: 'mobile', sortable: true}]
    const rows = reactive([])

    function searching() {
      const address = new URLS()
      axios.get(address.building_list()).then(value => {
        if (value.data.done === true) {
          searching_data.list_building = value.data.data
        }
      })
    }

    searching()

    return {
      rows,
      columns,
      apartements_info,
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
    apaetement_list() {
      const adress = new URLS()
      axios.get(adress.apartements_list() + "/" + this.searching_data.buildiing_selection.id).then(value => {
        if (value.data.done === true) {
          this.rows.splice(0, this.rows.length)
          for (let i = 0; i < value.data.data.length; i++) {
            this.rows.push(
              {
                name: value.data.data[i].number,
                person: value.data.data[i].person,
                M2: value.data.data[i].M2,
                types: value.data.data[i].type,
                mobile: value.data.data[i].mobile,
              },
            )
          }
          console.log(value.data.data)
        } else {
          this.toast('خطا در بروز رسانی', 'red', 'white')
        }
      })


    },
    create_apartements() {
      const address = new URLS()
      axios.post(address.create_apartements(), {
        "building_id": this.searching_data.buildiing_selection.id,
        "number": this.apartements_info.number,
        "number_person": this.apartements_info.person,
        "m2": this.apartements_info.M2,
        "type": this.apartements_info.type_selected,
        "mobile": this.apartements_info.mobile
      }).then(value => {
        if (value.data.done === true) {
          this.apartements_info.number = 0
          this.apartements_info.M2 = 0
          this.apartements_info.person = 0
          this.apartements_info.mobile = ''
          this.apaetement_list()
          this.toast('عملیات با موفقیت انجام شد', 'green', 'white')
        } else {
          this.toast('خطا در انجام عملیات', 'red', 'white')
        }
      })

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
    },


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
.tables{
  width: 90%;
  margin-left: 10%;
  margin-right: 10%;
}
</style>
