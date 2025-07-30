<template>
	<ion-page>
		<ion-content :fullscreen="true">
			<FormView
				v-if="formFields.data"
				doctype="Employee Resignation"
				v-model="resignationRequest"
				:isSubmittable="true"
				:fields="formFields.data"
				:id="props.id"
				@validateForm="validateForm"
			/>
		</ion-content>
	</ion-page>
</template>

<script setup>
import { IonPage, IonContent } from "@ionic/vue"
import { createResource } from "frappe-ui"
import { ref, watch, inject } from "vue"

import FormView from "@/components/FormView.vue"

const employee = inject("$employee")
const __ = inject("$translate")

const props = defineProps({
	id: {
		type: String,
		required: false,
	},
})

// reactive object to store form data
const resignationRequest = ref({})

// get form fields
const formFields = createResource({
	url: "hrms.api.get_doctype_fields",
	params: { doctype: "Employee Resignation" },
	auto: true,
	transform(data) {
		if (props.id) return data
		return data.filter(
			(field) => !["employee", "employee_name", "status", "company"].includes(field.fieldname)
		)
	},
})

// form scripts
watch(
	() => resignationRequest.value.employee,
	(employee_id) => {
		if (props.id && employee_id !== employee.data.name) {
			// if employee is not the current user, set form as read only
			setFormReadOnly()
		}
	}
)

// watch(
// 	() => resignationRequest.value.resignation_submission_date,
// 	(submission_date) => {
// 		if (submission_date) {
// 			validateResignationDate(submission_date)
// 		}
// 	}
// )

// helper functions
function setFormReadOnly() {
	formFields.data.map((field) => (field.read_only = true))
}

// function validateResignationDate(submission_date) {
// 	const selectedDate = new Date(submission_date)
// 	const today = new Date()
// 	const minRequiredDate = new Date(today)
// 	minRequiredDate.setDate(today.getDate() + 30)

// 	const submission_date_field = formFields.data.find((field) => field.fieldname === "resignation_submission_date")
// 	if (selectedDate < minRequiredDate) {
// 		submission_date_field.error_message = __("Resignation submission date must be at least 30 days from today")
// 	} else {
// 		submission_date_field.error_message = ""
// 	}
// }

function validateForm() {
	resignationRequest.value.employee = employee.data.name
}
</script> 