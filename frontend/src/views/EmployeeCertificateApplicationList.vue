<template>
	<ion-page>
		<ListView
			doctype="Employee Certificate"
			:pageTitle="__('Employee Certificate History')"
			:fields="EMPLOYEE_CERTIFICATE_FIELDS"
			:filterConfig="FILTER_CONFIG"
		/>
	</ion-page>
</template>

<script setup>
import { IonPage } from "@ionic/vue"
import ListView from "@/components/ListView.vue"
import { inject } from "vue"

const __ = inject("$translate")

const EMPLOYEE_CERTIFICATE_FIELDS = ["name", "employee", "purpose", "reason", "certificate_date", "docstatus"]
const FILTER_CONFIG = [
    {
        fieldname: "employee",
        fieldtype: "Link",
        label: __("Employee"),
        options: "Employee",
    },
    { fieldname: "purpose", fieldtype: "Link", label: __("Purpose"), options: "Employee Certificate Purpose" },
    { fieldname: "certificate_date", fieldtype: "Date", label: __("Certificate Date") },
]
</script>
