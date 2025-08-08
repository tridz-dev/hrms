<template>
	<BaseLayout>
		<template #body>
			<!-- Custom header with back button -->
			<header class="flex flex-row bg-white shadow-sm py-4 px-3 items-center justify-between border-b sticky top-0 z-10">
				<Button variant="ghost" class="!pl-0 hover:bg-white" @click="router.back()">
					<FeatherIcon name="chevron-left" class="h-5 w-5" />
				</Button>
				<h2 class="text-xl font-semibold text-gray-900">{{ __("Asset Request") }}</h2>
				<div style="width:2rem"></div>
			</header>

			<div class="flex flex-col mt-7 mb-7 p-4 gap-7">
				<div class="w-full">
					<router-link :to="{ name: 'AssetRequestFormView' }" v-slot="{ navigate }">
						<Button @click="navigate" variant="solid" class="w-full py-5 text-base">
							{{ __("Request Asset") }}
						</Button>
					</router-link>
				</div>
				<div>
					<div class="text-lg text-gray-800 font-bold">{{ __("Recent Asset Requests") }}</div>
					<RequestList
						:component="markRaw(AssetRequestItem)"
						:items="assetRequests"
						:addListButton="true"
						:listButtonRoute="'AssetRequestListView'"
						@itemClick="openRequestModal"
					/>
				</div>
			</div>
			<ion-modal
				:is-open="isRequestModalOpen"
				@didDismiss="closeRequestModal"
				:initial-breakpoint="1"
				:breakpoints="[0, 1]"
			>
				<RequestActionSheet
					v-if="selectedRequest"
					v-model="selectedRequest"
					:showOpenForm="selectedRequest?.docstatus === 0"
					@openFormView="handleEdit"
				/>
			</ion-modal>
		</template>
	</BaseLayout>
</template>

<script setup>
import { computed, inject, markRaw, ref } from "vue"
import BaseLayout from "@/components/BaseLayout.vue"
import RequestList from "@/components/RequestList.vue"
import RequestActionSheet from "@/components/RequestActionSheet.vue"
import AssetRequestItem from "@/components/AssetRequestItem.vue"
import { myAssetRequests } from "@/data/asset_request"
import { useRouter } from "vue-router"
import { FeatherIcon } from "frappe-ui"

const __ = inject("$translate")
const router = useRouter()

const isRequestModalOpen = ref(false)
const selectedRequest = ref(null)

// Fix: Ensure we always have an array, even when data is loading or null
const assetRequests = computed(() => {
	const data = myAssetRequests?.data || []
	return Array.isArray(data) ? data.slice(0, 5) : []
})

const openRequestModal = (request) => {
  selectedRequest.value = request
  isRequestModalOpen.value = true
}
const closeRequestModal = () => {
  isRequestModalOpen.value = false
  selectedRequest.value = null
}
const handleEdit = () => {
  closeRequestModal()
  router.push({ name: 'AssetRequestFormView', params: { id: selectedRequest.value.name } })
}
</script> 