<template>
	<ion-page>
		<ListView
			doctype="Asset Request"
			:pageTitle="__('Asset Request History')"
			:fields="ASSET_REQUEST_FIELDS"
			:filterConfig="FILTER_CONFIG"
		/>
	</ion-page>
</template>

<script setup>
import { IonPage } from "@ionic/vue"
import ListView from "@/components/ListView.vue"
import { inject } from "vue"

const __ = inject("$translate")

const ASSET_REQUEST_FIELDS = ["name", "employee", "request_date", "requested_item_name", "reason_for_request", "docstatus"]
const FILTER_CONFIG = [
	{
		fieldname: "employee",
		fieldtype: "Link",
		label: __("Employee"),
		options: "Employee",
	},
	{ fieldname: "request_date", fieldtype: "Date", label: __("Request Date") },
	{ fieldname: "requested_item_name", fieldtype: "Data", label: __("Requested Item Name") },

]
</script> 