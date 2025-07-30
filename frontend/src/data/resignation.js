import { createResource } from "frappe-ui"
import { employeeResource } from "./employee"

const transformResignationRequests = (data) => {
	return data.map((request) => {
		request.doctype = "Employee Resignation"
		return request
	})
}

export const myResignationRequests = createResource({
	url: "hrms.api.resignation.get_resignation_requests",
	params: {
		employee: employeeResource.data.name,
		limit: 10,
	},
	auto: true,
	cache: "hrms:my_resignation_requests",
	transform(data) {
		return transformResignationRequests(data)
	}
}) 