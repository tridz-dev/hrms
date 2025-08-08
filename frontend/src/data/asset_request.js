import { createResource } from "frappe-ui"
import { employeeResource } from "./employee"

const transformAssetRequests = (data) => {
	return data.map((request) => {
		request.doctype = "Asset Request"
		return request
	})
}

export const myAssetRequests = createResource({
	url: "hrms.api.asset_request.get_asset_requests",
	params: {
		employee: employeeResource.data.name,
		limit: 10,
	},
	auto: true,
	cache: "hrms:my_asset_requests",
	transform(data) {
		return transformAssetRequests(data)
	}
}) 