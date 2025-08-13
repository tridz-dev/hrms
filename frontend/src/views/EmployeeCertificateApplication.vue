<template>
	<ion-page>
		<ion-content :fullscreen="true">
			<FormView
				v-if="formFields.data"
				doctype="Employee Certificate"
				v-model="employeeCertificate"
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
const employeeCertificate = ref({})

// get form fields
const formFields = createResource({
    url: "hrms.api.get_doctype_fields",
    params: { doctype: "Employee Certificate" },
    auto: true,
    transform(data) {
        if (props.id) return data
        return data.filter((field) => !["employee","reference_no","address","salary","bank_account_number","subject_account_type","bank_name"].includes(field.fieldname))
    },
})

// form scripts
watch(
    () => employeeCertificate.value.employee,
    (employee_id) => {
        if (props.id && employee_id !== employee.data.name) {
            // if employee is not the current user, set form as read only
            setFormReadOnly()
        }
    }
)

// helper functions
function setFormReadOnly() {
    formFields.data.map((field) => (field.read_only = true))
}

function validateForm() {
    employeeCertificate.value.employee = employee.data.name
}
</script>
