<template>


  <div v-if="main_page">
    <div class="row">
      <div class="col-md-5 col-xs-12">
        <q-card class="my-card bg-cyan-1">
          <h5>ایجاد هزینه</h5>
          <q-input dense v-model="selected_out_come.name" standout rounded class="text" label="نام هزینه"></q-input>
          <q-select v-model="selected_out_come.type" class="text2" :options="type" option-value="id"
                    option-label="value"
                    label="پرداخت کننده هزینه"/>
          <q-select v-model="selected_out_come.kind" class="text2" :options="kind" option-label="value"
                    option-value="id"
                    label="براساس"/>
          <q-btn @click="create_cash" rounded color="indigo-13" class="buttons" dense label="ایجاد هزینه"></q-btn>
        </q-card>
      </div>
      <div class="col-1"></div>
      <div class="col-md-5 col-xs-12">
        <q-card class="my-card ">
          <div class="bg-red-1">
            <h5>ایجاد صورتحساب</h5>
            <q-input dense standout rounded class="text " :disable="!checking" v-model="create_data.month"
                     label="نام ماه"></q-input>
            <div>
              <q-btn @click="create_month" color="teal-5" :disable="!checking" rounded class="buttons"
                     label="ثبت اولیه  ماه "></q-btn>
            </div>
          </div>
          <hr>


          <q-select :disable="checking" dense standout rounded class="text" v-model="create_data.data.cost"
                    :options="money_list" option-value="id" option-label="name" label="انتخاب هزینه "/>
          <div>
            <q-input :disable="checking" dense standout rounded class="text" label="تاریخ"
                     v-model="create_data.data.date"></q-input>
            <q-popup-edit>
              <template v-slot="scope">
                <q-date minimal
                        v-model="create_data.data.date"
                        color="purple-8"
                        :locale="{daysShort  :['1','2','3','4 ','5','جمعه','شنبه'],
                months:['فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند']}"
                        calendar="persian">
                  <q-btn label="انتخاب" v-close-popup></q-btn>
                </q-date>
              </template>
            </q-popup-edit>
          </div>
          <q-input :disable="checking" dense standout rounded class="text" type="number" label="مبلغ هزینه "
                   v-model="create_data.data.price"></q-input>
          <q-input :disable="checking" dense standout rounded class="text" label="شرح هزینه "
                   v-model="create_data.data.discripe"></q-input>
          <div>
            <q-btn :disable="checking" color="pink-5" rounded class="buttons" @click="insert_data_table"
                   label="ثبت اولیه "></q-btn>
          </div>


        </q-card>
      </div>
    </div>
    <hr style="margin: 2rem">
    <div class="row">
      <q-btn  color="blue-grey-8" rounded @click="insert_to_db" class="content-end"
             style="display: block ; width: 25% ; margin-right: 70% ; margin-left: 5%" label="ثبت نهایی فاکتور ایجاد شده"></q-btn>
    </div>
    <div class="row">
      <q-input readonly standout
               style="display: block ; margin-top: 1rem ; width: 25% ; margin-right: 70% ; margin-left: 5%"
               :label="sum +  '      ' + 'تومان '"
      >

      </q-input>
    </div>
    <div class="row">
      <q-table
        class="table"
        title=""
        :rows="rows"
        :columns="columns"
        row-key=""
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
              <q-btn text-color="white" label="حذف" class="bg-pink-13 deletet_btn" @click="deleteـitem(props)"></q-btn>
            </q-td>
          </q-tr>
        </template>
      </q-table>

    </div>
  </div>
  <div v-else>
    <q-select v-model="apartement_id" option-label="name" option-value="id" :options="searching_data.list_building"
              class="select bg-grey-1" rounded label="انتخاب ساختمان" @update:model-value="select_building" ></q-select>
  </div>

</template>


<script>
import {reactive, ref} from 'vue'
import URLS from "src/URL/url";
import axios from "axios";
import {useQuasar} from "quasar";

export default {
  name: "out_money",
  data() {
    let apartement_id = ref('')
    let main_page = ref(false)
    let checking = ref(true)
    const selected_out_come = reactive({
      name: '',
      type: '',
      kind: ''
    })
    const type = [
      {value: 'پرداخت کننده فقط مالکین ', id: 0}, {value: 'پرداخت کننده همه ساکنین', id: 1}
    ]
    const kind = [{value: 'مساوی', id: 0}, {value: 'متراژ', id: 1}, {value: 'نفرات', id: 2}]
    const create_data = {
      month: '',
      data: {
        date: '',
        price: 0,
        discripe: '',
        cost: ''
      }
    }
    const all_data = []
    const searching_data = reactive({
      list_building: [],
    })
    let money_list = reactive([])

    function start() {
      const address = new URLS()
      axios.get(address.create_money_list()).then(value => {
        if (value.data.done === true) {
          money_list.splice(0, money_list.length)
          for (let i = 0; i < value.data.data.length; i++) {
            money_list.push(value.data.data[i])
          }
        }
      })
    }
    start()

    function searching() {
      const address = new URLS()
      axios.get(address.building_list()).then(value => {
        if (value.data.done === true) {
          searching_data.list_building = value.data.data
        }
      })
    }
    searching()


    const columns = reactive([
      {name: 'name', align: 'center', label: 'نام هزینه', field: 'name', sortable: true},
      {name: 'discripe', align: 'center', label: 'توضیج هزینه', field: 'discripe', sortable: true},
      {name: 'price', align: 'center', label: 'قیمت', field: 'price', sortable: true}
    ])
    const rows = reactive([])
    const $q = useQuasar()

    return {

      searching_data,
      apartement_id,
      main_page,
      start,
      money_list,
      columns,
      rows,
      all_data,
      create_data,
      checking,
      kind,
      selected_out_come,
      type,
      date: ref(''),
      icon: ref(false),
      bar: ref(false),
      bar2: ref(false),
      toolbar: ref(false),
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
    deleteـitem(probs) {
      this.all_data.splice(probs.rowIndex, 1)
      this.rows.splice(probs.rowIndex, 1)
    },

    create_cash() {
      const address = new URLS()
      axios.post(address.create_money(), {
        "name": this.selected_out_come.name,
        "type": this.selected_out_come.type.id,
        "kind": this.selected_out_come.kind.id
      }).then(value => {
        if (value.data.done === true) {
          this.selected_out_come.name = ''
          this.selected_out_come.type = ''
          this.selected_out_come.kind = ''
          this.start()
          this.toast('عملیات با موفقیت انجام شد', 'green', 'white')
        } else {
          this.toast('خطا در انجام عملیات ( نام هزینه تکراری است )', 'red', 'white')
        }
      })

    },

    insert_data_table() {
      if (this.create_data.data.cost.id !== '' && this.create_data.data.cost.id !== undefined) {
        this.rows.push({
          name: this.create_data.data.cost.name,
          discripe: this.create_data.data.discripe,
          price: this.create_data.data.price,
          id: this.create_data.data.cost.id
        })

        this.all_data.push({
          name: this.create_data.data.cost.name,
          discripe: this.create_data.data.discripe,
          price: this.create_data.data.price,
          id: this.create_data.data.cost.id
        })


        this.create_data.data.cost = ''
        this.create_data.data.price = 0
        this.create_data.data.discripe = ""
        this.create_data.data.date = ''
      } else {
        this.toast('یک هزینه می بایست انتخاب شود ', 'red', 'white')
      }
    },

    create_month() {
      if (this.create_data.month !== '') {
        const address = new URLS()
        axios.get(address.check_name(), {
          params: {name: this.create_data.month}
        }).then(value => {
          if (value.data > 0) {
            this.toast('نام ماه تکراری است ', 'red', 'white')
          } else {
            this.checking = false
          }
        })
      } else {
        this.toast('لطفا نام ماه  را انتخاب کنید ', 'orange-14', 'black')
      }
    },

    select_building(){
      this.main_page = true
    },

    insert_to_db(){
      if (this.all_data.length > 0 ){
        const  address = new URLS()
        axios.post(address.insert_factor_to_db() , {
          "data": this.all_data,
          "apartement_id": this.apartement_id.id,
          "month": this.create_data.month
        }).then(value => {
          if (value.data.done ===true){
            this.toast('فاکتور با موفقیت ثبت شد' , 'green' , 'white')
            this.rows=[]
            this.all_data=[]
          }
          else {
            this.toast('خطا در ثبت فاکتور' , 'red' , 'white')
          }
        })
      }
      else {
        this.toast('هزینه ای ثبت نشده است' , 'red' , 'white')
      }

    }
  },

  computed: {
    sum() {
      if (this.all_data.length > 0) {
        let sums = 0
        for (let i = 0; i < this.all_data.length; i++) {
          sums = sums + parseFloat(this.all_data[i].price)
        }
        return sums
      } else return 0
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
