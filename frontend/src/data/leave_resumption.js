import { createResource } from "frappe-ui"
import { employeeResource } from "./employee"

const transformLeaveResumptionRequests = (data) => {
    return data.map((request) => {
        request.doctype = "Leave Resumption"
        return request
    })
}

export const myLeaveResumptionRequests = createResource({
    url: "hrms.api.leave_resumption.get_leave_resumption_requests",
    params: {
        employee: employeeResource.data.name,
        limit: 10,
    },
    auto: true,
    cache: "hrms:my_leave_resumption_requests",
    transform(data) {
        return transformLeaveResumptionRequests(data)
    },
})


