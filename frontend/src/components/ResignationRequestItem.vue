<template>
	<ListItem
		:isTeamRequest="props.isTeamRequest"
		:employee="props.doc.employee"
		:employeeName="props.doc.employee_name"
	>
		<template #left>
			<div class="flex flex-col items-start gap-1.5">
				<div class="text-base font-normal text-gray-800 truncate max-w-[150px]">
					{{ props.doc.reason_for_resignation }}
				</div>
				<div class="text-xs font-normal text-gray-500">
					<span>{{ props.doc.resignation_submission_date }}</span>
					<span v-if="props.doc.last_working_date">
						<span class="whitespace-pre"> &middot; </span>
						<span class="whitespace-nowrap">{{ props.doc.last_working_date }}</span>
					</span>
				</div>
			</div>
		</template>
		<template #right>
			<Badge variant="outline" :theme="colorMap[status]" :label="__(status)" size="md" />
			<FeatherIcon name="chevron-right" class="h-5 w-5 text-gray-500" />
		</template>
	</ListItem>
</template>

<script setup>
import { computed } from "vue"
import { Badge, FeatherIcon } from "frappe-ui"

import ListItem from "@/components/ListItem.vue"

const props = defineProps({
	doc: {
		type: Object,
	},
	workflowStateField: {
		type: String,
		required: false,
	},
	isTeamRequest: {
		type: Boolean,
		default: false,
	},
})

const status = computed(() => {
	if (props.workflowStateField) return props.doc[props.workflowStateField]
	return props.doc.docstatus ? "Submitted" : "Draft"
})

const colorMap = {
	Draft: "gray",
	Submitted: "blue",
	Approved: "green",
	Rejected: "red",
	"Pending HR Approval": "blue",
	"Pending LM Approval": "blue"
}
</script> 