<template>
	<ion-page>
		<ListView
			doctype="Employee Resignation"
			:pageTitle="__('Resignation Request History')"
			:fields="RESIGNATION_FIELDS"
			:filterConfig="FILTER_CONFIG"
		/>
	</ion-page>
</template>

<script setup>
import { IonPage } from "@ionic/vue"
import ListView from "@/components/ListView.vue"
import { inject } from "vue"

const __ = inject("$translate")

const RESIGNATION_FIELDS = ["name", "employee", "resignation_submission_date", "last_working_date", "reason_for_resignation", "docstatus"]
const FILTER_CONFIG = [
	{
		fieldname: "employee",
		fieldtype: "Link",
		label: __("Employee"),
		options: "Employee",
	},
	{ fieldname: "resignation_submission_date", fieldtype: "Date", label: __("Submission Date") },
	{ fieldname: "last_working_date", fieldtype: "Date", label: __("Last Working Date") },
]
</script> 