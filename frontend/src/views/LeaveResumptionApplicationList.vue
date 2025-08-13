<template>
	<ion-page>
		<ListView
			doctype="Leave Resumption"
			:pageTitle="__('Leave Resumption History')"
			:fields="LEAVE_RESUMPTION_FIELDS"
			:filterConfig="FILTER_CONFIG"
		/>
	</ion-page>
</template>

<script setup>
import { IonPage } from "@ionic/vue"
import ListView from "@/components/ListView.vue"
import { inject } from "vue"

const __ = inject("$translate")

const LEAVE_RESUMPTION_FIELDS = ["name", "employee", "join_date", "comment", "docstatus"]
const FILTER_CONFIG = [
    {
        fieldname: "employee",
        fieldtype: "Link",
        label: __("Employee"),
        options: "Employee",
    },
    { fieldname: "join_date", fieldtype: "Date", label: __("Join Date") },
]
</script>


