<template>
  <div v-if="main_page">

    <div class="row">
      <q-select v-model="factor_id" @update:model-value="search_by_factors(factor_id.token)" standout bg-color="teal-5" rounded class="select" label="نام ماه"
      :options="select_month.list_month"  option-value="token" option-label="name"
      ></q-select>
      <q-table
        style="margin-right: 5% ; margin-left: 5% ; margin-top: 2rem"
        class="table"
        dense
        title="وضعیت پرداختی ها"
        :rows="rows"
        :columns="columns"
        row-key="name"
      >
        <template v-slot:header="props">
          <q-tr :props="props">
            <q-th auto-width />
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
              <q-btn size="sm" color="accent" round dense @click="props.expand = !props.expand" :icon="props.expand ? 'remove' : 'add'" />
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
            <q-td colspan="100%">
              <q-btn label="وضعیت به پرداخت شده ها " class="bg-cyan-1" @click="change_state(props.row.token , factor_id.token) "> </q-btn>
              <q-btn label="وضعیت به پرداخت شده ها " class="bg-amber-1" @click="show_factor(props.row.token , factor_id.token) "> </q-btn>
            </q-td>
          </q-tr>
        </template>

      </q-table>
    </div>
  </div>
  <div v-else>
    <q-select v-model="apartement_id" option-label="name" option-value="id" :options="searching_data.list_building"
              class="select bg-grey-1" rounded label="انتخاب ساختمان" @update:model-value="select_building"></q-select>
  </div>

</template>

<script>
import {reactive, ref} from 'vue';
import URLS from "src/URL/url";
import axios from "axios";

export default {
  name: "incoming_page",
  data() {

    let apartement_id = ref('')
    let main_page = ref(false)
    const searching_data = reactive({
      list_building: [],
    })
    const select_month = reactive({
      list_month: [],
    })
    let factor_id = ref('')
    const  columns = [
      {name: 'name', align: 'center', label: 'شماره واحد', field: 'name', sortable: true},
      {name: 'mobile', align: 'center', label: 'شماره همراه', field: 'mobile', sortable: true},
      {name: 'price', align: 'center', label: 'مبلغ فاکتور ', field: 'price', sortable: true},
      {name: 'states', align: 'center', label: 'وضعیت ', field: 'states', sortable: true},
    ]
    const rows =reactive([])

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
      factor_id,
      apartement_id,
      main_page,
      searching_data,
      select_month
    }
  },



  methods:{
    select_building(){

      const  address = new URLS()
      axios.post(address.factor_list() , {
        'id' : this.apartement_id.id
      }).then(value => {
        if(value.data.done ===true){
          for (let i = 0; i < value.data.data.length; i++) {
            this.select_month.list_month.push(value.data.data[i])
          }
          this.main_page = true
        }
      })
    },

    search_by_factors(token){
      this.rows =[]
      const  address = new URLS()
      axios.post(address.factor_apartenet_month() , {
        'id':token
      }).then(value => {
        if (value.data.done === true){
          console.log(value.data.data)
          console.log(token)
          for (let i = 0; i <value.data.data.length ; i++) {
            let state = 'پرداخت نشده'
            if (value.data.data[i].is_paid){
              state ='پرداخت شده'
            }
            this.rows.push({
              name: value.data.data[i].number,
              mobile: value.data.data[i].mobile,
              price: value.data.data[i].price,
              states: state ,
              token :value.data.data[i].token
            })

          }
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

.select {
  width: 50%;
  margin-right: 25%;
  margin-top: 5rem;
  font-family: myyekan;
}

.table {
  width: 80%;
  margin-top: 2rem;
  margin-right: 10%;
  margin-left: 10%;
  font-family: myvazir;
}

.text {
  font-family: myvazir;
  margin-top: 1rem;
  width: 80%;
  margin-right: 10%;
  margin-bottom: 1rem;
}

.deletet_btn {
  width: 25%;
  font-family: myvazir;
  margin-top: 1rem;
  margin-right: 10%;
  margin-bottom: 1rem;
}

h5 {
  text-align: center;
  font-family: myyekan;
  margin-top: 1rem;
  padding-top: 2rem;
}

.buttons {
  margin-top: 1rem;
  margin-bottom: 1rem;
  width: 80%;
  margin-right: 10%;
}

.text2 {
  text-align: center;
  display: block;
  width: 70%;
  margin-right: 15%;
  margin-left: 15%;
  margin-top: 1rem;
}
</style>
