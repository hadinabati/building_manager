<template>
<div class="row">
  <q-select standout bg-color="teal-5" rounded  class="mySelect" label="نام ماه"></q-select>
  <q-table
    style="margin-right: 5% ; margin-left: 5% ; margin-top: 2rem"
    class="table"
    dense
    title="Treats"
    :rows="rows"
    :columns="columns"
    row-key="name"
  />
</div>
</template>

<script>
export default {
  name: "incoming_page"
}
</script>

<style scoped>
.mySelect{
  font-family: myvazir;
  width: 60%;
  margin-right: 20%;
  margin-left: 20%;
  margin-top: 2rem;
}
.table{
  width: 90%;
  margin-top: 2rem;
  margin-right: 5%;
  margin-left: 5%;
  font-family: myvazir;
}
</style>
